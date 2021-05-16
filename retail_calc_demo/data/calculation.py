from decimal import Decimal
from typing import Mapping, Union

from retail_calc_demo.container import CalculationResultData

__all__ = [
    'get_total',
]


def _get_discount(
    discounts: Mapping[int, Decimal],
    quantity: int,
) -> Decimal:
    """
    Get discount by order quantity.

    Note: in case of performance issue try to change
    implementation to binary search algorithm.
    """
    discount_categories = sorted(discounts, reverse=True)
    for category in discount_categories:
        if quantity >= category:
            return discounts[category]

    return Decimal('0')


def get_total(
    quantity: int,
    price: Decimal,
    state_code: str,
    settings: Mapping[str, Mapping[Union[str, int], Decimal]],
) -> CalculationResultData:
    """Calculation of order subtotal with discount and total with taxes."""
    discount = _get_discount(settings['discounts'], quantity)
    tax_rate = settings['tax_rates'][state_code]
    subtotal = quantity * price
    subtotal_with_discount = subtotal - subtotal / 100 * discount
    total = subtotal_with_discount + subtotal_with_discount / 100 * tax_rate

    return CalculationResultData(subtotal_with_discount, total)
