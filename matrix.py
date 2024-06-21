'''
matrix class definition and methods
'''
from typing import Generic, TypeVar
from vector import Vector

K = TypeVar("K", int, float)

class Matrix(Generic[K]):
    '''Matrix class'''
    def __init__(self, value:list[list[K]]):
        #throw error if elements in matrix is not even or have inappropriate shape
        self._check_matrix(value)
        self._record_shape(value)
        #insert argument into 1D column major array
        self._value:list[K] = [value[j][i] for i, _ in enumerate(value[0]) \
                               for j in range(len(value))]

    def _check_matrix(self, value:list[list[K]]):
        '''check argument values'''
        #check if input of matrix is of correct format(empty list, )
        if len(value) == 0 or any(not isinstance(sublist, list) for sublist in value) or \
            any(len(sublist) == 0 for sublist in value) or \
            any(len(sublist) != len(value[0]) for sublist in value): #or \
            # any(not isinstance(element, type(sublist[0])) for sublist in value for element in sublist):
            raise TypeError("Invalid Matrix Form")

    def _record_shape(self, value:list[list[K]]):
        '''record shape of matrix in form (row, total element)'''
        self._shape:tuple = tuple([len(value),\
                                   len([element for sublist in value for element in sublist])])

    @property
    def value(self) -> list[K]:
        '''getter for self._value'''
        return self._value

    def size(self) -> tuple[int, int]:
        '''Utility function. Returns size of matrix in form of tuple(row, element count)''' 
        return self._shape

    def print_matrix(self):
        '''Utility function. Print matrix values'''
        #calculate column size = total element/row. Use integer division //
        column_size = self.size()[1] // self.size()[0]
        for i in range(self.size()[0]):
            print([self.value[j] for j in range(i, len(self.value), column_size)])

    def add(self, v:'Matrix[K]'):
        '''Add operation for matrix'''
        #O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("matrix not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("matrix not of same type")
        for i, _ in enumerate(self.value):
            self.value[i] += v.value[i]

    def sub(self, v:'Matrix[K]'):
        '''Deduct operation for matrix''' 
        #O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("matrix not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("matrix not of same type")
        for i, _ in enumerate(self.value):
            self.value[i] -= v.value[i]

    def scl(self, a:K):
        '''Scale operation for Matrix'''
        #O(n) time complexity and O(1) space complexity
        for i, _ in enumerate(self.value):
            self.value[i] *= a

def reshape_vector_to_matrix(v:list[Vector[K]]) -> Matrix[K]:
    '''reshape a vector(list of vector) into matrix'''
    if not isinstance(v, list) or len(v) == 0 or \
        any(not isinstance(vector, Vector) for vector in v) \
        or any(vector.size() != v[0].size() for vector in v):
        raise ValueError("Vector argument incorrect")
    return Matrix([[v[j].value[i] for j,_ in enumerate(v)] for i in range(v[0].size())])
