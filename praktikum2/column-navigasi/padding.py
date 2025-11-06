import streamlit as st
from PIL import Image

st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

img = Image.open("../assets/Animal2.jpeg")
st.title("Padding")
# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)

with col2:
    col2.image(img)