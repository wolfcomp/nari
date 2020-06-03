"""Defines a helper class to bundle string hex IDs with an associated name"""

from ..types import HexStr

# pylint: disable=too-few-public-methods,redefined-builtin
class IdNamePair():
    """Represents a tuple where there's a hex id and a string name; automatically converts the hex string to an int"""
    def __init__(self, id: HexStr, name: str):
        self.id = int(id, 16)
        self.name = name

    def __repr__(self):
        return f'<Pair {self.id}:{self.name}>'
