from marshmallow import Schema
from marshmallow.fields import Decimal, Dict, Integer, String

__all__ = [
    'AppSettingsDataSchema',
    'CalcViewDataSchema',
]


class AppSettingsDataSchema(Schema):
    """App config file schema."""
    discounts = Dict(keys=Integer, values=Decimal, required=True)
    tax_rates = Dict(keys=String, values=Decimal, required=True)


class CalcViewDataSchema(Schema):
    """GET params schema for calculation view."""
    quantity = Integer(required=True)
    price = Decimal(required=True)
    state_code = String(required=True)
