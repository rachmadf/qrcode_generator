# QR Code Generator

A simple Python-based QR code generator that converts text or other data into a QR code image.
Commonly, I use it to generate QR-Code for shared file link (like link of document in google drive).
The project uses the `qrcode` library with Pillow to generate and save QR code images. The generator supports configurable image size, border, foreground color, and background color.

## Features

* Generate QR codes from user-provided data
* Save QR codes as image files
* Configurable QR code box size
* Configurable border size
* Custom foreground and background colors
* High error correction level
* Simple command-line interface
* Reusable `generate_qr_code()` function

## Technologies

* Python
* `qrcode`
* Pillow

## Installation

Clone the repository:

```bash
git clone https://github.com/rachmadf/qrcode_generator.git
cd qrcode_generator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Python script:

```bash
python qrcode_generator.py
```

The program will ask for the data to encode:

```text
Enter the data for the QR code:
Enter filename to save QR code (default: qrcode.png):
```

For example:

```text
Enter the data for the QR code: https://github.com/rachmadf
Enter filename to save QR code (default: qrcode.png): github_profile.png
```

The generated QR code will be saved as the specified image file.

## Python Function

The core functionality is provided by the `generate_qr_code()` function:

```python
generate_qr_code(
    data,
    filename="qrcode.png",
    box_size=10,
    border=4,
    fill_color="black",
    back_color="white"
)
```

### Parameters

| Parameter | Description                   | Default |
| --------- | ------------------------------| ------- |
| data      | Data to encode in the QR code |         |
| filename  | Output image filename         | abc.png |
| border    | Size of the QR code border    | 4       |
| box_size  | Size of each QR code module   | 10      |
| fill_color| QR code foreground color      | Black   |
| back_color| QR code background color      | White   |

The function returns the absolute path of the generated QR code image.

Error Correction

The generator uses the QR Code High Error Correction Level (H). This provides greater resilience to damage or obstruction in the generated QR code.

Project Structure
qrcode_generator/
├── qrcode_generator.py
├── requirements.txt
├── .gitignore
└── README.md
Example Output

A QR code image is generated from the supplied data and saved locally according to the filename provided by the user.

Author

Rachmad Fitriyanto

GitHub: https://github.com/rachmadf

Portfolio: rachmadfitriyanto.pythonanywhere.com

License

This project is available for educational and personal use.
