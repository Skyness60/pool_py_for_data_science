def ft_filter(function_to_apply, iterable):
    """
    Filter the iterable using the function_to_apply.

    Args:
        function_to_apply (callable): The function to apply to each item in the iterable.
        iterable (iterable): The iterable to filter.

    Returns:
        generator: A generator that yields items from the iterable for which function_to_apply returns True.
    """
    return (item for item in iterable if function_to_apply(item))
