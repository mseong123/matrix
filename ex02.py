'''ex02 - linear interpolation and main function to run test'''

from typing import TypeVar, cast, Union, Type
from matrix import Matrix
from vector import Vector

V = TypeVar("V",bound=Vector | Matrix | int | float)

def lerp(u:V, v:V, t:float) -> V:
    '''linear interpolation'''
    return_value:V = u
    #checking arguments are of same type
    if not isinstance(u, type(v)):
        raise TypeError("first 2 argument are not of same type")
    #checking arguments are of same size and type if Vector or Matrix classes
    if isinstance(u, (Vector, Matrix)) and isinstance(v, (Vector, Matrix)):
        if u.size() != v.size():
            raise ValueError("arguments are not of same size")
        if not isinstance(u.value[0], type(v.value[0])):
            raise ValueError("arguments are not of same type")
    if isinstance(u, (Vector, Matrix)) and isinstance(v, (Vector, Matrix)):
        #time complexity of vector size O(n)
        for i, _ in enumerate(u.value):
            #constant space complexity, results stored in first input, O(1)
            u.value[i] = (u.value[i] * (1-t)) + ((v.value[i] * t)) 
    elif isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return_value = cast(V, (u * (1 - t)) + (v * t))
    return return_value

def main():
    '''main test function'''
    print("Results for exercise 02")
    try:
        print("Float interpolation")
        print(lerp(0., 1., 0.))
        print(lerp(0., 1., 1.))
        print(lerp(0., 1., 0.5))
        print(lerp(21., 42., 0.3))
        print("")
        print("Vector interpolation")
        lerp(Vector([2., 1.]), Vector([4.,2.]), 0.3).print_vector()
        print("")
        print("Matrix Interpolation")
        lerp(Matrix([[2., 1.],[3.,4.]]), Matrix([[20.,10.],[30.,40.]]), 0.5).print_matrix()

    except (ValueError, TypeError) as e:
        print(f"error occured: {e}")
        return
    print("")

if __name__ == "__main__":
    main()
