'''ex08 - trace for matrix and main function to run test'''

from typing import TypeVar
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 08'''
    print("Results for exercise 08")
    try:
        # subject.pdf
        u:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        v:Matrix[float] = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
        w:Matrix[float] = Matrix([[-2., -8., 4.],[1., -23., 4.], [0., 6., 4.]])
        # evalsheet pdf
        a:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        f:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        b:Matrix[float] = Matrix([[1., 2.], [3., 4.]])
        c:Matrix[float] = Matrix([[8., -7.], [4., 2.]])
        d:Matrix[float] = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])


    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print(u.trace())
        print("")
        print(v.trace())
        print("")
        print(w.trace())
        print("")
        print("eval test")
        print(a.trace())
        print("")
        print(f.trace())
        print("")
        print(b.trace())
        print("")
        print(c.trace())
        print("")
        print(d.trace())

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
