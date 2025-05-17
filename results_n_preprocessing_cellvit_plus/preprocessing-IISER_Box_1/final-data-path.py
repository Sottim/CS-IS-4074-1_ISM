import os
import csv
import argparse

def generate_filelist(input_dir, output_csv, file_extension=".tif", slide_mpp=0.25, magnification=40.0):
    """
    Generate a CSV file listing all files with the given extension in the input directory,
    along with slide_mpp and magnification columns.

    Args:
        input_dir (str): Path to the directory containing the files.
        output_csv (str): Path to the output CSV file.
        file_extension (str): File extension to filter by (e.g., '.tif').
        slide_mpp (float): The MPP (microns per pixel) value to be added to the CSV.
        magnification (float): The magnification value to be added to the CSV.
    """
    # Ensure the file extension starts with a dot
    if not file_extension.startswith("."):
        file_extension = f".{file_extension}"

    # Get all files with the given extension in the directory
    file_paths = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(file_extension):
                file_paths.append(os.path.join(root, file))

    # Write file paths, slide_mpp, and magnification to the CSV file
    with open(output_csv, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["path", "slide_mpp", "magnification"])  # Write the header
        for path in file_paths:
            writer.writerow([path, slide_mpp, magnification])

    print(f"File list with slide_mpp and magnification saved to {output_csv}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a CSV file listing all files in a directory.")
    parser.add_argument("input_dir", help="Path to the directory containing the files.")
    parser.add_argument("output_csv", help="Path to the output CSV file.")
    parser.add_argument("--file_extension", default=".tif", help="File extension to filter by (default: .tif).")
    parser.add_argument("--slide_mpp", type=float, default=0.25, help="Slide MPP value to add (default: 0.25).")
    parser.add_argument("--magnification", type=float, default=40.0, help="Magnification value to add (default: 40.0).")

    args = parser.parse_args()
    generate_filelist(args.input_dir, args.output_csv, args.file_extension, args.slide_mpp, args.magnification)
