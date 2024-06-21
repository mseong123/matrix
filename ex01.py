'''exercise 01 linear combination function and main function to run test'''

from typing import TypeVar
from vector import Vector
from matrix import Matrix

K = TypeVar("K", int, float)

def fma(a:K, b:K, c:K = 0):
    '''custom fma'''
    return (a * b) + c

def linear_combination(u: list[Vector[K]], coefs: list[K]) ->Vector[K]:
    '''linear combination'''
    if len(u) == 0 or len(coefs) == 0:
        raise ValueError("Argument List is empty")
    if len(u) != len(coefs):
        raise ValueError("length of argument list is different")
    if not all(vector.size() == u[0].size() for vector in u):
        raise ValueError("Vector size different in argument list")
    result:list[K] = []
    for i in range(u[0].size()):
        #Space complexity of 0(1) hence not counted
        accumulator:K = 0
        #time complexity of matrix ie a 2x2 matrix has 2x2 dimension hence O(n) is 4.
        for j, _ in enumerate(u):
            accumulator = fma(u[len(u) - j - 1].value[i], \
                                coefs[len(u) - j - 1], accumulator)
        #space complexity of dimension of result array hence if result vector size is 3, O(n) is 3
        result.append(accumulator)
    return Vector(result)

def main():
    '''main test function'''
    print("Results for exercise 01")
    try:
        e1:Vector[float] = Vector([1.,0.,0.])
        e2:Vector[float] = Vector([0.,1.,0.])
        e3:Vector[float] = Vector([0.,0.,1.])
        v1:Vector[float] = Vector([1., 2., 3.])
        v2:Vector[float] = Vector([0., 10., -100.])
    except (ValueError, TypeError) as e:
        print(f"error occured: {e}")
        return
    try:
        linear_combination([e1, e2, e3],[10.,-2., 0.5]).print_vector()
    except ValueError as e:
        print(f"Value Error: {e}")
        return
    except TypeError as e:
        print(f"Type Error: {e}")
        return
    print("")
    try:
        linear_combination([v1, v2],[10.,-2.]).print_vector()
    except ValueError as e:
        print(f"Value Error: {e}")
        return
    except TypeError as e:
        print(f"Type Error: {e}")
        return
    print("")

if __name__ == "__main__":
    main()
