import os
import subprocess
import argparse


def compress_images(input_dir, output_dir, resize_percent=25):
    """
    Compress images in a directory by resizing them using ImageMagick's convert tool.

    Args:
        input_dir (str): Path to the input directory containing images.
        output_dir (str): Path to the output directory where compressed images will be saved.
        resize_percent (int): Percentage to resize the images (default: 25%).
    """
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, file_name)

        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
            try:
                output_file_path = os.path.join(output_dir, file_name)

                subprocess.run(
                    [
                        "convert",
                        "-resize",
                        f"{resize_percent}%",
                        f"{input_file_path}",
                        f"{output_file_path}",
                    ],
                    check=True,
                )

                print(f"Compressed and saved: {output_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to process {file_name}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compress images in a directory by resizing them."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        required=True,
        help="Path to the input directory containing images.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Path to the output directory where compressed images will be saved.",
    )
    parser.add_argument(
        "--resize_percent",
        type=int,
        default=25,
        help="Percentage to resize the images (default: 25%).",
    )

    args = parser.parse_args()

    compress_images(args.input_dir, args.output_dir, args.resize_percent)
