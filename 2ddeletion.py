import numpy as np 
twod_array = np.array([[1,2,3], [9,7,6],[4,6,8]])
print(twod_array)
print('new array afer deletion')
new_array = np.delete(twod_array, 0 , axis = 0)
print(new_array)