import numpy as np

two2d_array = np.array([[2,3,4],[8,9,3],[1,4,0]])
print(two2d_array)

def traverse2d_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse2d_array(two2d_array)            
        