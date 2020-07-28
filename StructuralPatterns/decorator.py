from functools import wraps


def make_blink(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of it's name and docstring
    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return '<blink>' + ret + '</blink>'

    return decorator


# Apply the decorator here
@make_blink
def hello_world():
    """Original function"""

    return 'Hello, World!'


if __name__ == "__main__":
    # check the result of decorating
    print(hello_world())

    # check if the name of the function is still the same name of the function being decorated
    print(hello_world.__name__)

    # check if the docstring of the function is still the docstring of the function being decorated
    print(hello_world.__doc__)
