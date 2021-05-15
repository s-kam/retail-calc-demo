from operator import methodcaller
from os.path import abspath, dirname, join

from setuptools import find_packages, setup

_NAME = 'retail_calc_demo'

_CURRENT_DIRPATH = abspath(dirname(__file__))
_requirements = {}

for filename in (
    'requirements.in',
    'requirements-dev.in',
):
    with open(join(_CURRENT_DIRPATH, filename), 'r') as f:
        _requirements[filename] = tuple(filter(
            lambda line: line and not line.startswith('-'),
            map(methodcaller('strip'), f.readlines()),
        ))

setup(
    name=_NAME,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Aiohttp',
    ],
    version='0.1.0',
    packages=find_packages(exclude=[f'{_NAME}.tests*']),
    include_package_data=True,
    url='https://github.com/s-kam/retail-calc-demo',
    author='s-kam',
    author_email='salyakhutdinov.k@gmail.com',
    platforms=['*nix'],
    description='Retail Calculator Demo',
    python_requires='>=3.7,<3.10',
    install_requires=_requirements['requirements.in'],
    extras_require={
        'dev': _requirements['requirements-dev.in'],
    },
    entry_points={
        'console_scripts': [
            f'{_NAME}_run = '
            f'{_NAME}.scripts:run_app',
        ],
    }
)
