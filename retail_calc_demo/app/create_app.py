from asyncio import get_event_loop

from aiohttp.web import Application, run_app

from .views import calc_view

__all__ = [
    'create_app',
]


async def create_app():
    app = Application()
    app.router.add_get('/', calc_view)
    return app

if __name__ == "__main__":
    run_app(get_event_loop().run_until_complete(create_app()))
