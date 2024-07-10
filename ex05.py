'''ex05 - cosine angle and main function to run test'''

from typing import TypeVar
from vector import Vector

K = TypeVar("K", int, float)

def angle_cos(u: Vector[K], v:Vector[K]) -> float:
    """return cos angle"""
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("argument is not of Vector type")
    # error handling for generic type done in dot method in vector class
    if all(value== 0 for value in u.value) or all(value == 0 for value in v.value):
        raise ValueError("vector arguments are zero")
    return u.dot(v) / (u.norm() * v.norm())



def main():
    '''Test case for exercise 05'''
    print("Results for exercise 05")
    try:
        u:Vector[float] = Vector([1., 0.])
        v:Vector[float] = Vector([1., 0.])
        a:Vector[float] = Vector([1., 0.])
        b:Vector[float] = Vector([0., 1.])
        c:Vector[float] = Vector([-1., 1.])
        d:Vector[float] = Vector([1., -1.])
        i:Vector[float] = Vector([2., 1.])
        j:Vector[float] = Vector([4., 2.])
        g:Vector[float] = Vector([1., 2., 3.])
        h:Vector[float] = Vector([4., 5., 6.])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print(angle_cos(u, v))
        print(angle_cos(a, b))
        print(angle_cos(c, d))
        print(angle_cos(i, j))
        print(angle_cos(g, h))
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
