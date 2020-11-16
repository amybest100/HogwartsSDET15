def singleton(func):
    """
    暂时不用过分了解
    """
    _instance = {}

    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)
            return _instance[func]

    return wrapper()
