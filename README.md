#StegnoVault
StegnoVault is a web application that allows users to encode and decode hidden messages within images using steganography techniques. This project utilizes Streamlit for the user interface and provides a simple way to secure messages by embedding them in image files.

Features
Encode Messages: Users can upload an image and a secret message, which will be encoded into the image using a password for security.
Decode Messages: Users can upload an encoded image and provide the correct password to retrieve the hidden message.
Project Structure
stegnovault
├── app.py                # Main application logic using Streamlit
├── stegno_utils          # Package for encoding and decoding utilities
│   ├── __init__.py      # Initializes the stegno_utils package
│   ├── encode.py        # Logic for encoding messages into images
│   └── decode.py        # Logic for decoding messages from images
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
Installation
To run the StegnoVault application, you need to have Python installed on your machine. Follow these steps to set up the project:

Clone the repository:

git clone <repository-url>
cd stegnovault
Install the required dependencies:

pip install -r requirements.txt
Running the Application
To start the Streamlit application, run the following command in your terminal:

streamlit run app.py
This will launch the application in your default web browser, where you can choose to encode or decode messages.

Dependencies
The project requires the following Python libraries:

Streamlit
Pillow
cryptography
Make sure these libraries are listed in the requirements.txt file for easy installation.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
