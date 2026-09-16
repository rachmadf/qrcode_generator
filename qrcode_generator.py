import os
import re

import qrcode


def validate_filename(filename: str) -> str:
    """
    Validate and normalize the QR code output filename.

    The filename must contain only a simple filename and must not
    include directory paths or path traversal characters.

    Args:
        filename: The requested output filename.

    Returns:
        A validated filename with a .png extension.

    Raises:
        ValueError: If the filename is empty, contains a directory path,
            or contains invalid characters.
    """
    filename = filename.strip()

    if not filename:
        raise ValueError("QR code filename cannot be empty.")

    # Prevent directory paths and path traversal.
    if os.path.basename(filename) != filename:
        raise ValueError("Filename must not contain a directory path.")

    # Allow letters, numbers, spaces, underscores, hyphens, and periods.
    if not re.fullmatch(r"[A-Za-z0-9 _.-]+", filename):
        raise ValueError(
            "Filename contains invalid characters. "
            "Use letters, numbers, spaces, underscores, hyphens, or periods."
        )

    # Add .png extension automatically.
    if not filename.lower().endswith(".png"):
        filename += ".png"

    return filename


def generate_qr_code(
    data: str,
    filename: str = "qrcode.png",
    output_dir: str = "output",
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
) -> str:
    """
    Generate a QR code from the given data and save it as a PNG image.

    Args:
        data: The text, URL, or other data to encode.
        filename: Output filename. The .png extension is added automatically
            if it is not provided.
        output_dir: Directory where the QR code image will be saved.
        box_size: Size of each QR code module.
        border: Width of the QR code border in modules.
        fill_color: Foreground color of the QR code.
        back_color: Background color of the QR code.

    Returns:
        The absolute path to the generated QR code image.

    Raises:
        ValueError: If the data, filename, output directory, box size,
            or border is invalid.
    """
    # Validate data.
    data = data.strip()

    if not data:
        raise ValueError("QR code data cannot be empty.")

    # Validate filename.
    filename = validate_filename(filename)

    # Validate QR code configuration.
    if box_size <= 0:
        raise ValueError("box_size must be greater than 0.")

    if border < 0:
        raise ValueError("border cannot be negative.")

    # Validate output directory.
    output_dir = output_dir.strip()

    if not output_dir:
        raise ValueError("Output directory cannot be empty.")

    # Create output directory if it does not exist.
    os.makedirs(output_dir, exist_ok=True)

    # Build complete output path.
    output_path = os.path.join(output_dir, filename)

    # Create QR code.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image.
    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color,
    )

    # Save image.
    img.save(output_path)

    return os.path.abspath(output_path)


if __name__ == "__main__":
    print("QR Code Generator")
    print("-----------------")

    data = input("Enter the data for the QR code: ")

    filename = input(
        "Enter filename to save QR code (default: qrcode): "
    ).strip() or "qrcode"

    try:
        path = generate_qr_code(data, filename)
        print(f"QR code has been generated and saved to: {path}")

    except ValueError as error:
        print(f"Error: {error}")