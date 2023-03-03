from abc import ABCMeta, abstractmethod


class Kind(metaclass=ABCMeta):
    """A kind is a type"""

    __slots__ = ()


def kind_function(funtion: callable) -> callable:
    """A decorator that marks a function as a kind function"""
    funtion.__isabstractmethod__ = True
    return funtion
