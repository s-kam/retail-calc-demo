from marshmallow import ValidationError

__all__ = [
    'AppConfigValidationError',
    'RequestQueryValidationError',
    'UnknownStateCodeValidationError',
]


class AppConfigValidationError(ValidationError):
    """App configuration validation error."""


class RequestQueryValidationError(ValidationError):
    """Request query parameters validation error."""


class UnknownStateCodeValidationError(RequestQueryValidationError):
    """Unknown state code query parameter error."""
