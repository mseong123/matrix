'''
vector class definition and methods
'''

from typing import Generic
import math
from generics import K


class Vector(Generic[K]):
    '''Vector class''' 
    def __init__(self, value:list[K]):
        '''store value in 2d array due to print format'''
        self._value:list[K] = []
        for i in value:
            self._value.append(i)

    @property
    def value(self) -> list[K]:
        '''class getter for _value'''
        return self._value

    def size(self) -> int:
        '''Utility function. Returns size of vector'''
        return len(self._value)

    def print_vector(self) -> None:
        '''Utility function. Print vector values'''
        for i in self._value:
            print([i])
    #exercise 00
    def add(self, v:'Vector[K]'):
        '''addition operation for vector
            Time complexity -
            the comparison operators not counted since they are constant and doesn't 
            depend on n input (which is size of vector. Also operations inside the loop 
            also considered constant following same logic. Hence time complexity is O(n) 
            which is the no of loop that depends on N
            Space complexity -
            Range is an iterator that is lazily generated hence doesn't need new data structures. 
            It has O(1). Also not dependant on N. 
            Same with addition operations which happens in place. Hence O(1)
        '''
        if self.size() == v.size():
            for i in range(self.size()):
                self._value[i] += v.value[i]

    def sub(self, v:'Vector[K]'):
        '''subtraction operation for vector'''
        if self.size() == v.size():
            for i in range(self.size()):
                self._value[i] -= v.value[i]

    def scl(self, a:K):
        '''scale operation for vector'''
        for i in range(self.size()):
            self._value[i] *= a
