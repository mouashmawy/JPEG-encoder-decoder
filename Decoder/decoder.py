#from huffman_decoder import *
import numpy as np

#describe your function
def Huffman_deconding(array):


    return #array 1xN





# function to implement the inverse length coding algorthem 
# input: encoded array of 1 X N  dimuntion 
# output: decoded array of 1X 64  dimuntion 
def length_coding_decoding(encoded_array):
    decoded_array = []
    flag = 0  # Indicates a zero encountered in encoded_array

    for index in range(len(encoded_array)):
        if encoded_array[index] == 0:
            flag = 1
        else:
            if flag == 1:
                # Append zeros as per the count in encoded_array
                decoded_array.extend([0] * encoded_array[index])
                flag = 0
            else:
                # Append non-zero values directly
                decoded_array.append(encoded_array[index])

    return decoded_array



def expened_matrix_dimantion(input_array):
    n = 8
    output = np.zeros((8,8))
    index = 0
    # There are 15 diagonal lines in a zigzag pattern over an 8x8 matrix
    for i in range(15):
        # For the first 8 diagonals (i < 8), the starting point is the first column
        if i < n:
            start, end, step = 0, i + 1, 1
        # For the remaining 7 diagonals, the starting point shifts downwards
        else:
            start, end, step = i - n + 1, n, 1

        # Move through the current diagonal line
        for j in range(start, end, step):
            # Calculate the x and y coordinates in the matrix
            # If i is even, the direction is top-left to bottom-right
            # If i is odd, the direction is bottom-right to top-left
            y, x = (j, i - j) if i % 2 == 0 else (i - j, j)
            output[x][y] = input_array[index]
            # Move to the next element in the input array
            index += 1

    # Return the expanded matrix
    return output





#describe your function
def dequantization(block):



    return #dequantized block (8x8)



# this function  calculate all 8x8 DCT basis matrices using np vectorized operations.
# Output: Dictionary with keys  from '0,0' to '7,7', each mapping to its corresponding 8x8 DCT basis matrix. 
# for example dct_bases['0,0'] will return the first base
def DCT_bases_optimized():
    # Create meshgrids for u, v, x, and y
    u, v, x, y = np.meshgrid(range(8), range(8), range(8), range(8), indexing='ij')

    # Compute the DCT bases
    dct_bases = np.cos(((2 * x + 1) * u * np.pi) / 16) * np.cos(((2 * y + 1) * v * np.pi) / 16)

    # Reshape to separate each 8x8 DCT base
    dct_bases = dct_bases.reshape(8, 8, 8, 8)

    return dct_bases

def inverse_dct(dct_coefficients):

    dct_bases = DCT_bases_optimized()
    
    # Initialize the matrix for the result of the IDCT
    idct_matrix = np.zeros((8, 8))
    
    # Loop through each pixel in the spatial domain
    for x in range(8):
        for y in range(8):
            sum = 0
            # Accumulate the sum of the product of DCT coefficients and basis functions
            for u in range(8):
                for v in range(8):
                    sum += dct_coefficients[u, v] * dct_bases[u, v, x, y]
            idct_matrix[x, y] = sum

    return np.round(idct_matrix)



#describe your function
def collect_image(time_domain_blocks):
    # Determine the size of the full array
    columns = (max(int(key.split(',')[1]) for key in time_domain_blocks.keys()) + 1)*8
    rows=(max(int(key.split(',')[0]) for key in time_domain_blocks.keys()) + 1)*8
    # Create the full array
    full_array = np.zeros((rows,columns))


    # Fill in the full array
    for key, block in time_domain_blocks.items():
        row, col = map(int, key.split(','))
        full_array[row*8:(row+1)*8, col*8:(col+1)*8] = block
    return full_array






