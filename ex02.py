'''linear interpolation and main function to run test'''

from typing import TypeVar, cast, Union, Type
from matrix import Matrix
from vector import Vector

V = TypeVar("V",bound=Vector | Matrix | int | float)

def lerp(u:V, v:V, t:float) -> V:
    '''linear interpolation'''
    return_value:V
    #checking arguments are of same type
    if not isinstance(u, type(v)):
        raise TypeError("first 2 argument are not of same type")
    #checking arguments are of same size and type if Vector or Matrix classes
    if isinstance(u, (Vector, Matrix)) and isinstance(v, (Vector, Matrix)):
        if u.size() != v.size():
            raise ValueError("arguments are not of same size")
        if not isinstance(u.value[0], type(v.value[0])):
            raise ValueError("arguments are not of same type")
    if isinstance(u, Vector) and isinstance(v, Vector):
        result:list = []
        #time complexity of vector size O(n)
        for i in range(u.size()):
            #space complexity of vector size O(n)
            result.append(cast(float, (u.value[i] * (1-t)) + (v.value[i] * t)))
        return_value=cast(V, Vector(result))
    return return_value

def main():
    '''main test function'''
    print("Results for exercise 02")
    try:
        v1:Vector[float] = Vector([2., 1.])
        v2:Vector[int] = Vector([4, 2])
    except (ValueError, TypeError) as e:
        print(f"error occured: {e}")
        return
    try:
        summary:Vector = lerp(v1,v2,0.3)
        summary.print_vector()
    except (ValueError, TypeError) as e:
        print(f"error occured: {e}")
        return
    print("")

if __name__ == "__main__":
    main()
