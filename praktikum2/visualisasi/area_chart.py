import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")

st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.area_chart(df)