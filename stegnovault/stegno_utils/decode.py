from PIL import Image
from cryptography.fernet import Fernet
import base64

def decode_message(image_path, password):
    """
    Decodes a hidden message from an image using the provided password.

    Args:
        image_path (str): Path to the encoded image.
        password (str): Password used for decryption.

    Returns:
        str: The decoded and decrypted message.

    Raises:
        ValueError: If decryption fails or the image is invalid.
    """
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    w, h = image.size

    # Extract binary data from the image
    binary_data = ""
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)  # Extract the LSB of the red channel

    # Debugging: Print extracted binary data
    print(f"Extracted binary data (first 64 bits): {binary_data[:64]}...")

    # Stop at the delimiter
    delimiter = "11111111"
    if delimiter in binary_data:
        binary_data = binary_data[:binary_data.index(delimiter)]
    else:
        raise ValueError("No hidden message found or the image is corrupted.")

    # Debugging: Print truncated binary data
    print(f"Truncated binary data (first 64 bits): {binary_data[:64]}...")

    # Convert binary data to string
    byte_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in byte_data:
        try:
            decoded_data += chr(int(byte, 2))
        except ValueError:
            break  # Stop if invalid binary data is encountered

    # Debugging: Print decoded data before decryption
    print(f"Decoded data (before decryption): {decoded_data}")

    # Remove any non-ASCII characters and trailing invalid characters
    decoded_data = "".join(char for char in decoded_data if ord(char) < 128)
    decoded_data = decoded_data.rstrip("\x00")  # Remove null characters
    decoded_data = decoded_data.rstrip()  # Remove trailing whitespace or invalid characters

    # Debugging: Print final sanitized data
    print(f"Final sanitized decoded data: {decoded_data}")

    # Validate decoded data length
    if len(decoded_data) == 0:
        raise ValueError("Decoded data is empty. The image might be corrupted or the message is missing.")

    # Decrypt the message
    try:
        cipher_suite = Fernet(base64.urlsafe_b64encode(password.encode().ljust(32)[:32]))
        decrypted_message = cipher_suite.decrypt(decoded_data.encode()).decode()
        return decrypted_message
    except Exception as e:
        print(f"Decryption error: {e}")  # Debugging: Print the exact error
        raise ValueError("Decryption failed. Ensure the password is correct and the image is valid.") from e