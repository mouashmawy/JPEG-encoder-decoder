import numpy as np
import pandas as pd

def dct_eqn(x,y,u,v):
    first_term = np.cos((2*x+1)*u*np.pi/16)
    second_term = np.cos((2*y+1)*v*np.pi/16)
    return first_term*second_term



def dct_generate(u,v):
    dct_base = np.zeros((8, 8))
    for x in range(8):
        for y in range(8):
            dct_base[x,y] = dct_eqn(x,y,u,v)
    return dct_base

def dct_generate2(u,v):
    dct_matrix = np.fromfunction(lambda i, j: dct_eqn(i, j,u,v), (8, 8))
    return dct_matrix



def dct_matrix_generate(image):

    #dct matrix
    dct_matrix = np.zeros((8, 8))
    for u in range(8):
        for v in range(8):
            dct_matrix[u,v] = np.sum(image*dct_generate(u,v))
    return dct_matrix

