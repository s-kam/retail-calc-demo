from os.path import join
from typing import Mapping

from aiohttp.web import Application

from retail_calc_demo.data import AppSettingsDataSchema
from retail_calc_demo.utils import BASE_DIR
from .views import calc_view, index_view, state_codes_view

__all__ = [
    'create_app',
]


def create_app(settings: Mapping) -> Application:
    app = Application()
    app['settings'] = AppSettingsDataSchema().load(settings)
    app.router.add_get('/calc', calc_view)
    app.router.add_get('/states', state_codes_view)
    app.router.add_get('/', index_view)
    app.router.add_static(
        '/',
        path=join(BASE_DIR, 'retail_calc_demo', 'app', 'static'),
        name='static',
    )
    return app
