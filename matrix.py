'''
matrix class definition and methods
'''
from typing import Generic, TypeVar, cast
from vector import Vector

K = TypeVar("K", float, int)

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

    @value.setter
    def value(self, new_value):
        '''setter for self._value'''
        self._value = new_value

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

    def row_echelon(self) -> 'Matrix[K]':
        '''return matrix converted to reduced row echelon form'''
        # check for any null row and move to bottom of matrix
        column:int = self.size()[1] // self.size()[0]
        # def replace_row(temp, j):
        #     for i in range(column):
        #         self.value[i * self.size()[0] + j] = self.value[i * self.size()[0] + j +1]
        #         self.value[i * self.size()[0] + j + 1] = temp[i]
        def normalize_row(row):
            normalized:list[K] = []
            column:K | None = None
            for j in range(row, self.size()[1], self.size()[0]):
                denom:K = self.value[j]
                if denom == 0:
                    normalized.append(denom)
                    continue
                # time complexity row m
                for k in range(j, self.size()[1], self.size()[0]):
                    self.value[k] /= denom # type: ignore
                    if column is None:
                        column = len(normalized)
                    normalized.append(self.value[k])
                break
            return (column, normalized)
        # time complexity m x n
        def pivot(row, column, normalized):
            deduct:int = 0
            for j in range(0, self.size()[0]):
                # don't do anything if same row as normalized
                if row == j:
                    continue
                # if column value above pivot and below is zero, don't do anything
                elif self.value[column * self.size()[0] + j] == 0:
                    continue
                # else iterate through remaining columns in the row and deduct
                else:
                    count:int = column
                    deduct = self.value[column * self.size()[0] + j] * normalized[column]
                    for k in range(column * self.size()[0] + j, self.size()[1], self.size()[0]):
                        self.value[k] -= deduct * normalized[count]
                        count += 1

        # Below is for rearranging of rows before RREF calculation:
        # 1) Pivot of rows below should always to be right of pivot of row above it
        # 2) Null elements row should always be at the bottom of matrix
        # My algo iterates through every column (outer loop) and every row(inner loop)
        # and checks for condition (1) Just doing this will preprocess properly any
        # matrix before RREF calculation (tested) although row arrangement
        # end result might differ in diff examples but still works. Commented out because
        # exercise doesn't need matrix preprocessing.

        # for i in range(column):
        #     temp:list[K] = []
        #     for j in range(self.size()[0] - 1):
        #         if self.value[i * self.size()[0] + j] == 0 and \
        #                 self.value[i * self.size()[0] + j + 1] != 0:
        #             if i == 0 or (i > 0 and all(self.value[k * self.size()[0] + j] \
        #                 == 0 for k in range(i) )):
        #                 temp = [self.value[m] for m in range(j, self.size()[1], self.size()[0])]
        #                 replace_row(temp,j)

        # reduced Row Echelon Form calculation
        for row in range(self.size()[0]):
            # normalize row
            # time complexity m (row) x n (column)
            column, normalized = normalize_row(row)
            # if column is None, means null element hence no pivot in the current row.
            if column is not None:
                # set values below and above pivot to zero
                # time complexity is m (row) x ( m(row) x n(column) => going through
                # matrix row again and check and if pivot above and below is not zero,
                # process and adjusting the columns)
                pivot(row, column, normalized)
        # total time complexity = normalized (m x n) = (n) ^ 2 + pivot m x n = (n) ^ 2 hence 2n^2 = n^2 
        # which is lower than (m x n) ^ 3 required by eval. Space are all constant
        return self

    def determinant(self) -> K:
        """return determinant of matrix (scalar value)"""
        # check if non square matrix
        column:int = self.size()[1] // self.size()[0]
        row_swap:int = 1

        if column != self.size()[0]:
            raise TypeError("Can't return determinant of a non-square matrix")
        # I use LU decomposition which is efficient and more stable for larger matrices. 

        # function to swap row with pivot which is zero to last row for both Upper Triangular Matrix. 
        # constant hence not included in time complexity
        def swap_row(last, j):
            nonlocal row_swap
            for i in range(column):
                self.value[i * self.size()[0] + self.size()[0] -1] = self.value[i * self.size()[0] + j]
                self.value[i * self.size()[0] + j] = last[i]
            row_swap *= -1
        
        # row operations below pivot to get upper triangular Matrix. time complexity n x n x n (n^3).
        for i in range(column):
            for j in range(self.size()[0]):
                if j == i and self.value[i * self.size()[0] + j] != 0:
                    placeholder_row:int = j
                elif j == i and self.value[i * self.size()[0] + j] == 0:
                    last_swap:list[K] = [self.value[k] for k in range(self.size()[0] - 1, self.size()[1], self.size()[0])]
                    swap_row(last_swap, j)
                    break
                if j > i and self.value[i * self.size()[0] + j] != 0: 
                    deduct:K = self.value[i * self.size()[0] + j] / self.value[i * self.size()[0] + placeholder_row] # type: ignore
                    column_placeholder: int = 0
                    for k in range(j, self.size()[1], self.size()[0]): 
                        self.value[k] -= deduct * self.value[column_placeholder * self.size()[0] + placeholder_row]
                        column_placeholder += 1

        result:K | None = None
        # time complexity n x n (n^2), multiply diagonal rows in Upper Matrix
        for i in range(column):
            for j in range(self.size()[0]):
                if i == j:
                    if result is None:
                        result = self.value[i * self.size()[0] + j]
                    else:
                        result *= self.value[i * self.size()[0] + j]
        # Total space complexity = constant
        # Total time complexity = n^3 + n^2 hence total n^3
        if result == 0:
            return result
        else:
            return row_swap * cast(K,result)

    def inverse(self) -> "Matrix[K]":
        """return an inverse matrix. Use Gauss-Jordan elimination method"""
        
        # Check whether matrix is square and if determinant is zero throw error
        # create a copy to store original matrix value before passing to inverse function
        # space complexity = m x n
        copy:list[K] = self.value.copy()
        if self.determinant() == 0:
            raise TypeError("Determinant is zero. No inverse possible.")
        # Once check, assign value back
        self.value = copy
        # Use augmented matrix [A | I]. 
        column:int = self.size()[1] // self.size()[0]
        # create an identity matrix with same shape. 
        # Time complexity n^2. 
        # Space complexity n^2.
        identity:list[K] = []
        for i in range(column):
            for j in range(self.size()[0]):
                if i == j:
                    identity.append(1)
                else:
                    identity.append(0)
        # 1) Augmented matrix transformation for Lower triangular portion.
        # Iterate through n (outer loop) and n (inner loop). Then do row transformation
        # for every row n. n^3 time complexity. 
        def swap_row(last, last_swap_identity, j):
            for i in range(column):
                self.value[i * self.size()[0] + self.size()[0] -1] = self.value[i * self.size()[0] + j]
                self.value[i * self.size()[0] + j] = last[i]
                identity[i * self.size()[0] + self.size()[0] -1] = identity[i * self.size()[0] + j]
                identity[i * self.size()[0] + j] = last_swap_identity[i]
        for i in range(column):
            for j in range(self.size()[0]):
                deduct_lower:K | None = None
                if i == j and self.value[i * self.size()[0] + j] != 0:
                    pivot:int = j
                elif i == j and self.value[i * self.size()[0] + j] == 0:
                    last_swap:list[K] = [self.value[k] for k in range(self.size()[0] - 1, self.size()[1], self.size()[0])]
                    last_swap_identity:list[K] = [identity[k] for k in range(self.size()[0] - 1, self.size()[1], self.size()[0])]
                    swap_row(last_swap, last_swap_identity, j)
                    break
                if j != i and j > i and self.value[i * self.size()[0] + j] != 0:
                    if deduct_lower is None:
                        deduct_lower = self.value[i * self.size()[0] + j] / self.value[i * self.size()[0] + pivot] # type: ignore
                    column_placeholder: int = 0
                    # time complexity n (iterate through row j)
                    for k in range(j, self.size()[1], self.size()[0]):
                        if deduct_lower is not None:
                            self.value[k] -= deduct_lower * self.value[column_placeholder * self.size()[0] + pivot]
                            identity[k] -= deduct_lower * identity[column_placeholder * self.size()[0] + pivot]
                        column_placeholder += 1
                    
        # 2) Augmented matrix transformation for upper triangular portion.
        # Iterate through n (outer loop) and n (inner loop). Then do row transformation
        # for every row n. n^3 time complexity.
        
        for i in range(column -1, 0 -1, -1):
            for j in range(self.size()[0]-1, 0-1, -1):
                deduct_upper:K | None = None
                if i == j and self.value[i * self.size()[0] + j] != 0:
                    pivot_upper:int = j
                if j != i and j < i and self.value[i * self.size()[0] + j] != 0:
                    if deduct_upper is None:
                        deduct_upper = self.value[i * self.size()[0] + j] / self.value[i * self.size()[0] + pivot_upper] # type: ignore
                    column_placeholder_upper: int = column - 1
                    # time complexity n (iterate through row j)
                    for k in range((column -1) * self.size()[0] + j, 0 - 1, -self.size()[0]):
                        if deduct_upper is not None:
                            self.value[k] -= deduct_upper * self.value[column_placeholder_upper * self.size()[0] + pivot_upper] # type: ignore
                            identity[k] -= deduct_upper * identity[column_placeholder_upper * self.size()[0] + pivot_upper] # type: ignore
                        column_placeholder_upper -= 1
        # 3) Augmented matrix transformation for normalized pivot
        # Iterate through n (outer loop) and n (inner loop) to find pivot. Then do row transformation
        # for every row n. n^3 time complexity.
        for i in range(column):
            for j in range(self.size()[0]):
                deduct_normalized:K | None = None
                if i == j:
                    if deduct_normalized is None:
                        deduct_normalized = self.value[i * self.size()[0] + j]
                    column_placeholder_normalized: int = 0
                    for k in range(j, self.size()[1], self.size()[0]):
                        if deduct_normalized is not None:
                            self.value[k] /= deduct_normalized # type: ignore
                            identity[k] /= deduct_normalized # type: ignore
                        column_placeholder_normalized += 1

        # total space complexity is creating a n x n augmented identity matrix hence n^2
        # total time complexity is n x n (n^2) + (n x n x n) n^3 1) augment lower triangular matrix +
        # (n x n x n) n^3 1) augment upper triangular matrix + (n x n x n) n ^ 3 3) normalize pivot
        # total = n^2 + 3n^3, hence time complexity is n^3. 
        self.value = identity
        return self

    def rank(self) -> int:
        self.row_echelon()
        self.print_matrix()





def reshape_vector_to_matrix(v:list[Vector[K]]) -> "Matrix[K]":
    '''reshape a vector(list of vector) into matrix'''
    if not isinstance(v, list) or len(v) == 0 or \
        any(not isinstance(vector, Vector) for vector in v) \
        or any(vector.size() != v[0].size() for vector in v):
        raise ValueError("Vector argument incorrect")
    return Matrix([[v[j].value[i] for j,_ in enumerate(v)] for i in range(v[0].size())])
