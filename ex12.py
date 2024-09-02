'''ex12 - inverse for matrix and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 12'''
    print("Results for exercise 12")
    try:
        # pdf test
        u:Matrix[float] = Matrix([[2., -1.,3.], [-1., 1., 3.], [4.,3.,5.]])
        # v:Matrix[float] = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]])
        # w:Matrix[float] = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.],])
        # x:Matrix[float] = Matrix([[ 8., 5., -2., 4.],[ 4., 2.5, 20., 4.],[ 8., 5., 1., 4.],[28., -4., 17., 1.]])
        # evalsheet pdf
        # a:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        # b:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        # c:Matrix[float] = Matrix([[2., 0.], [0., 2.]])
        # d:Matrix[float] = Matrix([[1., 1.], [1., 1.]])
        # f:Matrix[float] = Matrix([[0., 1.], [1., 0.]])
        # g:Matrix[float] = Matrix([[1., 2.], [3., 4.]])
        # h:Matrix[float] = Matrix([[-7., 5.], [4., 6.]])
        # i:Matrix[float] = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print("")
        u.inverse()
        print("")
        # print(v.determinant())
        # print("")
        # print(w.determinant())
        # print("")
        # print(x.determinant())
        # print("")
        # print("eval test")
        # print("")
        # print(a.determinant())
        # print("")
        # print(b.determinant())
        # print("")
        # print(c.determinant())
        # print("")
        # print(d.determinant())
        # print("")
        # print(f.determinant())
        # print("")
        # print(g.determinant())
        # print("")
        # print(h.determinant())
        # print("")
        # print(i.determinant())
        # print("")

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()