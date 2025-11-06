import streamlit as st
import pandas as pd
import numpy as np

st.title("MAP")
st.subheader("Praktikum-2 Visualisasi Data")
st.write("kelompok-3")
st.markdown("""
Nama Lengkap Anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10, 10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)