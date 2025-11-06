import streamlit as st

st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

st.title('Exapanders')
# Defining Expanders
with st.expander("Streamlit with Python"):
    st.write("Develop ML Applications in Minutes!!!!")