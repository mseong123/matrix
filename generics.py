'''
define generic K for multiple use in matrix
'''

from typing import TypeVar
from vector import Vector
from matrix import Matrix

K = TypeVar("K", int, float)

V = TypeVar("V", int, float, Matrix, Vector)
