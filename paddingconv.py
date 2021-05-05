
import numpy as np #se importa la libreria numpy

def conv_helper(original, kernel):
    
    o_row, o_col = original.shape #se crea la matriz original y se redimensiona el arrey
    result = 0
    #se crea un ciclo for para irnos moviendo por la matriz
    for row in range(o_row): #se va moviendo por las fila
        for col in range(o_col): #se va moviendo por las columnas
            result += original[row,col] *  kernel[row,col]
            #se hace un producto punto entre la matriz original y el filtro (kernel)
    return result


#caso prueba obtenido de "examples convolution.xlsx"
original = np.array ([[10,4,50,30,20],
                      [80,0,0,0,6],
                      [0,0,1,16,17],
                      [0,1,0,7,23],
                      [1,0,6,0,4]]) #datos de la matriz original 

kernel = np.array ([[1,0,1],
                    [0,0,0],
                    [1,0,3]]) #datos del filter (kernel)

original_row, original_col = original.shape #se redimesiona el arrey
kernel_row, kernel_col = kernel.shape #se redimensiona el arrey

#se crea una matriz "convolution" inicializada en 0 
convolution = np.zeros((convX,convY))

#se calcula la altura y la longitud
pad_height=int((kernel_row-1)/2)
path_width=int((kernel_-1)/2)

padded_image=np.zeros((original_row+(2+pad_height), original_col+(2*pad_width)))

padded_image[pad_height:padded_original.shape[]-padheight,pad_width:padded_image.shape[1]-pad_width]=image

#se crea un ciclo for para poder ir guardando los datos en la matriz convolution
for row in range(convX):
    for col in range(convY):
            convolution[row, col] = conv_helper(
                                original[row:row + kernel_row, 
                                col:col + kernel_col],kernel)


print(convolution)
