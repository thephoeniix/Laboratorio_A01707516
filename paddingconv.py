
import numpy as np 

def conv_helper(fragment, kernel):
    
    f_row, f_col = fragment.shape
    result = 0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result


original = np.array ([[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [0,0,1,16,17,18],
              [0,1,0,7,23,24],
              [1,7,6,5,4,3]])
  

kernel = np.array ([[1,1,1],
              [0,0,0],
              [2,10,3]]) 


original_row, original_col = original.shape 
kernel_row, kernel_col = kernel.shape

#se crea una matriz iicializada en ceros pero con las dimensiones de la matriz original
output = np.zeros(original.shape)

#se hacen calculos para obtener los tamaños de la altura y longitus de la matriz paddling
pad_height = int((kernel_row - 1) / 2)
pad_width = int((kernel_col - 1) / 2)

padded_original = np.zeros((original_row + (2 * pad_height), original_col + (2 * pad_width)))

padded_original[pad_height:padded_original.shape[0] - pad_height, pad_width:padded_original.shape[1] - pad_width] = original

#se van salvando en la nueva matriz los datos de paddling 
for row in range(original_row):
    for col in range(original_col):
            output[row, col] = conv_helper(
                                original[row:row + kernel_row, 
                                col:col + kernel_col],kernel)


print(output)