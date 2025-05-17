import os
from pathlib import Path
import tifffile
from tifffile import TiffWriter
import argparse
from tqdm import tqdm  # Import tqdm for progress bar


# Hardcoded parameters
TILE_SIZE = 256
COMPRESSION = "jpeg"
RESOLUTION = (0.25, 0.25)


def process_wsi_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all TIFF files in the input folder
    tiff_files = [file_name for file_name in os.listdir(input_folder) if file_name.endswith(".tif") or file_name.endswith(".tiff")]

    # Process all TIFF files in the input folder with a progress bar
    for file_name in tqdm(tiff_files, desc="Processing files", unit="file"):
        input_file = os.path.join(input_folder, file_name)
        print(f"Processing: {input_file}")

        try:
            # Step 1: Extract the highest resolution image (Directory 0) in memory
            with tifffile.TiffFile(input_file) as tif:
                data = tif.pages[0].asarray()  # Load the highest resolution image

            # Step 2: Convert directly to a tiled pyramid TIFF
            pyramid_output_path = os.path.join(output_folder, f"{Path(file_name).stem}_compatible.tif")
            with TiffWriter(pyramid_output_path, bigtiff=True) as tif:
                tif.write(
                    data,
                    tile=(TILE_SIZE, TILE_SIZE),
                    compression=COMPRESSION,
                    resolution=RESOLUTION,
                    metadata={'axes': 'YXC'}
                )
            print(f"Tiled pyramid TIFF saved at {pyramid_output_path}")

        except Exception as e:
            print(f"Failed to process {input_file}: {e}")

    print("All files processed!")


def main():
    parser = argparse.ArgumentParser(description="Process whole-slide images (WSI) to create tiled pyramid TIFFs.")
    parser.add_argument(
        "--input_folder",
        type=str,
        required=True,
        help="Path to the folder containing input WSI TIFF files."
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        required=True,
        help="Path to the folder where output tiled pyramid TIFF files will be saved."
    )

    args = parser.parse_args()

    # Call the processing function with parsed arguments
    process_wsi_files(
        input_folder=args.input_folder,
        output_folder=args.output_folder
    )


if __name__ == "__main__":
    main()
