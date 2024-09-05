'''Exercise 03 - dot product and main function to run test'''

from vector import Vector

def main():
    '''Test case for exercise 03'''
    print("Results for exercise 03")
    try:
        # pdf test
        u:Vector[float] = Vector([0., 0.])
        v:Vector[float] = Vector([1., 1.])
        a:Vector[float] = Vector([1., 1.])
        b:Vector[float] = Vector([1., 1.])
        c:Vector[float] = Vector([-1., 6.])
        d:Vector[float] = Vector([3., 2.])
        # eval test
        f:Vector[float] = Vector([0., 0.])
        g:Vector[float] = Vector([0., 0.])
        h:Vector[float] = Vector([1., 0.])
        i:Vector[float] = Vector([0., 0.])
        j:Vector[float] = Vector([1., 0.])
        k:Vector[float] = Vector([1., 0.])
        l:Vector[float] = Vector([1., 0.])
        m:Vector[float] = Vector([0., 1.])
        n:Vector[float] = Vector([1., 1.])
        o:Vector[float] = Vector([1., 1.])
        p:Vector[float] = Vector([4., 2.])
        q:Vector[float] = Vector([2., 1.])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print("pdf test")
        print(u.dot(v))
        print(a.dot(b))
        print(c.dot(d))
        print("")
        print("eval test")
        print(f.dot(g))
        print(h.dot(i))
        print(j.dot(k))
        print(l.dot(m))
        print(n.dot(o))
        print(p.dot(q))
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
