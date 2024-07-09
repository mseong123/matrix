'''
vector class definition and methods
'''

from typing import Generic, TypeVar

K = TypeVar("K", int, float)

class Vector(Generic[K]):
    '''Vector class''' 
    def __init__(self, value:list[K]):
        '''store value in 2d array due to print format'''
        #error check if not empty argument
        if len(value) == 0:
            raise ValueError("Empty list in Vector initialisation")
        #error check if elements are of same type
        if any(not isinstance(element, type(value[0])) for element in value):
            raise ValueError("Elements in argument are not of same type")
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
        #O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("vector not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("vector not of same type")
        for i in range(self.size()):
            self._value[i] += v.value[i]

    def sub(self, v:'Vector[K]'):
        '''subtraction operation for vector'''
        #O(n) time complexity and O(1) space complexity
        if self.size() != v.size():
            raise TypeError("vector not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("vector not of same type")
        for i in range(self.size()):
            self._value[i] -= v.value[i]

    def scl(self, a:K):
        '''scale operation for vector'''
        #O(n) time complexity and O(1) space complexity
        for i in range(self.size()):
            self._value[i] *= a

    def dot(self, v:'Vector[K]') -> K:
        '''dot product'''
        if self.size() != v.size():
            raise TypeError("vector not of same size")
        if not isinstance(self.value[0], type(v.value[0])):
            raise TypeError("vector not of same type")
        result:K = 0
        #O(n) time complexity and O(1) space complexity
        for i in range(self.size()):
            result += self._value[i] * v.value[i]
        return result

    def norm_1(self) -> float:
        """norm 1(L1) taxicab Norm/Manhattan Norm. Preferred to L2 where sparsity and outliers 
        influence are important. Used in feature selection (LASSO regression) to encourage
        model sparsity LASSO tends to shrink coefficients of less important features to zero, 
        effectively performing feature selection. This is because the penalty encourages sparsity
        in the model.By reducing the number of features (coefficients), LASSO helps create 
        simpler and more interpretable models."""
        #O(n) time complexity and O(1) space complexity
        result:float = 0
        for i in self.value:
            result += -i if i < 0 else i
        return result

    def norm(self) -> float:
        """Euclidean Norm. Provides smoother solutions and penalises large coefficients 
        (Ridge regression). In ridge regression, we modify the least squares objective by 
        adding a penalty term proportional to the sum of the squares of the coefficients 
        to the loss function. Unlike LASSO regression, doesnt shrink
        coefficient to zero. Reduce impact of highly correlated predictors"""
        #O(n) time complexity and O(1) space complexity
        result:float = 0
        for i in self.value:
            result += pow(i, 2)
        return pow(result, 1/2)

    def norm_inf(self) -> float:
        """The norm_inf norm represents the maximum magnitude of any individual 
        component of the vector. It is useful in various contexts where you want 
        to measure the "size" of the vector based on its largest element."""
        #O(n) time complexity and O(1) space complexity
        result:float = [-value if value < 0 else value for value in self.value]
        return max(result)





    
