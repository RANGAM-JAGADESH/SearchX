import re
from decimal import Decimal

def parse_price(value):
    """
    Convert different price formats into Decimal.
    """

    if value is None:
        return Decimal("0.00")

    value = str(value).strip()

    # Handle NaN
    if value.lower() == "nan":
        return Decimal("0.00")

    # Remove commas
    value = value.replace(",", "")

    # Keep only digits and decimal point
    value = re.sub(r"[^0-9.]", "", value)

    if value == "":
        return Decimal("0.00")

    try:
        return Decimal(value)
    except:
        return Decimal("0.00")