import argparse
import os
import tifffile
import numpy as np
import openslide
from pathlib import Path
from tqdm import tqdm
import logging

# Setup logging
logging.basicConfig(
    filename="process_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def extract_full_resolution_image(file_path, output_dir):
    try:
        logging.info(f"Processing started: {file_path}")
        with tifffile.TiffFile(file_path) as tif:
            series = tif.series[1]  # Assuming series[1] is the full resolution
            full_res_level = series.levels[0]
            full_image = full_res_level.asarray()
            output_path = Path(output_dir) / (Path(file_path).stem + "_compatible.tiff")
            tifffile.imwrite(
                output_path,
                full_image,
                bigtiff=True,
                compression="jpeg",
                tile=(512, 512),
                photometric="rgb",
            )
            logging.info(f"Processing completed: {file_path}")
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Process SCN files in a directory.")
    parser.add_argument(
        "input_dir", type=str, help="Path to the directory containing .scn files"
    )
    parser.add_argument(
        "output_dir", type=str, help="Path to the directory to save .tiff files"
    )
    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    scn_files = list(input_dir.glob("*.scn"))
    if not scn_files:
        print("No .scn files found in the input directory.")
        return
    for scn_file in tqdm(scn_files, desc="Processing SCN files", unit="file"):
        extract_full_resolution_image(scn_file, output_dir)


if __name__ == "__main__":
    main()
