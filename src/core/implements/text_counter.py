"""
Defines all the implemented tasks in the main application
"""


def map_task(items):
    """
    Creates a built-in python diccionary with the items received as a parameter
    as a key and counting the occurrences of the items as a value

    Args:
        items (list): items to work with, creating a key:value map with item
        and its occurrences
    """
    dic = {}
    for item in items:
        dic[item] = dic.get(item, 0) + 1

    return dic


def reduce_task(*items):
    """
    Converges the keys for the n items received, performing the sum operation
    with all the values of the same key and returning a joined dictionary

    Args:
        *args (dict): dictionaries to join summing their values with equal keys

    Returns:
        dict: merged dictionary
    """
    merged = dict()
    keys = set().union(*items)
    for key in keys:
        merged[key] = sum([x.get(key, 0) for x in items])
    return merged
