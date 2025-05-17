import os
import subprocess
import openslide
from tqdm import tqdm

def is_pyramidal_tiff(file_path):
    """
    Check if the given TIFF file is a pyramidal TIFF compatible with OpenSlide.
    Returns True if compatible, False otherwise.
    """
    try:
        slide = openslide.OpenSlide(file_path)
        # Check if there are multiple levels (indicating a pyramidal image)
        return slide.level_count > 1
    except openslide.OpenSlideError:
        return False

def convert_to_pyramidal(file_path, output_path):
    """
    Convert a TIFF file to a pyramidal TIFF format using VIPS.
    """
    command = [
        "vips", "tiffsave", file_path, output_path,
        "--tile", "--pyramid", "--compression", "none", "--bigtiff"
    ]
    subprocess.run(command, check=True)
    print(f"Converted {file_path} to pyramidal format at {output_path}")

# def convert_to_pyramidal(file_path, output_path):
#     command = [
#         "--tile-height", "256",
#         "--bigtiff",
#         "--pyramid-depth", "4"  # Explicitly define pyramid depth
#     ]
#     subprocess.run(command, check=True)

def process_images(input_dir, output_dir):
    """
    Process all TIFF files in the input directory. Convert them to a pyramidal format if necessary.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Get list of TIFF files
    tiff_files = [f for f in os.listdir(input_dir) if f.endswith(".tif") or f.endswith(".tiff")]

    # Use tqdm for the progress bar
    for file_name in tqdm(tiff_files, desc="Processing images", unit="file"):
        file_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_pyramid.tif")

        if not is_pyramidal_tiff(file_path):
            print(f"{file_name} is not in pyramidal format. Converting...")
            convert_to_pyramidal(file_path, output_path)
        else:
            print(f"{file_name} is already in pyramidal format. Skipping conversion.")

# Define your input and output directories
input_dir = "/media/network/hdd/santosh/OPTRASCAN_IISER_Round_1/IISER_Box_1/"
output_dir = "/media/network/hdd/santosh/OPTRASCAN_IISER_Round_1/OPTRASCAN_IISER_Round_1_modified_2_pyrimid/"

# Run the script
process_images(input_dir, output_dir)
