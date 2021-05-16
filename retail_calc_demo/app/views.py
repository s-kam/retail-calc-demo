from aiohttp.web_exceptions import HTTPFound
from marshmallow import ValidationError

from retail_calc_demo.constant import APP_SETTINGS_LABEL, \
    DISCOUNTS_SETTING_LABEL, KNOWN_STATE_CODES_SETTING_LABEL, \
    PRICE_GET_PARAM_LABEL, \
    QUANTITY_GET_PARAM_LABEL, \
    STATE_CODE_GET_PARAM_LABEL, TAX_RATES_SETTING_LABEL, \
    UNKNOWN_STATE_CODE_GET_PARAM_ERROR_MESSAGE
from retail_calc_demo.data import CalcViewDataSchema, calculate_totals
from retail_calc_demo.utils import json_response
from .cache import CachedViewResponse
from .exc import RequestQueryValidationError, UnknownStateCodeValidationError

__all__ = [
    'calc_view',
    'state_codes_view',
    'index_view',
]


@CachedViewResponse()
async def calc_view(request):
    """Order subtotal and total calculation."""

    try:
        params = CalcViewDataSchema().load(request.query)

    except ValidationError as err:
        raise RequestQueryValidationError(*err.args, **err.kwargs) from err

    state_code = params[STATE_CODE_GET_PARAM_LABEL]
    settings = request.app[APP_SETTINGS_LABEL]

    if state_code not in settings[KNOWN_STATE_CODES_SETTING_LABEL]:
        raise UnknownStateCodeValidationError(
            message=UNKNOWN_STATE_CODE_GET_PARAM_ERROR_MESSAGE,
            field_name=STATE_CODE_GET_PARAM_LABEL,
        )

    return json_response(
        calculate_totals(
            params[QUANTITY_GET_PARAM_LABEL],
            params[PRICE_GET_PARAM_LABEL],
            settings[DISCOUNTS_SETTING_LABEL],
            settings[TAX_RATES_SETTING_LABEL][state_code],
        )._asdict(),
    )


@CachedViewResponse()
async def state_codes_view(request):
    """Known state codes."""
    return json_response(
        tuple(request.app[APP_SETTINGS_LABEL][KNOWN_STATE_CODES_SETTING_LABEL])
    )


async def index_view(request):
    """Redirect to static index.html from root."""
    raise HTTPFound('/index.html')
