import numpy as np
 
arr = np.array([10, 20, 30])
print(arr.dtype)
 
arr_float = np.array([10, 20, 30], dtype='float64')
print(arr_float.dtype)
 
student_dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('marks', 'f4')])
 
students = np.array([
    ('Arush', 21, 14.4),
    ('Aryan', 34, 45)    
], dtype=student_dtype)
 
print(students)
print(students['name'])
print(students['marks'])
 
arr = np.empty((2, 3))
print(arr)
 
zero_arr = np.zeros((3, 2))
ones_arr = np.ones((2, 3), dtype=int)
print(zero_arr)
print(ones_arr)
 
list = [1, 2, 3]
arr = np.asarray(list)
print(arr)
 
arr = np.arange(0, 10, 2)
print(arr)
 