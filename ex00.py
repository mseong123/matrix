'''Exercise 00 functions add, subtract and multiply and a main function to run test'''

from vector import Vector
from matrix import Matrix


def main():
    '''Test case for exercise 00'''
    print("Results for exercise 00")
    print("Vector")
    u:Vector[float] = Vector([2., 3.])
    v:Vector[float] = Vector([5., 7.])
    a:Vector[float] = Vector([2., 3.])
    b:Vector[float] = Vector([5., 7.])
    c:Vector[float] = Vector([2., 3.])
    try:
        u.add(v)
        a.sub(b)
    except TypeError as e:
        print(f"TypeError: {e}")
        return
    u.print_vector()
    print("")
    a.print_vector()
    print("")
    c.scl(2.0)
    c.print_vector()
    print("")
    print("Matrix")
    try:
        m:Matrix[float] = Matrix([
            [1.,2.],
            [3.,4.]
        ])
        n:Matrix[float] = Matrix([
            [7.,4.],
            [-2.,2.]
        ])
        o:Matrix[float] = Matrix([
            [1.,2.],
            [3.,4.]
        ])
        p:Matrix[float] = Matrix([
            [7., 4.],
            [-2., 2.]
        ])
        q:Matrix[float] = Matrix([
            [1.,2.],
            [3.,4.]
        ])
    except TypeError as e:
        print(f"TypeError {e}")
        return
    try:
        m.add(n)
        o.sub(p)
    except TypeError as e:
        print(f"TypeError {e}")
        return
    m.print_matrix()
    print("")
    o.print_matrix()
    print("")
    q.scl(2.)
    q.print_matrix()


if __name__ == "__main__":
    main()
