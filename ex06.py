'''ex06 - cross product and main function to run test'''

from typing import TypeVar
from vector import Vector

K = TypeVar("K", int, float)

def cross_product(u:Vector[K], v:Vector[K]) -> Vector[K]:
    """return cross product of 2 3D vectors"""
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise TypeError("argument is not of Vector type")
    # error handling for generic type done in dot method in vector class
    if u.size() != 3 or v.size() != 3:
        raise ValueError("vector arguments size are not of 3 dimensions")
    result:list[K] = []
    # Time complexity O(n) space complexity of O(n)
    for i in range(3):
        if i == 0:
            result.append((u.value[1] * v.value[2]) - (u.value[2] * v.value[1]))
        elif i == 1:
            result.append((u.value[2] * v.value[0]) - (u.value[0] * v.value[2]))
        else:
            result.append((u.value[0] * v.value[1]) - (u.value[1] * v.value[0]))
    return Vector(result)

def main():
    '''Test case for exercise 06'''
    print("Results for exercise 06")
    try:
        # pdf test
        u:Vector[float] = Vector([0., 0., 1.])
        v:Vector[float] = Vector([1., 0., 0.])
        a:Vector[float] = Vector([1., 2., 3.])
        b:Vector[float] = Vector([4., 5., 6.])
        c:Vector[float] = Vector([4., 2., -3.])
        d:Vector[float] = Vector([-2., -5., 16.])
        i:Vector[float] = Vector([2., 1.])
        j:Vector[float] = Vector([4., 2.])
        g:Vector[float] = Vector([1., 2., 3.])
        h:Vector[float] = Vector([4., 5., 6.])
        # eval test
        k:Vector[float] = Vector([0., 0., 0.])
        l:Vector[float] = Vector([0., 0., 0.])
        m:Vector[float] = Vector([1., 0., 0.])
        n:Vector[float] = Vector([0., 0., 0.])
        o:Vector[float] = Vector([1., 0., 0.])
        p:Vector[float] = Vector([0., 1., 0.])
        q:Vector[float] = Vector([8., 7., -4.])
        r:Vector[float] = Vector([3., 2., 1.])
        s:Vector[float] = Vector([1., 1., 1.])
        t:Vector[float] = Vector([0., 0., 0.])
        w:Vector[float] = Vector([1., 1., 1.])
        x:Vector[float] = Vector([1., 1., 1.])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        cross_product(u, v).print_vector()
        print("")
        cross_product(a, b).print_vector()
        print("")
        cross_product(c, d).print_vector()
        print("eval test")
        cross_product(k, l).print_vector()
        print("")
        cross_product(m, n).print_vector()
        print("")
        cross_product(o, p).print_vector()
        print("")
        cross_product(q, r).print_vector()
        print("")
        cross_product(s, t).print_vector()
        print("")
        cross_product(w, x).print_vector()

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
