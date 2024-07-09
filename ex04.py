'''Exercise 04 - norm and main function to run test'''

from vector import Vector

def main():
    '''Test case for exercise 04'''
    print("Results for exercise 04")
    try:
        u:Vector[float] = Vector([0., 0., 0.])
        v:Vector[float] = Vector([1., 2., 3.])
        w:Vector[float] = Vector([-1., -2.])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
    try:
        print(u.norm_1(), u.norm(), u.norm_inf())
        print(v.norm_1(), v.norm(), v.norm_inf())
        print(w.norm_1(), w.norm(), w.norm_inf())
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
