import qrcode
from PIL import Image
import os

def generate_qr_code(data, filename="qrcode.png", box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generate a QR code from the given data.
    
    Args:
        data (str): The data to encode in the QR code
        filename (str): The filename to save the QR code image (default: "qrcode.png")
        box_size (int): The size of each box in the QR code (default: 10)
        border (int): The size of the border around the QR code (default: 4)
        fill_color (str): The color of the QR code (default: "black")
        back_color (str): The background color (default: "white")
        
    Returns:
        str: The path to the saved QR code image
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    img.save(filename)
    
    return os.path.abspath(filename)

if __name__ == "__main__":
    # Example usage
    data = input("Enter the data for the QR code: ")
    
    filename = input(
        "Enter filename to save QR code (default: qrcode): "
    ).strip() or "qrcode"

    if not filename.lower().endswith(".png"):
        filename += ".png"
    
    path = generate_qr_code(data, filename)
    print(f"QR code has been generated and saved to: {path}")
