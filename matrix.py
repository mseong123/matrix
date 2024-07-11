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
            # any(not isinstance(element, type(sublist[0])) for sublist
            # in value for element in sublist):
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
        for i in range(self.size()[0]):
            print([self.value[j] for j in range(i, len(self.value), self.size()[0])])

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

    def mul_vec(self, vec:Vector[K]) -> Vector[K]:
        '''Matrix multiplication with vector'''
        column:int = self._shape[1] // self._shape[0]
        if vec.size() != column:
            raise ValueError("Argument vector size incorrect")
        # space complexity of 0(n),n = size of vector which is no. of row of linear map
        result:list[K] = []
        # time complexity of row of matrix (n) x column of matrix (m)
        # (j below with step row) due to column major storage format
        for i in range(self.size()[0]):
            temp_result:K = 0
            for j in range(i, self.size()[1], self.size()[0]):
                temp_result += self.value[j] * vec.value[j // self.size()[0]]
            result.append(temp_result)
        return Vector(result)

    def mul_mat(self, mat: 'Matrix[K]') -> 'Matrix[K]':
        '''Matrix multiplication with vector'''
        column:int = self._shape[1] // self._shape[0]
        if mat.size()[0] != column:
            raise ValueError("Argument matrix size incorrect")
        # space complexity m x p
        result:list[K] = []
        # time complexity m x p x n
        # column of mat (p)
        for i in range(mat.size()[1] // mat.size()[0]):
            # row of self (m)
            for j in range(self.size()[0]):
                temp_result:K = 0
                # column of self and row of mat (n)
                for k in range(j, self.size()[1], self.size()[0]):
                    temp_result += self.value[k] * \
                        mat.value[(k // self.size()[0])+ (i * mat.size()[0])]
                result.append(temp_result)
        self._shape = (self.size()[0], len(result))
        self._value = result
        return self

    def trace(self) -> K:
        '''return trace of matrix'''
        column:int = self.size()[1] // self.size()[0]
        if column != self.size()[0]:
            raise TypeError("Can't return trace of a non-square matrix")
        result:K = 0
        # time complexity of O(n) column
        for i in range(column):
            result += self.value[(i * self.size()[0]) + i]
        return result

    def transpose(self) -> 'Matrix[K]':
        '''returns transpose of matrix'''
        outer_list:list[list[K]] = []
        column:int = self.size()[1] // self.size()[0]
        # time complexity O(nm) and space complexity (assignment of values) 0(nm)
        for i in range(column):
            inner_list:list[K] = []
            for j in range(self.size()[0]):
                inner_list.append(self.value[(i * self.size()[0]) + j])
            outer_list.append(inner_list)
        return Matrix(outer_list)





def reshape_vector_to_matrix(v:list[Vector[K]]) -> Matrix[K]:
    '''reshape a vector(list of vector) into matrix'''
    if not isinstance(v, list) or len(v) == 0 or \
        any(not isinstance(vector, Vector) for vector in v) \
        or any(vector.size() != v[0].size() for vector in v):
        raise ValueError("Vector argument incorrect")
    return Matrix([[v[j].value[i] for j,_ in enumerate(v)] for i in range(v[0].size())])
