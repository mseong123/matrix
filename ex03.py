'''Exercise 03 - dot product and main function to run test'''

from vector import Vector

def main():
    '''Test case for exercise 03'''
    print("Results for exercise 03")
    try:
        u:Vector[float] = Vector([0., 0.])
        v:Vector[float] = Vector([1., 1.])
        a:Vector[float] = Vector([1., 1.])
        b:Vector[float] = Vector([1., 1.])
        c:Vector[float] = Vector([-1., 6.])
        d:Vector[float] = Vector([3., 2.])
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return
    try:
        print(u.dot(v))
        print(a.dot(b))
        print(c.dot(d))
    except (TypeError, ValueError) as e:
        print(f"Error occured: {e}")
        return

if __name__ == "__main__":
    main()
