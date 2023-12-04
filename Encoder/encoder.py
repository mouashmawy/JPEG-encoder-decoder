import numpy as np
import heapq
# from Huffman_encoder import get_Huffman_table, heap_tree, encode_huffman, decode_huffman



# Function to divide the image pixels into blocks of 8x8 shape. in two steps. first padding the 2D image to ensure its divided by 8 
# then iterate over the padded matrix to generate the blocks
# Input: Image pixels as a 2D array.
# Output: Array of 2D 8x8 blocks.

import numpy as np

def generating_image_blocks(image):
    # Initialize an empty list to store the 8x8 blocks
    blocks = {}

    # Determine the number of rows and columns in the original image
    number_of_rows, number_of_columns = image.shape

    # Calculate the amount of padding needed for rows and columns
    rows_to_add = number_of_rows % 8
    columns_to_add = number_of_columns % 8

    # Calculate padding for top and bottom
    padding_top = rows_to_add // 2
    padding_bottom = rows_to_add - padding_top

    # Calculate padding for left and right
    padding_left = columns_to_add // 2
    padding_right = columns_to_add - padding_left


    # Padding is added equally on opposite sides where possible
    padded_array = np.pad(image, 
                          ((padding_top, padding_bottom), 
                           (padding_left, padding_right)), 
                          'constant', constant_values=0)

    # Iterate over the padded image to extract 8x8 blocks
    rows, columns = padded_array.shape
    print(rows,columns)
    for row,row_index in zip(range(0, rows, 8),range(rows//8)):
        for column, column_index in zip(range(0, columns, 8), range(columns//8)):
            # Slice out an 8x8 block
            blocks[f'{row_index},{column_index}'] = padded_array[row:row+8, column:column+8]

    return blocks



# function to Converts an image pixel block to its frequency domain representation using DCT
# input: image_box the pixel in 8x8 dimension
# output:return the new image matrix after computing the dct convertion ( in the frequence domain )in 8x8 dimension
def DCT_matrix(image_box):
    # Initializing the matrix
    u = np.arange(8)
    x = u.reshape((8, 1))
    v = u.reshape((1, 8))
    y = v.reshape((8, 1))

    # Precompute cosine values
    cos_term_u_x = np.cos((2 * x + 1) * u * np.pi / (2 * 8))
    cos_term_v_y = np.cos((2 * y + 1) * v * np.pi / (2 * 8))

    # Compute IDCT using matrix operations
    dct_matrix = cos_term_u_x.T @ image_box @ cos_term_v_y

    # Normalizatio  divide The first element by 64 first row and column, excluding the first element,by 32 then divided All other elements  by 16
    dct_matrix /= 16
    dct_matrix[0, :] /= 2
    dct_matrix[:, 0] /= 2

    return dct_matrix



#describe your function
def quantization(block):



    return #quantized block (8x8)



# this functuon Transform each block from 2-D into 1-D through reading it using the zig-zag patter 
#input: 2D matrix of 8x8 shape
#output 1D array of 1x 64

def  reduce_block_dimension(blcok):
    # Initialize an empty list with 15 sublists for serpentine ordering
    template_empty_arrays = [[] for i in range(15)]

    # Traverse the 8x8 block in serpentine (zigzag) order
    for i in range(8):
        for j in range(8):
            sum_indices = i + j  # Calculate the sum of indices to determine the order
            
            # If the sum of indices is even, insert the element at the beginning of the sublist
            if sum_indices % 2 == 0:
                template_empty_arrays[sum_indices].insert(0, blcok[i][j])
            else:
                # If the sum is odd, append the element at the end of the sublist
                template_empty_arrays[sum_indices].append(blcok[i][j])



    # Flatten the list of lists into a single list to get the serpentine ordered elements
    oneD_array = [item for sublist in template_empty_arrays for item in sublist]

    return oneD_array


# function to implement the lenght code algorithem 
#input 1D array of 1x 64
#output 1D array pf 1xN where N depened on the numbers of zero
def length_code_algorthem(one_day_array):
    # run the length code algorthem 
    encoded_array = []
    count = 0

    # Iterate over the serpentine ordered array to apply run-length encoding for zeros
    for number in one_day_array:
        if number == 0:
            count += 1
        else:
            # Add zero count to encoded_array if any zeros were counted
            if count > 0:
                encoded_array.extend([0, count])
                count = 0
            encoded_array.append(number)

    # Append the encoding for the last run of zeros, if any
    if count > 0:
        encoded_array.extend([0, count])


    return encoded_array

def get_frequency(array):

    frequency_table = {}
    for i in array:
        if i in frequency_table:
            frequency_table[i] += 1
        else:
            frequency_table[i] = 1

    return frequency_table



class Node: 
	def __init__(self, freq, symbol, left=None, right=None): 

		self.freq = freq 
		self.symbol = symbol 
		self.left = left 
		self.right = right 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 


def heap_tree(frequency_table):
    symbols = list(frequency_table.keys())
    freqs = list(frequency_table.values())

    unused_nodes = []
    
    for i in range(len(symbols)):
        heapq.heappush(unused_nodes, Node(freqs[i], symbols[i]))

    
    while len(unused_nodes) > 1: 

        left = heapq.heappop(unused_nodes) 
        right = heapq.heappop(unused_nodes) 

        left.huff = 0
        right.huff = 1

        new_freq = left.freq + right.freq
        new_symbol = left.symbol + right.symbol
        new_node = Node(new_freq, new_symbol, left, right) 

        heapq.heappush(unused_nodes, new_node)

    return unused_nodes[0]



def printNodes(node, val=''): 
	newVal = val + str(node.huff) 
	if(node.left): printNodes(node.left, newVal) 
	if(node.right): printNodes(node.right, newVal) 
	if(not node.left and not node.right): print(f"{node.symbol} -> {newVal}") 

def huff_table_constr(node, huff_table=None, code_start = ''):

    if huff_table is None:
        huff_table = {}

    code = code_start + str(node.huff) 

    if(node.left): huff_table_constr(node.left,huff_table, code) 
    if(node.right): huff_table_constr(node.right,huff_table, code) 
    if(not node.left and not node.right):
        x = (node.symbol, code)
        huff_table[node.symbol] = code
    return huff_table


def get_Huffman_table(array):
    freq_table = get_frequency(array)
    tree = heap_tree(freq_table)
    huff_table = huff_table_constr(tree)
    return huff_table


def encode_huffman(array, huff_table):
    code = ''
    for i in array:
        code += huff_table[i]
    return code


def decode_huffman(encoded_str, root):
    decoded_array = []
    current_node = root
    for bit in encoded_str:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_array.append(current_node.symbol)
            current_node = root

    return decoded_array

#describe your function
def Huffman_enconding(array):
    #testing
    array= [1,1,1,2,5,9,5,3,2,5,7,4,1,2,5,9,6,3,9,8,5,2,1,4,7,5,8,9,6,2,8,7,5,6,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,8,5,2,1,4,7,8,8,6,2,5,8,7]

    table = get_Huffman_table(array)
    print(table) 
    root = heap_tree(get_frequency(array))


    encoded = encode_huffman(array, table)
    print(encoded)
    print('------------------------------')
    decoded = decode_huffman(encoded, root)
    print(decoded)

    print("Is the array simillar? ",array == decoded)
    compression_ratio = round(len(encoded)/(len(array)*8)*100)
    print(f"Compression ratio: {compression_ratio}%")

    return encoded, root      #stream of 0s & 1s






