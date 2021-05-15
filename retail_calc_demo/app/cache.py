from hashlib import sha1
from typing import Awaitable, Callable, Optional

from aiocache import cached
from aiocache.base import SENTINEL
from aiohttp.web_request import Request
from aiohttp.web_response import StreamResponse

__all__ = [
    'CachedViewResponse',
]


_URI_BASED_CACHE_KEY_PREFIX = 'cache:view'


def _generate_view_response_cache_key(  # pylint: disable=unused-argument
    handler: Callable[..., Awaitable[StreamResponse]],
    request: Request,
    *args,
    **kwargs,
) -> str:
    """
    Generate view response cache key based on request path and sorted params.
    """
    get_params = request.query

    hash_ = sha1(request.path.encode('utf-8'))

    for param in sorted(get_params):
        hash_.update(param.encode('utf-8'))

        for value in sorted(get_params.getall(param)):
            hash_.update(str(value).encode('utf-8'))

    return f'{_URI_BASED_CACHE_KEY_PREFIX}:{request.method}:{hash_.hexdigest()}'


class CachedViewResponse(cached):
    """Overridden decorator ``aiocache.cached`` for view."""
    def __init__(self, ttl: Optional[int] = SENTINEL) -> None:
        super().__init__(
            key_builder=_generate_view_response_cache_key,
            ttl=ttl,
        )
