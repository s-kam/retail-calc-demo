from decimal import Decimal
from typing import NamedTuple

__all__ = [
    'CalculationResultData',
]


class CalculationResultData(NamedTuple):
    subtotal_with_discount: Decimal
    total: Decimal
