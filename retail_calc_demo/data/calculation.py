from decimal import Decimal
from typing import Mapping

from retail_calc_demo.container import CalculationResultData

__all__ = [
    'calculate_totals',
]


def _get_discount(
    discounts: Mapping[int, Decimal],
    quantity: int,
) -> Decimal:
    """
    Get discount by order quantity.

    Note: in case of performance issue try to implement binary search
    algorithm instead.
    """
    discount_categories = sorted(discounts, reverse=True)
    for category in discount_categories:
        if quantity >= category:
            return discounts[category]

    return Decimal('0')


def calculate_totals(
    quantity: int,
    price: Decimal,
    discounts: Mapping[int, Decimal],
    tax_rate: Decimal,
) -> CalculationResultData:
    """Calculation of order subtotal with discount and total with taxes."""
    discount = _get_discount(discounts, quantity)

    subtotal = quantity * price
    subtotal_with_discount = subtotal - subtotal / 100 * discount
    total = subtotal_with_discount + subtotal_with_discount / 100 * tax_rate

    return CalculationResultData(subtotal_with_discount, total)
