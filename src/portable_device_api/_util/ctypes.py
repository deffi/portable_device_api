from ctypes import POINTER


def null_pointer(type_):
    """This is a workaround for PyCharm complaining about parameter 'arg' being
    unfilled"""

    # noinspection PyArgumentList
    return POINTER(type_)()
