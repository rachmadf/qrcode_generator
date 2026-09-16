# QR Code Generator

A Python-based QR Code Generator with both a reusable Python function,
command-line interface (CLI), and responsive Flask web interface.

The web application allows users to enter text or URLs, customize the
QR code appearance, preview the result, and download the generated PNG
image.

## Features

### Core QR Generation

- Generate QR codes from text, URLs, and other data
- High error correction using `ERROR_CORRECT_H`
- Configurable QR module size
- Configurable QR border
- Custom foreground and background colors
- PNG output
- Reusable Python function
- Filename validation
- Path traversal protection
- Automatic `.png` extension

### Web Interface

- Responsive Bootstrap-based layout
- Three-section interface:
  1. Input
  2. Customization
  3. QR Code Preview
- Text/URL character counter
- Filename input with automatic `.png` extension
- Foreground color picker
- Background color picker
- QR size control
- Border control
- Generated QR code preview
- Generated filename display
- PNG download
- Clear/reset action
- Server-side validation
- User-friendly error presentation
- Mobile-responsive layout

## Technologies

- Python
- Flask
- `qrcode`
- Pillow
- Bootstrap 5
- HTML5
- JavaScript

## Project Structure

```text
qrcode_generator/
│
├── app.py
├── qrcode_generator.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── output/
│
├── static/
│   └── generated/
│
└── templates/
    └── index.html

Author

Rachmad Fitriyanto

GitHub: https://github.com/rachmadf

Portfolio: rachmadfitriyanto.pythonanywhere.com

License: This project is available for educational and personal use.
