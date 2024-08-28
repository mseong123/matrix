'''ex010 - row echelon for matrix and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 10'''
    print("Results for exercise 10")
    try:
        # pdf test
        u:Matrix[float] = Matrix([[1., 0., 0.], [0., 1., 0.],[0., 0., 1.]])
        v:Matrix[float] = Matrix([[1., 2.],[3., 4.]])
        w:Matrix[float] = Matrix([[1., 2.],[2., 4.]])
        x:Matrix[float] = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],\
                                  [8., 5., 1., 4., 17.]])
        # evalsheet pdf
        a:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        b:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        c:Matrix[float] = Matrix([[4., 2.], [2., 1.]])
        d:Matrix[float] = Matrix([[-7., 2.], [4., 8.]])
        f:Matrix[float] = Matrix([[1., 2.], [4., 8.]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("own test")
        print("")
        u.row_echelon().print_matrix()
        print("")
        v.row_echelon().print_matrix()
        print("")
        w.row_echelon().print_matrix()
        print("")
        x.row_echelon().print_matrix()
        print("")
        print("eval test")
        print("")
        a.row_echelon().print_matrix()
        print("")
        b.row_echelon().print_matrix()
        print("")
        c.row_echelon().print_matrix()
        print("")
        d.row_echelon().print_matrix()
        print("")
        f.row_echelon().print_matrix()
        print("")

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
