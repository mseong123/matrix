# matrix | 42KL

This Specialization project aims to dive deep into the subject of Linear Algebra which powers most of the underlying algorithms in Machine Learning, Artificial Intelligence, Computer Graphics and other Computer Science subject matters. 
Topics and exercises included in the project:
1. Vector and Matrix operations (ie add, subtract, scale)
2. Linear combination
3. Linear interpolation
4. Dot Product
5. Norm
6. Cross Product
7. Trace
8. Matrix Multiplication
9. Matrix transpose
10. Row echelon form
11. Determinant of Matrix
12. Inverse of Matrix
13. Rank of Matrix

The objective of the project is to code the above operations without any help of libraries. The subject pdf is essential reading - over 60 pages long! - and introduces theoretical concepts to properties of Vector space and Linear Transformation (vector maps).
Also important is the 3Blue1Brown youtube video series - Essence of Linear Algebra. Both links as attached.

 - [`Subject PDF`](https://github.com/mseong123/matrix/blob/master/en.subject.pdf)
 - [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

Project is coded in Python and the exercise imposed time and space complexity limit on each operations. Project marks 100/100. 
## To run MANDATORY and BONUS
```
python train.py
python prediction.py
```
`python train.py` will train the regression model based on the dataset(data.csv). `python prediction` will then execute the program and prompt for an input (mileage) which will then output the predicted price of car based on the regression mode including a scatterplot showing the results and the precision of the model (R-square and Root Mean Square Deviation)

## To install jupyter lab
```
pip install jupyterlab
jupyter lab
```

In web interface, open notebook (ft_linear_regression.ipynb) and run the cells. The notebook will provide visualisation to the gradient descent algorithm in action in particular:
* Animation of the individual cost functions derivatives w.r.t each coefficient alongside the steps taken to reach the optimum solution.
* The number of steps taken for the associated learning rate.
* a 3D wireframe showing update of the GD for both coefficient at the same time. 
