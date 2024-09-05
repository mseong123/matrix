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
    # space complexity is O(n) number of dimension of vectors
    result:list[K] = []
    for i in range(u[0].size()): 
        accumulator:K = 0
        # n is list of coordinates of vector (m x n) where n is dimension and m is no. of vectors.
        # time complexity is no in list of vectors (m) x operation of linear combination with coefficients for each vector n
        # hence O(m x n)
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
        print("pdf test")
        linear_combination([e1, e2, e3],[10.,-2., 0.5]).print_vector()
        print("")
        linear_combination([v1, v2],[10.,-2.]).print_vector()
        print("")
        print("eval test")
        linear_combination([Vector([-42.,42.])],[-1.]).print_vector()
        print("")
        linear_combination([Vector([-42.]), Vector([-42.]), Vector([-42.])],[-1., 1., 0.]).print_vector()
        print("")
        linear_combination([Vector([-42.,42.]), Vector([1.,3.]), Vector([10.,20.])],[1., -10., -1.]).print_vector()
        print("")
        linear_combination([Vector([-42.,100., -69.5]), Vector([1.,3.,5.])],[1., -10.]).print_vector()

    except (ValueError, TypeError) as e:
        print(f"error occured: {e}")
        return

if __name__ == "__main__":
    main()
