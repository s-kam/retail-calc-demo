from typing import Any

from aiohttp.web_exceptions import HTTPFound
from aiohttp.web_response import Response
from simplejson import dumps

from retail_calc_demo.data import CalcViewDataSchema, get_total
from .cache import CachedViewResponse

__all__ = [
    'calc_view',
    'state_codes_view',
    'index_view',
]


def _make_json_response(data: Any) -> Response:
    return Response(
        text=dumps(data),
        content_type='application/json',
    )


@CachedViewResponse()
async def calc_view(request):
    """Order subtotal and total calculation."""
    params = CalcViewDataSchema().load(request.query)
    return _make_json_response(get_total(
        params['quantity'],
        params['price'],
        params['state_code'],
        request.app['settings'],
    )._asdict())


@CachedViewResponse()
async def state_codes_view(request):
    """Known state codes."""
    return _make_json_response(tuple(request.app['settings']['tax_rates']))


async def index_view(request):
    """Redirect to static index.html from root."""
    raise HTTPFound('/index.html')
