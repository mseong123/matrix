'''Exercise 04 - norm and main function to run test'''

from vector import Vector

def main():
    '''Test case for exercise 04'''
    print("Results for exercise 04")
    try:
        # pdf test
        u:Vector[float] = Vector([0., 0., 0.])
        v:Vector[float] = Vector([1., 2., 3.])
        w:Vector[float] = Vector([-1., -2.])
        # eval test
        a:Vector[float] = Vector([0.])
        b:Vector[float] = Vector([1.])
        c:Vector[float] = Vector([0., 0.])
        d:Vector[float] = Vector([1., 0.])
        f:Vector[float] = Vector([2., 1.])
        g:Vector[float] = Vector([4., 2.])
        h:Vector[float] = Vector([-4., -2.])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print(u.norm_1(), u.norm(), u.norm_inf())
        print(v.norm_1(), v.norm(), v.norm_inf())
        print(w.norm_1(), w.norm(), w.norm_inf())
        print("")
        print("eval test")
        print(a.norm_1(), a.norm(), a.norm_inf())
        print(b.norm_1(), b.norm(), b.norm_inf())
        print(c.norm_1(), c.norm(), c.norm_inf())
        print(d.norm_1(), d.norm(), d.norm_inf())
        print(f.norm_1(), f.norm(), f.norm_inf())
        print(g.norm_1(), g.norm(), g.norm_inf())
        print(h.norm_1(), h.norm(), h.norm_inf())
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
