'''
matrix class definition and methods
'''
from typing import Generic
from generics import K

class Matrix(Generic[K]):
    '''Matrix class'''
    def __init__(self, value:list[list[K]]):
        #throw error if elements in matrix is not even
        self._check_matrix(value)
        self._record_shape(value)
        #insert argument into 1D array to ensure time complexity O(n) is met
        self._value:list[K] = [element for sublist in value for element in sublist]

    def _check_matrix(self, value:list[list[K]]):
        '''check if matrix is of correct size'''
        if len([element for sublist in value for element in sublist]) \
                % 2 != 0 and len(value) != 1:
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
            print([self._value[element] for element in \
                   range(i * column_size, (i + 1) * column_size)])

    def add(self, v:'Matrix[K]'):
        '''Add operation for matrix'''
        if self.size() == v.size():
            for i, _ in enumerate(self.value):
                self.value[i] += v.value[i]

    def sub(self, v:'Matrix[K]'):
        '''Deduct operation for matrix''' 
        if self.size() == v.size():
            for i, _ in enumerate(self.value):
                self.value[i] -= v.value[i]

    def scl(self, a:K):
        '''Scale operation for Matrix'''
        for i, _ in enumerate(self.value):
            self.value[i] *= a
