import pytest
from click.testing import CliRunner
from order_menu_func import order, menu


def test_order_with_valid_pizza_type():
    runner = CliRunner()
    result = runner.invoke(order, ['Margherita'])
    assert result.exit_code == 0
    assert 'Prepared in' in result.output


def test_order_with_valid_pizza_type_and_delivery():
    runner = CliRunner()
    result = runner.invoke(order, ['Margherita', '--delivery'])
    assert result.exit_code == 0
    assert 'Prepared in' in result.output
    assert 'Delivered in' in result.output


def test_order_with_invalid_pizza_type():
    runner = CliRunner()
    result = runner.invoke(order, ['InvalidType'])
    assert result.exit_code == 0
    assert 'Sorry, it is not available on the menu.' in result.output


def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    assert 'Menu:' in result.output
    assert 'Margherita' in result.output
    assert 'Pepperoni' in result.output
    assert 'Hawaiian' in result.output


if __name__ == '__main__':
    pytest.main()