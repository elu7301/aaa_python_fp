class Pizza:
    def __init__(self, size: str) -> None:
        """
        Initializes a new instance of the Pizza class.

        Args:
            size : The size of the pizza.

        Attributes:
            size : The size of the pizza.
            ingredients : The list of pizza ingredients,
                starting with default ingredients:
                'Tomato sauce' and 'Mozzarella'.
        """
        self.size = size
        self.ingredients = ['Tomato sauce', 'Mozzarella']

    def add_ingredients(self, ingredient: str) -> None:
        """
        Adds an ingredient to the pizza.

        Args:
            ingredient (str): The ingredient to be added.
        """
        self.ingredients.append(ingredient)

    def dict(self) -> dict:
        """
        Returns the pizza details as a dictionary.

        Returns:
            dict: A dictionary representing the
                pizza with keys 'Size' and 'Ingredients'.
        """
        return {
            'Size': self.size,
            'Ingredients': self.ingredients
        }

    def __eq__(self, other) -> bool:
        """
        Compares two pizzas for equality.

        Args:
            other (Pizza): The other pizza object to compare.

        Returns:
            bool: True if the pizzas have the
                same size and ingredients, False otherwise.
        """
        return (self.size == other.size
                and self.ingredients == other.ingredients)


class Margherita(Pizza):
    def __init__(self, size: str):
        """
        Initializes a new instance of the Margherita
            class, a subtype of Pizza.

        Args:
            size : The size of the Margherita pizza.

        Attributes:
            size : The size of the Margherita pizza.
            ingredients : The list of Margherita
                pizza ingredients, including 'Tomatoes'.
        """
        super().__init__(size)
        self.add_ingredients('Tomatoes')


class Pepperoni(Pizza):
    def __init__(self, size: str):
        """
        Initializes a new instance of the Pepperoni
            class, a subtype of Pizza.

        Args:
            size : The size of the Pepperoni pizza.

        Attributes:
            size : The size of the Pepperoni pizza.
            ingredients : The list of Pepperoni
                pizza ingredients, including 'Pepperoni'.
        """
        super().__init__(size)
        self.add_ingredients('Pepperoni')


class Hawaiian(Pizza):
    def __init__(self, size: str):
        """
        Initializes a new instance of the Hawaiian
            class, a subtype of Pizza.

        Args:
            size : The size of the Hawaiian pizza.

        Attributes:
            size : The size of the Hawaiian pizza.
            ingredients : The list of Hawaiian
                pizza ingredients, including 'Chicken' and 'Pineapples'.
        """
        super().__init__(size)
        self.add_ingredients('Chicken')
        self.add_ingredients('Pineapples')
