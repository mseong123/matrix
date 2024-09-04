'''ex13 - matrix rank and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 13'''
    print("Results for exercise 13")
    try:
        # pdf test
        u:Matrix[float] = Matrix([[1., 0.,0.], [0., 1., 0.], [0.,0.,1.]])
        v:Matrix[float] = Matrix([[1., 2., 0., 0.], [2., 4., 0., 0.], [-1, 2. ,1.,1.]])
        w:Matrix[float] = Matrix([[8., 5., -2],[4., 7., 20.],[7., 6., 1.], [21., 18., 7.]])
        # evalsheet pdf
        a:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        b:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        c:Matrix[float] = Matrix([[2, 0.], [0., 2]])
        d:Matrix[float] = Matrix([[1., 1.], [1., 1.]])
        f:Matrix[float] = Matrix([[0., 1.], [1., 0.]])
        g:Matrix[float] = Matrix([[1., 2.], [3., 4.]])
        h:Matrix[float] = Matrix([[-7., 5.], [4., 6.]])
        i:Matrix[float] = Matrix([[1, 0.,0.], [0., 1., 0.], [0.,0.,1.]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print("")
        u.rank()
        print("")
        v.rank()
        print("")
        w.rank()
        print("")
        print("eval test")
        print("")
        a.rank()
        print("")
        b.rank()
        print("")
        c.rank()
        print("")
        d.rank()
        print("")
        f.rank()
        print("")
        g.rank()
        print("")
        h.rank()
        print("")
        i.rank()
        print("")

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()