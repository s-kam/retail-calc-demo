from typing import Mapping

from aiohttp.web import Application

from .views import calc_view

__all__ = [
    'create_app',
]


def create_app(settings: Mapping) -> Application:
    app = Application()
    app['settings'] = settings

    app.router.add_get('/', calc_view)
    return app
