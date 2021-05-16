from typing import Union
from decimal import Decimal

from marshmallow import Schema
from marshmallow.fields import Decimal as DecimalField, Dict, Integer, String

from retail_calc_demo.constant import DISCOUNTS_SETTING_LABEL, \
    PRICE_GET_PARAM_LABEL, QUANTITY_GET_PARAM_LABEL, \
    STATE_CODE_GET_PARAM_LABEL, TAX_RATES_SETTING_LABEL

__all__ = [
    'AppSettingsDataSchema',
    'CalcViewDataSchema',
]


def _positive_number_validator(value: Union[int, Decimal]) -> bool:
    return value > 0


def _non_negative_number_validator(value: Union[int, Decimal]) -> bool:
    return value >= 0


def _percent_validator(value: Union[int, Decimal]) -> bool:
    return _non_negative_number_validator(value) and value <= 100


# App config file schema.
AppSettingsDataSchema = Schema.from_dict({
    DISCOUNTS_SETTING_LABEL: Dict(
        keys=Integer(validate=_non_negative_number_validator),
        values=DecimalField(validate=_percent_validator),
        required=True,
    ),
    TAX_RATES_SETTING_LABEL: Dict(
        keys=String,
        values=DecimalField(validate=_percent_validator),
        required=True,
    ),
})

# GET params schema for calculation view.
CalcViewDataSchema = Schema.from_dict({
    QUANTITY_GET_PARAM_LABEL: Integer(
        required=True,
        validate=_positive_number_validator
    ),
    PRICE_GET_PARAM_LABEL: DecimalField(
        required=True,
        validate=_positive_number_validator
    ),
    STATE_CODE_GET_PARAM_LABEL: String(required=True),
})
