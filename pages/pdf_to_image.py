import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os
import shutil

def pdf_to_png(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def main():
    st.title("PDF to PNG Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Create a temporary directory to store the uploaded file and images
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, uploaded_file.name)

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        pdf_images = pdf_to_png(pdf_path)

        st.markdown("### Converted Images")

        # Display PNG images in four columns
        col1, col2, col3, col4 = st.columns(4)

        for i, image in enumerate(pdf_images):
            # Save each image as a temporary PNG file
            temp_image_path = os.path.join(temp_dir, f"page_{i+1}.png")
            image.save(temp_image_path)

            # Display the image in a smaller size
            with col1:
                st.image(image, caption=f"Page {i+1}", use_column_width=True, width=200)

        # Delete temporary directory after display
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()