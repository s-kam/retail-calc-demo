from decimal import Decimal

from retail_calc_demo.data import calculate_totals


def test_calculate_totals():
    # Zero values are allowed.
    assert calculate_totals(
        0,
        Decimal('0'),
        {},
        Decimal('0'),
    ) == (Decimal('0'), Decimal('0'))

    # Calculation without discounts and taxes.
    assert calculate_totals(
        1,
        Decimal('1'),
        {},
        Decimal('0'),
    ) == (Decimal('1'), Decimal('1'))

    # Too small for discount order.
    assert calculate_totals(
        10,
        Decimal('10'),
        {11: Decimal('1.3333'), 12: Decimal('0.01')},
        Decimal('0'),
    ) == (Decimal('100'), Decimal('100'))

    # Calculation with high precision.
    assert calculate_totals(
        10,
        Decimal('1.3333'),
        {0: Decimal('0'), 10: Decimal('1.3333'), 12: Decimal('100')},
        Decimal('1.3333'),
    ) == (Decimal('13.155231111'), Decimal('13.330629807402963'))
