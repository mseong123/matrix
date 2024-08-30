'''ex11 - determinant for matrix and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 11'''
    print("Results for exercise 11")
    try:
        # pdf test
        u:Matrix[float] = Matrix([[1., -1.], [-1., 1.]])
        v:Matrix[float] = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]])
        w:Matrix[float] = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.],])
        x:Matrix[float] = Matrix([[ 8., 5., -2., 4.],[ 4., 2.5, 20., 4.],[ 8., 5., 1., 4.],[28., -4., 17., 1.]])
        # evalsheet pdf
        a:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        b:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        c:Matrix[float] = Matrix([[2., 0.], [0., 2.]])
        d:Matrix[float] = Matrix([[1., 1.], [1., 1.]])
        e:Matrix[float] = Matrix([[0., 1.], [1., 0.]])
        f:Matrix[float] = Matrix([[1., 2.], [3., 4.]])
        g:Matrix[float] = Matrix([[-7., 5.], [4., 6.]])
        h:Matrix[float] = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print("")
        L, U, det = u.determinant()
        print(det)
        print("")
        L, U, det = v.determinant()
        print(det)
        print("")
        L, U, det = w.determinant()
        print(det)
        print("")
        L, U, det = x.determinant()
        print(det)
        print("")
        print("eval test")
        print("")
        L, U, det = a.determinant()
        print(det)
        print("")
        L, U, det = b.determinant()
        print(det)
        print("")
        L, U, det = c.determinant()
        print(det)
        print("")
        L, U, det = d.determinant()
        print(det)
        print("")
        L, U, det = e.determinant()
        print(det)
        print("")
        L, U, det = f.determinant()
        print(det)
        print("")
        L, U, det = g.determinant()
        print(det)
        print("")
        L, U, det = h.determinant()
        print(det)
        print("")

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
