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
        # a:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        # b:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        # c:Matrix[float] = Matrix([[4., 2.], [2., 1.]])
        # d:Matrix[float] = Matrix([[-7., 2.], [4., 8.]])
        # f:Matrix[float] = Matrix([[1., 2.], [4., 8.]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print("")
        # print(u.determinant())
        # print("")
        # print(v.determinant())
        # print("")
        # print(w.determinant())
        # print("")
        print(x.determinant())
        print("")
        # print("eval test")
        # print("")
        # a.row_echelon().print_matrix()
        # print("")
        # b.row_echelon().print_matrix()
        # print("")
        # c.row_echelon().print_matrix()
        # print("")
        # d.row_echelon().print_matrix()
        # print("")
        # f.row_echelon().print_matrix()
        # print("")

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
