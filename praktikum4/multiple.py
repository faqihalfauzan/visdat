import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Area Chart")

st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

# --- Perbaikan untuk Streamlit ---
# Membuat figure dan axes object
fig, ax = plt.subplots(figsize=(10, 6))

# Data
jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
jumlah_mahasiswa = [120, 150, 100, 80]
jumlah_mahasiswa_2024 = [110, 140, 95, 85]

x = np.arange(len(jurusan))
width = 0.4

# Gunakan ax.bar() BUKAN plt.bar()
ax.bar(x, jumlah_mahasiswa, width, label='2023', color='skyblue')
ax.bar(x + width, jumlah_mahasiswa_2024, width, label='2024', color='orange')

# Gunakan ax.set_... BUKAN plt....
ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks(x + width / 2) 
ax.set_xticklabels(jurusan, rotation=45, ha='right')
ax.legend()
fig.tight_layout()

# --- Tampilkan di Streamlit ---
st.pyplot(fig)