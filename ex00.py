'''Exercise 00 functions add, subtract and multiply and a main function to run test'''

from vector import Vector
from matrix import Matrix
from generics import T


def main():
    '''Test case for exercise 00'''
    u:Vector[float] = Vector([2,3])
    v:Vector[float] = Vector([5,7])
    a:Matrix[int] = Matrix([[1,2,3],[4,5,6]])
    print(a.size())

if __name__ == "__main__":
    main()
