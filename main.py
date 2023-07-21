import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import os

def list_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_files.append(os.path.join(directory, filename))
    return image_files

def main():
    st.title("Image Files in 'output' Folder")

    output_directory = "output"  # 'output'フォルダのパスを指定

    if not os.path.exists(output_directory):
        st.warning("The 'output' folder does not exist. Please make sure to save images in that folder.")
        return

    image_files = list_image_files(output_directory)

    if not image_files:
        st.warning("No image files found in the 'output' folder.")
    else:
        st.markdown("### Image Files List")
        for image_file in image_files:
            image = open(image_file, "rb").read()
            st.image(image, caption=os.path.basename(image_file), use_column_width=True)
            st.download_button("Download", data=image, file_name=os.path.basename(image_file))

if __name__ == "__main__":
    main()