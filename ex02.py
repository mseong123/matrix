'''linear interpolation and main function to run test'''

from vector import Vector
from matrix import Matrix
from generics import V

def lerp(u: V, v:V , t:float) -> V:
    '''linear interpolation'''
    if not isinstance(u, type(v)):
        raise TypeError("first 2 argument are not of same type")
    if isinstance(u, Vector) or isinstance(u, Matrix) 
