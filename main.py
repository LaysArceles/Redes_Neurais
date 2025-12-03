from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)
    filtered = image[:]

    for i in range(len(image)):                # percorre a linha imagem 
        for j in range(len(image[i])):         # percorre a coluna imagem
            nova = 0                           # ??
            novaKety = 0 
            for x in range(len(kernel)):       # percorre a linha do kernel
                for y in range(len(kernel[x])): # percorre a coluna do kernel
                    if i+x >= len(image) or j+y >= len(image[0]):  #
                        continue
                    nova += (image[i+x][j+y] * kernel[x][y])
                    novaKety += (kernel[x][y]) 
            if novaKety !=0:
                nova = nova/novaKety
           
            if nova > 255:
                nova = 255
            if nova < 0:
                nova = 0
            filtered[i][j] = nova

    return filtered

Kernel = Kernel("images.jfif", filter_function)


init()