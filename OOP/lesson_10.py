def suppress(errors, *, or_return=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                return or_return
        return inner
    return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
    return 1 // 0


print(foo())  # 42


@suppress((KeyError, IndexError))
def get_item(key, structure):
    return structure[key]


print(get_item(7, "foo") is None)  # True
print(get_item('a', {}) is None)  # True
