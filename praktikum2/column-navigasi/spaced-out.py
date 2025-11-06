import streamlit as st

st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

from PIL import Image
img = Image.open("../assets/Animal1.jpeg")
st.title("Spaced-Out Columns")
# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)