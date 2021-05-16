from typing import Awaitable, Callable

from aiohttp.web_exceptions import HTTPException, HTTPFound
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from retail_calc_demo.constant import GET_PARAMS_ERROR_MESSAGE, \
    UNKNOWN_ERROR_MESSAGE
from retail_calc_demo.utils import json_response
from .exc import RequestQueryValidationError

__all__ = [
    'error_middleware',
]


@middleware
async def error_middleware(
    request: Request,
    handler: Callable[[Request], Awaitable],
) -> Response:
    logger = request.app.logger
    try:
        return await handler(request)

    except HTTPFound as err:
        raise err

    except HTTPException as err:
        return json_response(
            {
                'identity': 'HTTP',
                'data': {
                    'reason': err.reason,
                },
            },
            status=err.status,
        )

    except RequestQueryValidationError as err:
        logger.exception(err)

        return json_response(
            {
                'identity': GET_PARAMS_ERROR_MESSAGE,
                'data': err.messages,
            },
            status=400,
        )

    except Exception as err:  # pylint: disable=broad-except
        logger.exception(err)

        return json_response(
            {
                'identity': UNKNOWN_ERROR_MESSAGE,
                'data': None,
            },
            status=500,
        )
