import streamlit as st
import numpy as np

st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

st.title("Container")
with st.container():
    st.write("Element Inside Contianer")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
st.write("Element Outside Container")

st.title("Out of Order Container")
# Defining Contianers
container_one = st.container()
container_one.write("Element One Inside Contianer")
st.write("Element Outside Contianer")
# Now insert few more elements in the container_one
container_one.write("Element Two Inside Contianer")
container_one.line_chart(np.random.randn(40, 4))