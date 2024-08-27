'''ex010 - row echelon for matrix and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 10'''
    print("Results for exercise 10")
    try:
        # own test
        u:Matrix[float] = Matrix([[0., 1,0,0],[1,0,0,1]])
        # v:Matrix[float] = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
        # w:Matrix[float] = Matrix([[-2., -8., 4., 5.],[1., -23., 4.,5.], [0., 6., 4.,5.]])
        # evalsheet pdf
        # a:Matrix[float] = Matrix([[0, 0], [0, 0]])
        # b:Matrix[float] = Matrix([[1, 0], [0, 1]])
        # c:Matrix[float] = Matrix([[1, 2], [3, 4]])
        # d:Matrix[float] = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        # f:Matrix[float] = Matrix([[1, 2], [3, 4], [5, 6]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    # try:
        print("own test")
    u.row_echelon()
        # print("")
        # v.transpose().print_matrix()
        # print("")
        # w.transpose().print_matrix()
        # print("")
        # print("eval test")
        # a.transpose().print_matrix()
        # print("")
        # b.transpose().print_matrix()
        # print("")
        # c.transpose().print_matrix()
        # print("")
        # d.transpose().print_matrix()
        # print("")
        # f.transpose().print_matrix()

    # except (TypeError, ValueError) as e:
    #     print(f"Error occured: {e}")
    #     return

if __name__ == "__main__":
    main()