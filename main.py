from Encoder.encoder import *
from Decoder.decoder import *
import cv2



def main():
    image_path=r"C:\Users\fatma taha\Desktop\ZC\Info\Lab6\B2DBy.jpg"
    # Load the grayscale image
    gray_image_in_pixels = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) #2D array
   
    if gray_image_in_pixels is not None:
     
        image_blocks=generating_image_blocks(gray_image_in_pixels)  # list of 8x8 image blocks

        reverse_blocks={}
        # loop through each block
        for block in image_blocks:
            # first transfare the information in the block to the frequesnce domain using DCT 
            freq_spectruem=DCT_matrix(image_blocks[block])
            # third reduce the matrix d 
            one_d_array=reduce_block_dimension(freq_spectruem)

            # quantization 

            # forth the length code algorthem 

            reduced_array=length_code_algorthem(one_d_array)

            # huffman 

            #decoding 
            decoded_array=length_coding_decoding(reduced_array)

            two_d_matrix=expened_matrix_dimantion(decoded_array)

            time_domain=optimized_IDCT_matrix(two_d_matrix)

            reverse_blocks[block]=time_domain


        generated_image=collect_image(reverse_blocks)
        image = np.uint8(generated_image)

        # Save the image to a file
        cv2.imwrite('output_image.png', image)



    else:
        print("Failed to load the image.")
        return None



    pass




if __name__ == '__main__':
    main()




