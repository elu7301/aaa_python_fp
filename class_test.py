import pytest
from pizza_class import Margherita, Pepperoni, Hawaiian


def test_pizza_class():
    margherita_l = Margherita('L')
    pepperoni_xl = Pepperoni('XL')
    hawaiian_l = Hawaiian('L')
    hawaiian_xl = Hawaiian('XL')

    assert (margherita_l.dict() ==
            {'Size': 'L',
             'Ingredients': ['Tomato sauce', 'Mozzarella', 'Tomatoes']})
    assert (pepperoni_xl.dict() ==
            {'Size': 'XL',
             'Ingredients': ['Tomato sauce', 'Mozzarella', 'Pepperoni']})
    assert (hawaiian_l.dict() ==
            {'Size': 'L',
             'Ingredients': ['Tomato sauce', 'Mozzarella',
                             'Chicken', 'Pineapples']})

    assert hawaiian_l == hawaiian_l
    assert hawaiian_l != hawaiian_xl
    assert hawaiian_l != margherita_l


if __name__ == "__main__":
    pytest.main()
