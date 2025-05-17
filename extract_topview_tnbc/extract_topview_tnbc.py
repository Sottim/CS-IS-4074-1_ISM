import os
import tifffile
from PIL import Image
import argparse
from tqdm import tqdm


def process_tiff_files(input_dir, output_dir):
    """
    :param input_dir: Directory containing .tiff files.
    :param output_dir: Directory to save the extracted .png files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    tiff_files = [
        f for f in os.listdir(input_dir) if f.lower().endswith((".tiff", ".tif"))
    ]

    for file_name in tqdm(tiff_files, desc="Processing files"):
        tiff_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(
            output_dir, f"{os.path.splitext(file_name)[0]}.png"
        )

        try:
            # Read the .tiff file using tifffile
            with tifffile.TiffFile(tiff_file_path) as tif:
                # Get the first page (level 0 - highest resolution)
                level_0 = tif.pages[0].asarray()

                img = Image.fromarray(level_0)

                img.save(output_file_path)

        except Exception as e:
            print(f"Error processing file {file_name}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract top-level views from .tiff files and save them as .png files."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        required=True,
        help="Path to the directory containing .tiff files.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Path to the destination directory for .png files.",
    )

    args = parser.parse_args()

    process_tiff_files(args.input_dir, args.output_dir)
