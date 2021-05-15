from os.path import join

from pytest import fixture

from retail_calc_demo.app import create_app
from retail_calc_demo.utils import BASE_DIR, yaml_safe_load


@fixture(scope='session')
def app_settings():
    return yaml_safe_load(
        join(BASE_DIR, 'retail_calc_demo', 'tests', 'test.yaml'),
    )


@fixture()
def app(app_settings):
    return create_app(settings=app_settings)


@fixture()
async def app_client(aiohttp_client, app):
    return await aiohttp_client(app)
