from decimal import Decimal

from invoicekit import parse_line, total


def test_parse_line():
    assert parse_line("Coffee beans, 12.50") == ("Coffee beans", Decimal("12.50"))


def test_total():
    assert total(["a, 1.25", "b, 2.75"]) == Decimal("4.00")
