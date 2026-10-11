"""Parse invoice lines and add them up."""

from decimal import Decimal


def parse_line(line: str) -> tuple[str, Decimal]:
    """'Coffee beans, 12.50' -> ('Coffee beans', Decimal('12.50'))"""
    item, _, amount = line.rpartition(",")
    return item.strip(), Decimal(amount.strip())


def total(lines: list[str]) -> Decimal:
    return sum((parse_line(line)[1] for line in lines), Decimal("0"))
