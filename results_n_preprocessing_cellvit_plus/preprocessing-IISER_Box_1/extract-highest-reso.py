# import tifffile

# # Path to your multi-page TIFF file
# input_file = "/media/network/hdd/santosh/OPTRASCAN_IISER_Round_1/IISER_Box_1/20190610_97_800-15_G-15-4175-A_Biopsy_ER_HnE_40X.tif"

# # Path to save the single-page TIFF
# output_file = "/home/KutumLabGPU/Documents/santosh/capstone_project/models/WSIDimension/output_single_layer.tif"

# # Open and extract Directory 0
# with tifffile.TiffFile(input_file) as tif:
#     data = tif.pages[0].asarray()  # Load the highest resolution image
#     tifffile.imwrite(output_file, data)

# print(f"Single-layer TIFF saved at {output_file}")


from tifffile import TiffWriter, imread

# Read the single-layer TIFF
image = imread("/home/KutumLabGPU/Documents/santosh/capstone_project/models/WSIDimension/output_single_layer.tif")

# Save as a tiled pyramid TIFF
with TiffWriter("/home/KutumLabGPU/Documents/santosh/capstone_project/models/WSIDimension/compatible_output.tif", bigtiff=True) as tif:
    tif.write(image, tile=(256, 256), compression="jpeg", resolution=(0.25, 0.25), metadata={'axes': 'YXC'})

