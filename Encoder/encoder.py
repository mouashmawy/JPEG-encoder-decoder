import numpy as np
from DCT_encoder import *
from Huffman_encoder import *



#describe your function
def divide_image(image):





    return #blocks 8x8



#describe your function
def DCT(block8x8):


    data = np.loadtxt(open("w6-img.csv", "rb"), delimiter=",", skiprows=0)
    image = np.array(data)
    dct_matrix = dct_matrix_generate(image)

    dct_matrix /=16
    dct_matrix[0,:] /=2
    dct_matrix[:,0] /=2


    dct_matrix = np.round(dct_matrix)

    print(dct_matrix)

    

    return #DCT block 8x8



#describe your function
def quantization(block):



    return #quantized block (8x8)



#describe your function
def linearing(block):



    return #array 1x64



#describe your function
def encoding_one_length(array):


    return #array 1xN



#describe your function
def Huffman_enconding(array):


    return #stream of 0s & 1s




