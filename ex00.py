'''Exercise 00 functions add, subtract and multiply and a main function to run test'''

from vector import Vector
from matrix import Matrix


def main():
    '''Test case for exercise 00'''
    print("Results for exercise 00")
    u:Vector[float] = Vector([2., 3.])
    v:Vector[float] = Vector([5., 7.])
    u.add(v)
    u.print_vector()
    print("")
    a:Vector[float] = Vector([2., 3.])
    b:Vector[float] = Vector([5., 7.])
    a.sub(b)
    a.print_vector()
    print("")
    c:Vector[float] = Vector([2., 3.])
    c.scl(2.0)
    c.print_vector()
    print("")
    m:Matrix[float] = Matrix([
        [1.,2.],
        [3.,4.]
    ])
    n:Matrix[float] = Matrix([
        [7.,4.],
        [-2.,2.]
    ])
    m.add(n)
    m.print_matrix()
    print("")
    o:Matrix[float] = Matrix([
        [1.,2.],
        [3.,4.]
    ])
    p:Matrix[float] = Matrix([
        [7.,4.],
        [-2.,2.]
    ])
    o.sub(p)
    o.print_matrix()
    print("")
    q:Matrix[float] = Matrix([
        [1.,2.],
        [3.,4.]
    ])
    q.scl(2.)
    q.print_matrix()


if __name__ == "__main__":
    main()
