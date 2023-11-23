import pytest
from pizza import Margherita, Pepperoni, Hawaiian


def test_pizza_class():
    margherita_large = Margherita('L')
    pepperoni_extra_large = Pepperoni('XL')
    hawaiian_large = Hawaiian('L')
    hawaiian_extra_large = Hawaiian('XL')

    assert (margherita_large.dict() ==
            {'Size': 'L',
             'Ingredients': ['Tomato sauce', 'Mozzarella', 'Tomatoes']})
    assert (pepperoni_extra_large.dict() ==
            {'Size': 'XL',
             'Ingredients': ['Tomato sauce', 'Mozzarella', 'Pepperoni']})
    assert (hawaiian_large.dict() ==
            {'Size': 'L',
             'Ingredients': ['Tomato sauce', 'Mozzarella',
                             'Chicken', 'Pineapples']})

    assert hawaiian_large == hawaiian_large
    assert hawaiian_large != hawaiian_extra_large
    assert hawaiian_large != margherita_large


if __name__ == "__main__":
    pytest.main()
