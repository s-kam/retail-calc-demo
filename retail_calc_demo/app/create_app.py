from os.path import join
from typing import Mapping

from aiohttp.web import Application
from marshmallow import ValidationError

from retail_calc_demo.constant import APP_SETTINGS_LABEL, \
    KNOWN_STATE_CODES_SETTING_LABEL, TAX_RATES_SETTING_LABEL
from retail_calc_demo.data import AppSettingsDataSchema
from retail_calc_demo.utils import BASE_DIR
from .exc import AppConfigValidationError
from .middlewares import error_middleware
from .views import calc_view, index_view, state_codes_view

__all__ = [
    'create_app',
]


def create_app(settings: Mapping) -> Application:
    app = Application()

    try:
        settings = AppSettingsDataSchema().load(settings)

    except ValidationError as err:
        raise AppConfigValidationError(*err.args, **err.kwargs) from err

    settings[KNOWN_STATE_CODES_SETTING_LABEL] = frozenset(
        settings[TAX_RATES_SETTING_LABEL],
    )
    app[APP_SETTINGS_LABEL] = settings

    app.middlewares.append(error_middleware)

    app.router.add_get('/calc', calc_view)
    app.router.add_get('/state_codes', state_codes_view)
    app.router.add_get('/', index_view)
    app.router.add_static(
        '/',
        path=join(BASE_DIR, 'retail_calc_demo', 'app', 'static'),
        name='static',
    )

    return app
