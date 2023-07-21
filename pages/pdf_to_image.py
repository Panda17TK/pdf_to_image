import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

def pdf_to_png(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def main():
    st.title("PDF to PNG Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Create a temporary directory to store the uploaded file
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, uploaded_file.name)

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        pdf_images = pdf_to_png(pdf_path)

        st.markdown("### Converted Images")
        for i, image in enumerate(pdf_images):
            st.image(image, caption=f"Page {i+1}", use_column_width=True)

            # Save each image as a temporary PNG file
            temp_image_path = os.path.join(temp_dir, f"page_{i+1}.png")
            image.save(temp_image_path)

            # Download button for each image
            image_download_button = f"Download Image {i+1}"
            st.download_button(
                label=image_download_button,
                data=temp_image_path,
                file_name=f"page_{i+1}.png"
            )

if __name__ == "__main__":
    main()