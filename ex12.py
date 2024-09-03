'''ex12 - inverse for matrix and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 12'''
    print("Results for exercise 12")
    try:
        # pdf test
        u:Matrix[float] = Matrix([[1, 0.,0.], [0., 1., 0.], [0.,0.,1.]])
        v:Matrix[float] = Matrix([[2, 0.,0.], [0., 2., 0.], [0.,0.,2.]])
        w:Matrix[float] = Matrix([[8., 5., -2],[4., 7., 20.],[7., 6., 1.]])
        # evalsheet pdf
        a:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        b:Matrix[float] = Matrix([[2., 0.], [0., 2.]])
        c:Matrix[float] = Matrix([[0.5, 0.], [0., 0.5]])
        d:Matrix[float] = Matrix([[0., 1.], [1., 0.]])
        f:Matrix[float] = Matrix([[1., 2.], [3., 4.]])
        g:Matrix[float] = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print("")
        u.inverse().print_matrix()
        print("")
        v.inverse().print_matrix()
        print("")
        w.inverse().print_matrix()
        print("")
        print("eval test")
        print("")
        a.inverse().print_matrix()
        print("")
        b.inverse().print_matrix()
        print("")
        c.inverse().print_matrix()
        print("")
        d.inverse().print_matrix()
        print("")
        f.inverse().print_matrix()
        print("")
        g.inverse().print_matrix()
        print("")

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()