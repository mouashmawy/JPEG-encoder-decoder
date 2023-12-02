import heapq 

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


#testing
array= [1,1,1,2,5,9,5,3,2,5,7,4,1,2,5,9,6,3,9,8,5,2,1,4,7,5,8,9,6,2,8,7,5,6,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,9,7,4,5,5,5,5,5,5,5,6,6,9,8,5,2,1,4,7,8,8,6,2,5,8,7]

table = get_Huffman_table(array)
print(table)

print(encode_huffman(array, table))