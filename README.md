# Custom QR Code Generator with Logo

This Python script generates a high-quality QR code and embeds a custom logo in the center. It uses high error correction to ensure the QR code remains scannable even with the logo overlay.

## Features

-   **Custom Logo Embedding:** Automatically centers and resizes your logo (`logo.png`) onto the QR code.
-   **High Error Correction:** Uses `ERROR_CORRECT_H` (High) to prevent data loss due to the logo.
-   **Customizable:** You can easily change the target URL, box size, and border.
-   **Output:** Saves the final image as a PNG file.

## Prerequisites

You need Python installed on your system. This project relies on the following libraries:

-   `qrcode`
-   `Pillow` (PIL)

## Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/IBullseyea/custom-qr-generator.git
    cd custom-qr-generator
    ```

2.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Add your logo:** Place your logo image file in the project directory and name it `logo.png`.
2.  **Edit the script (Optional):** Open `test.py` and change the `target_url` variable to your desired URL.
    ```python
    target_url = "https://www.your-website.com"
    ```
3.  **Run the script:**
    ```bash
    python test.py
    ```
4.  **Get your QR Code:** The script will generate a file named `branded_qr.png` in the same directory.

## Example

The script takes a standard URL and a logo file, combines them, and outputs a scannable QR code image with your branding in the center.

## License

This project is open source and available under the [MIT License](LICENSE).
