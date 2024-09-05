'''ex07 - linear map/matrix multiplication and main function to run test'''

from typing import TypeVar
from vector import Vector
from matrix import Matrix

K = TypeVar("K", int, float)

def main():
    '''Test case for exercise 07'''
    print("Results for exercise 07")
    try:
        # pdf test
        u:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        v:Vector[float] = Vector([4., 2.])
        a:Matrix[float] = Matrix([[2., 0.],[0., 2.]])
        b:Vector[float] = Vector([4., 2.])
        c:Matrix[float] = Matrix([[2., -2.], [-2., 2.]])
        d:Vector[float] = Vector([4., 2.])
        m:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        n:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        i:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        j:Matrix[float] = Matrix([[2., 1.], [4., 2.]])
        g:Matrix[float] = Matrix([[3., -5.], [6., 8.]])
        h:Matrix[float] = Matrix([[2., 1.], [4., 2.]]) 
        # eval test
        a_eval:Matrix[float] = Matrix([[0., 0.], [0., 0.]])
        b_eval:Vector[float] = Vector([4., 2.])
        c_eval:Matrix[float] = Matrix([[1., 0.], [0., 1.]])
        d_eval:Vector[float] = Vector([4., 2.])
        e_eval:Matrix[float] = Matrix([[1., 1.], [1., 1.]])
        f_eval:Vector[float] = Vector([4., 2.])
        g_eval:Matrix[float] = Matrix([[2., 0.], [0., 2.]])
        h_eval:Vector[float] = Vector([2., 1.])
        i_eval:Matrix[float] = Matrix([[0.5, 0.], [0., 0.5]])
        j_eval:Vector[float] = Vector([4., 2.])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        u.mul_vec(v).print_vector()
        print("")
        a.mul_vec(b).print_vector()
        print("")
        c.mul_vec(d).print_vector()
        print("")
        m.mul_mat(n).print_matrix()
        print("")
        i.mul_mat(j).print_matrix()
        print("")
        g.mul_mat(h).print_matrix()
        print("")
        print("eval test")
        a_eval.mul_vec(b_eval).print_vector()
        print("")
        c_eval.mul_vec(d_eval).print_vector()
        print("")
        e_eval.mul_vec(f_eval).print_vector()
        print("")
        g_eval.mul_vec(h_eval).print_vector()
        print("")
        i_eval.mul_vec(j_eval).print_vector()

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
