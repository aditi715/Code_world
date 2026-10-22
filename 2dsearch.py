import numpy as np

twod_array = np.array([[1,3,2],[4,5,6],[9,8,7]])
print(twod_array)

def search2d_array(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return ' the value is lcated at index' + str(i) + ',' + str(j)
        
        return 'the element is not found in the array'
    
print(search2d_array(twod_array, 5))    