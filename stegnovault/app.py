import streamlit as st
from stegno_utils import encode_message, decode_message
import os

st.title("🔐 StegnoVault - Hide Secret Messages in Images")

option = st.selectbox("Choose an option:", ["Encode", "Decode"])

if option == "Encode":
    st.subheader("Encode a secret message into an image")

    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        message = st.text_area("Enter your secret message:")
        password = st.text_input("Enter a password to secure the message:")

        if st.button("Encode Message"):
            if message and password:
                with open("uploaded_image.png", "wb") as f:
                    f.write(uploaded_image.getbuffer())

                try:
                    encoded_image_path = encode_message("uploaded_image.png", message, password)
                    st.success(f"Message encoded successfully! The encoded image is saved at: {encoded_image_path}")
                    st.image(encoded_image_path, caption="Encoded Image", use_container_width=True)
                except Exception as e:
                    st.error(f"Failed to encode message: {str(e)}")
            else:
                st.error("Please provide both a message and a password.")

elif option == "Decode":
    st.subheader("Decode a hidden message from an image")

    uploaded_encoded_image = st.file_uploader("Upload an encoded image", type=["png", "jpg", "jpeg"])
    if uploaded_encoded_image:
        password = st.text_input("Enter the password for decryption:")

        if st.button("Decode Message"):
            if password:
                with open("encoded_image.png", "wb") as f:
                    f.write(uploaded_encoded_image.getbuffer())

                try:
                    decoded_message = decode_message("encoded_image.png", password)
                    st.success(f"Decoded Message: {decoded_message}")
                except ValueError as e:
                    st.error(f"Failed to decode message: {str(e)}")
                except Exception as e:
                    st.error("An unexpected error occurred during decoding.")
            else:
                st.error("Please provide the password to decode the message.")