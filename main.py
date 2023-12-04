from Encoder.encoder import *
from Decoder.decoder import *
import cv2

def split_array(base_array, chunk_size):
    # Check if the array can be evenly divided into chunks of 'chunk_size'
    if len(base_array) % chunk_size != 0:
        raise ValueError("The length of the base array is not evenly divisible by the chunk size.")
    
    # Split the array into sub-arrays of the specified chunk size
    return [base_array[i:i + chunk_size] for i in range(0, len(base_array), chunk_size)]


def main():
    image_path=r"B2DBy.jpg"
    # Load the grayscale image
    gray_image_in_pixels = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) #2D array
   
    if gray_image_in_pixels is not None:
        # Get the dimensions
        rows,columns = gray_image_in_pixels.shape
            
        rows, columns,image_blocks=generating_image_blocks(gray_image_in_pixels)  # list of 8x8 image blocks
        information_array=[]
        # loop through each block
        for block in image_blocks:
            # first transfare the information in the block to the frequesnce domain using DCT 
            freq_spectruem=DCT_matrix(block)
            # third reduce the matrix d 
            one_d_array=reduce_block_dimension(freq_spectruem)

            # quantization 

            # forth the length code algorthem 

            reduced_array=length_code_algorthem(one_d_array)

            # append to the total array
            information_array.extend(reduced_array)


        

        # huffman
        encoded_array, root_tree =Huffman_enconding(information_array) 

        # decoding
        decoded_array = decode_huffman(encoded_array, root_tree)



        #inverse length coding 
        decoded_length_coding = length_coding_decoding(decoded_array)
        # dividing the information array back to 1x64 elements 
        divided_arrays = split_array(decoded_length_coding,64)

        # decoding 
        reverse_blocks=[]
        for block in divided_arrays:
            # inverse of the zig zag pattern to get 8x8 matrix
            two_d_matrix=expened_matrix_dimantion(block)
            # geting the time domain using inverse DCT 
            time_domain=optimized_IDCT_matrix(two_d_matrix)
        
            reverse_blocks.append(time_domain)
        

        # collection the 2d 8x8 back together 
        generated_image=collect_image(reverse_blocks,rows,columns)
        image = np.uint8(generated_image)

        # Save the image to a file
        cv2.imwrite('output_image.png', image)



    else:
        print("Failed to load the image.")
        return None



    pass




if __name__ == '__main__':
    main()




