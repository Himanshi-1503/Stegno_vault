from PIL import Image
from cryptography.fernet import Fernet
import base64

def encode_message(image_path, message, password):
    # Open the image
    image = Image.open(image_path)
    cipher_suite = Fernet(base64.urlsafe_b64encode(password.encode().ljust(32)[:32]))
    encrypted_message = cipher_suite.encrypt(message.encode())

    # Encode the message into the image
    new_image = image.copy()
    data = encrypted_message.decode()
    w, h = new_image.size
    pixels = new_image.load()

    # Convert the message to binary and add a delimiter
    binary_data = ''.join(format(ord(char), '08b') for char in data) + "11111111"
    print(f"Binary data to encode (first 64 bits): {binary_data[:64]}...")  # Debugging
    data_index = 0

    for y in range(h):
        for x in range(w):
            if data_index < len(binary_data):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_data[data_index])  # Modify the LSB of the red channel
                pixels[x, y] = (r, g, b)
                data_index += 1

    # Save the encoded image
    encoded_image_path = "encoded_image.png"
    new_image.save(encoded_image_path)
    return encoded_image_path