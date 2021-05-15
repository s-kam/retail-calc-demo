from argparse import ArgumentParser
from os.path import join

from aiohttp.web import run_app as run

from retail_calc_demo.app import create_app
from retail_calc_demo.utils import BASE_DIR, yaml_safe_load

__all__ = [
    'run_app',
]


def run_app() -> None:
    parser = ArgumentParser(
        description='Retail calculator demo app runner.'
    )
    parser.add_argument(
        '-c',
        '--config-file',
        default=join(BASE_DIR, 'config', 'retail_calc_demo.yaml'),
        help='Config file path for app.'
    )
    args = parser.parse_args()

    run(
        create_app(yaml_safe_load(args.config_file))
    )


if __name__ == "__main__":
    run_app()
