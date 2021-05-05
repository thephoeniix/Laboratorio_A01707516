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

#se hacen los calculos para poder obtener el número de filas y columas de la matriz convolution
convY=int(original_col-(kernel_col/2)*2+1) #columnas de la matriz convolution
convX=int(original_row-(kernel_row/2)*2+1) #filas de la matriz convolution

#se crea una matriz inicializada en 0 
convolution = np.zeros((convX,convY))

#se crea un ciclo for para poder ir guardando los datos en la matriz convolution
for row in range(convX):
    for col in range(convY):
            convolution[row, col] = conv_helper(
                                original[row:row + kernel_row, 
                                col:col + kernel_col],kernel)


print(convolution)
