import random


def log(func_or_template):
    """
    Decorator that logs the execution time
        of a function or uses a template string to log execution time.

    Args:
        func_or_template :
            If a string is provided,
                it is used as a template to log execution time.
            If a function is provided,
                it logs the execution time using the function name.

    Returns:
        function: Decorator function that logs the execution time.
    """
    template_given = isinstance(func_or_template, str)

    def decorator(func):
        def wrapped(*args, **kwargs):
            """
            Wrapper function that logs
                the execution time and calls the decorated function.

            Returns:
                Any: Return value of the decorated function.
            """
            if template_given:
                execution_time = random.randint(1, 30)
                print(func_or_template.format(execution_time))
            else:
                execution_time = random.randint(1, 30)
                print(f'{func.__name__} — {execution_time}s!')
            return func(*args, **kwargs)

        wrapped.__name__ = func.__name__
        wrapped.__doc__ = func.__doc__

        return wrapped

    return decorator if template_given else decorator(func_or_template)


@log
def bake(pizza):
    """
    Baking pizza

    Args:
        pizza (Pizza): The pizza to be baked.
    """


@log('🛵 Delivered for {}s!')
def delivery(pizza):
    """
    Delivering pizza

    Args:
        pizza (Pizza): The pizza to be delivered.
    """


@log('🏠 Picked-up for {}s!')
def pickup(pizza):
    """
    Self pick-up

    Args:
        pizza (Pizza): The pizza to be picked up.
    """
