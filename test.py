import qrcode
from PIL import Image
import os

qr = qrcode.QRCode(
    version=1,
    # High error correction level to ensure the QR code remains readable with a logo
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10,
    border=4,
)

target_url = "LINK_HERE.COM"
qr.add_data(target_url)
qr.make(fit=True)

# Generate QR image in RGBA mode
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

logo_filename = "logo.png"

if os.path.exists(logo_filename):
    logo = Image.open(logo_filename)

    qr_width, qr_height = qr_image.size

    # Resize logo to 25% of QR code size
    logo_size = int(qr_width * 0.25) 
    logo = logo.resize((logo_size, logo_size))

    # Calculate position to center the logo
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    qr_image.paste(logo, pos)
    
    output_filename = "branded_qr.png"
    qr_image.save(output_filename)
    print(f"QR code with logo created: {output_filename}")
else:
    print(f"WARNING: '{logo_filename}' not found!")
    print("Please add your logo as 'logo.png' to this directory and run the script again.")