import streamlit as st

st.title("Praktikum 1 visualisasi data")
st.subheader("Bagian 2-data-elements")
st.markdown("""
nama lengkap anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")

st.write("Displaying an Images")
#displaying image by specifying path
st.image("assets/Animal2.jpeg")
#image Courtesy by unplesh
st.write("Image Courtesy: unplash.com")

import streamlit as st
st.write("Displaying Multiple Image")
#listening out animal images
animal_images = [
    'assets/Animal1.jpeg',
    'assets/Animal2.jpeg',
    'assets/Animal6.jpg',
    'assets/Animal4.jpeg',
   
]
#Displaying Multiple images with width 150
st.image(animal_images, width=150)
# image courtesy
st.write("Image Courtesy: Unplash") 

import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as file:
        encoded_string = base64.b64encode(file.read())
    st.write("Image Courtesy: unsplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string.decode()}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image('assets/Animal5.jpg')

import streamlit as st
from PIL import Image

# Membuka gambar dari path lokal
original_image = Image.open("assets/Animal1.jpeg")

# Menampilkan gambar asli
st.title("Original Image")
st.image(original_image)

# Mengubah ukuran gambar menjadi 600x400
resized_image = original_image.resize((600, 400))

# Menampilkan gambar hasil resize
st.title("Resized Image")
st.image(resized_image)