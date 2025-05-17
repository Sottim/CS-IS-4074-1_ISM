import tifffile
import numpy as np
import openslide
from pathlib import Path
from tqdm import tqdm
import logging
import yaml
import argparse

# Setup logging
logging.basicConfig(
    filename="process_log_multiple_markers.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def extract_full_resolution_image(file_path, output_dir):
    try:
        logging.info(f"Processing started: {file_path}")
        with tifffile.TiffFile(file_path) as tif:
            series = tif.series[1]
            full_res_level = series.levels[0]
            full_image = full_res_level.asarray()
            output_path = Path(output_dir) / (Path(file_path).stem + "_compatible.tiff")
            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)
            tifffile.imwrite(
                output_path,
                full_image,
                bigtiff=True,
                compression="jpeg",
                tile=(512, 512),
                photometric="rgb",
            )
            logging.info(f"Processing completed: {file_path} -> {output_path}")
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Process SCN files listed in a YAML file."
    )
    parser.add_argument(
        "config_file", type=str, help="Path to the YAML configuration file"
    )
    args = parser.parse_args()

    # Read the YAML configuration file
    try:
        with open(args.config_file, "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        logging.error(f"Error reading YAML file: {e}")
        return

    # Extract file mappings from config
    file_mappings = config.get("files", [])

    # Validate inputs
    if not file_mappings:
        print("No files specified in the YAML file.")
        logging.warning("No files specified in the YAML file.")
        return

    # Process each file
    for mapping in tqdm(file_mappings, desc="Processing SCN files", unit="file"):
        scn_file = Path(mapping.get("input", ""))
        output_dir = Path(mapping.get("output_dir", ""))

        # Validate file and output directory
        if not scn_file.exists() or scn_file.suffix.lower() != ".scn":
            print(f"Skipping {scn_file}: File does not exist or is not an .scn file.")
            logging.warning(
                f"Skipping {scn_file}: File does not exist or is not an .scn file."
            )
            continue

        if not output_dir:
            print(f"Skipping {scn_file}: No output directory specified.")
            logging.warning(f"Skipping {scn_file}: No output directory specified.")
            continue

        extract_full_resolution_image(scn_file, output_dir)


if __name__ == "__main__":
    main()
