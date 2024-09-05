'''Exercise 00 functions add, subtract and multiply and a main function to run test'''

from vector import Vector
from matrix import Matrix

def main():
    '''Test case for exercise 00'''
    print("Results for exercise 00")
    try:
        # pdf test
        pdf_u:Vector[float] = Vector([2., 3.])
        pdf_v:Vector[float] = Vector([5., 7.])
        pdf_a:Vector[float] = Vector([2., 3.])
        pdf_b:Vector[float] = Vector([5., 7.])
        pdf_c:Vector[float] = Vector([2., 3.])
        pdf_m:Matrix[float] = Matrix([
                [1.,2.],
                [3.,4.]
            ])
        pdf_n:Matrix[float] = Matrix([
            [7.,4.],
            [-2.,2.]
        ])
        pdf_o:Matrix[float] = Matrix([
            [1.,2.],
            [3.,4.]
        ])
        pdf_p:Matrix[float] = Matrix([
            [7.,4.],
            [-2.,2.]
        ])
        pdf_q:Matrix[float] = Matrix([
            [1.,2.],
            [3.,4.]
        ])
        # evalsheet pdf (addition)
        eval_a_add:Vector[float] = Vector([0., 0.])
        eval_b_add:Vector[float] = Vector([0., 0.])
        eval_c_add:Vector[float] = Vector([1., 0.])
        eval_d_add:Vector[float] = Vector([0., 1.])
        eval_e_add:Vector[float] = Vector([1., 1.])
        eval_f_add:Vector[float] = Vector([1., 1.])
        eval_g_add:Vector[float] = Vector([21., 21.])
        eval_h_add:Vector[float] = Vector([21., 21.])
        eval_i_add:Vector[float] = Vector([-21., 21.])
        eval_j_add:Vector[float] = Vector([21., -21.])
        eval_k_add:Vector[float] = Vector([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
        eval_l_add:Vector[float] = Vector([9., 8., 7., 6., 5., 4., 3., 2., 1., 0.])
        eval_m_add:Matrix[float] = Matrix([
            [0.,0.],
            [0.,0.]
        ])
        eval_n_add:Matrix[float] = Matrix([
            [0.,0.],
            [0.,0.]
        ])
        eval_o_add:Matrix[float] = Matrix([
            [1.,0.],
            [0.,1.]
        ])
        eval_p_add:Matrix[float] = Matrix([
            [0.,0.],
            [0.,0.]
        ])
        eval_q_add:Matrix[float] = Matrix([
            [1.,1.],
            [1.,1.]
        ])
        eval_r_add:Matrix[float] = Matrix([
            [1.,1.],
            [1.,1.]
        ])
        eval_s_add:Matrix[float] = Matrix([
            [21.,21.],
            [21.,21.]
        ])
        eval_t_add:Matrix[float] = Matrix([
            [21.,21.],
            [21.,21.]
        ])
        # evalsheet pdf (deduction)
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print("Vector operations")
        pdf_u.add(pdf_v)
        pdf_a.sub(pdf_b)
        pdf_u.print_vector()
        print("")
        pdf_a.print_vector()
        print("")
        pdf_c.scl(2.0)
        pdf_c.print_vector()
        print("")
        print("Matrix operations")
        pdf_m.add(pdf_n)
        pdf_o.sub(pdf_p)
        pdf_m.print_matrix()
        print("")
        pdf_o.print_matrix()
        print("")
        pdf_q.scl(2.)
        pdf_q.print_matrix()
        print("")
        print("eval test")
        print("Vector operations (additions)")
        eval_a_add.add(eval_b_add)
        eval_a_add.print_vector()
        print("")
        eval_c_add.add(eval_d_add)
        eval_c_add.print_vector()
        print("")
        eval_e_add.add(eval_f_add)
        eval_e_add.print_vector()
        print("")
        eval_g_add.add(eval_h_add)
        eval_g_add.print_vector()
        print("")
        eval_i_add.add(eval_j_add)
        eval_i_add.print_vector()
        print("")
        eval_k_add.add(eval_l_add)
        eval_k_add.print_vector()
        print("")
        print("Matrix operations (additions)")
        eval_m_add.add(eval_n_add)
        eval_m_add.print_matrix()
        print("")
        eval_o_add.add(eval_p_add)
        eval_o_add.print_matrix()
        print("")
        eval_q_add.add(eval_r_add)
        eval_q_add.print_matrix()
        print("")
        eval_s_add.add(eval_t_add)
        eval_s_add.print_matrix()
        print("")
        print("Vector operations (deductions)")
        

    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return


if __name__ == "__main__":
    main()
