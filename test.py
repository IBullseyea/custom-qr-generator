import qrcode
from PIL import Image
import os

qr = qrcode.QRCode(
    version=1,
    # High error correction level to ensure the QR code remains readable with a logo
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=50, # Increased resolution for high-quality printing
    border=4,
)

target_url = "https://www.youtube.com/"
qr.add_data(target_url)
qr.make(fit=True)

# Generate QR image in RGBA mode
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

logo_filename = "logo.png"

if os.path.exists(logo_filename):
    logo = Image.open(logo_filename)

    qr_width, qr_height = qr_image.size

    # Calculate maximum dimension for the logo (25% of QR code width)
    max_logo_size = int(qr_width * 0.25)

    # Calculate new size preserving aspect ratio
    logo_w, logo_h = logo.size
    aspect_ratio = logo_w / logo_h

    if logo_w > logo_h:
        new_w = max_logo_size
        new_h = int(max_logo_size / aspect_ratio)
    else:
        new_h = max_logo_size
        new_w = int(max_logo_size * aspect_ratio)
    
    # Use LANCZOS for better quality resizing
    # We keep the original 'logo' variable intact for the border calculation
    logo_main = logo.resize((new_w, new_h), Image.LANCZOS)

    # Calculate position to center the logo
    pos_main = ((qr_width - new_w) // 2, (qr_height - new_h) // 2)

    # Create a white border that follows the logo's shape
    if logo.mode == 'RGBA':
        # Calculate border width relative to QR size (e.g., 2% of total width)
        border_width = int(qr_width * 0.02)
        
        # Calculate size for the border image (slightly larger than the main logo)
        border_w = new_w + (border_width * 2)
        border_h = new_h + (border_width * 2)
        
        # Resize the original logo to this larger size to get the correct shape mask
        logo_border_base = logo.resize((border_w, border_h), Image.LANCZOS)
        
        # Create a pure white image
        logo_bg = Image.new('RGBA', (border_w, border_h), "white")
        
        # Apply the alpha channel from the resized logo to the white image
        # This creates a white silhouette exactly matching the logo's shape
        logo_bg.putalpha(logo_border_base.split()[3])
        
        # Calculate position for the border (centered)
        pos_bg = ((qr_width - border_w) // 2, (qr_height - border_h) // 2)
        
        # Paste the white silhouette first
        qr_image.paste(logo_bg, pos_bg, logo_bg)
        
        # Paste the main logo on top
        qr_image.paste(logo_main, pos_main, logo_main)
    else:
        # If no transparency, just paste the logo directly
        qr_image.paste(logo_main, pos_main)
    
    output_filename = "1branded_qr.png"
    qr_image.save(output_filename)
    print(f"QR code with logo created: {output_filename}")
else:
    print(f"WARNING: '{logo_filename}' not found!")
    print("Please add your logo as 'logo.png' to this directory and run the script again.")