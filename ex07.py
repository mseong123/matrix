'''ex07 - linear map/matrix multiplication and main function to run test'''

from typing import TypeVar
from vector import Vector
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 07'''
    print("Results for exercise 07")
    try:
        u:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        v:Vector[float] = Vector([4., 2.])
        a:Matrix[float] = Matrix([[2., 0.],[0., 2.]])
        b:Vector[float] = Vector([4., 2.])
        c:Matrix[float] = Matrix([[2., -2.], [-2., 2.]])
        d:Vector[float] = Vector([4., 2.])
        i:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        j:Matrix[float] = Matrix([[2., 1.], [4., 2.]])
        g:Matrix[float] = Matrix([[3., -5.], [6., 8.]])
        h:Matrix[float] = Matrix([[2., 1.], [4., 2.]])
        k:Matrix[float] = Matrix([[2., -5.], [1., 8.],[3.,2.]])
        l:Matrix[float] = Matrix([[2., 1.,5.], [4., 2.,3.]])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        u.mul_vec(v).print_vector()
        print("")
        a.mul_vec(b).print_vector()
        print("")
        c.mul_vec(d).print_vector()
        print("")
        i.mul_mat(j).print_matrix()
        print("")
        g.mul_mat(h).print_matrix()
        print("")
        k.mul_mat(l).print_matrix()
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
