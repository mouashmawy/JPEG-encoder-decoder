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



# function to comute the inverse DCT 
def optimized_IDCT_matrix(dct_matrix):
    u = np.arange(8)
    x = u.reshape((8, 1))
    v = u.reshape((1, 8))
    y = v.reshape((8, 1))

    # Precompute cosine values
    cos_term_u_x = np.cos((2 * x + 1) * u * np.pi / (2 * 8))
    cos_term_v_y = np.cos((2 * y + 1) * v * np.pi / (2 * 8))

    # Compute IDCT using matrix operations
    idct_matrix = cos_term_u_x @ dct_matrix @ cos_term_v_y.T

    return idct_matrix



#describe your function

def collect_image(time_domain_blocks, rows, columns):
    # Create the full array
    number_of_columns=columns//8
    number_of_rows=rows//8

    full_array = np.zeros((rows, columns))

    # Generate a dictionary with the keys as tuple coordinates
    block_coordinates = {(row, col): None for row in range(number_of_rows) for col in range(number_of_columns)}

    for key, block in zip(block_coordinates.keys(),time_domain_blocks):
        row, col = key
        full_array[row*8:(row+1)*8, col*8:(col+1)*8]=block

    return full_array






