import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
jumlah_mahasiswa = [120, 150, 100, 80]

# Data tambahan untuk tahun yang berbeda
jumlah_mahasiswa_2024 = [110, 140, 95, 85]

x = range(len(jurusan)) # Indeks posisi untuk batang
width = 0.4

# Batang untuk tahun 2023 (diletakkan di posisi x)
plt.bar(x, jumlah_mahasiswa, width, label='2023', color='skyblue')

# Batang untuk tahun 2024 (diletakkan sedikit bergeser dari x)
plt.bar([p + width for p in x], jumlah_mahasiswa_2024, width, label='2024', color='orange')

plt.title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)

# Mengatur Label x-axis di tengah antara dua batang
plt.xticks([p + width / 2 for p in x], jurusan) 
plt.legend()
plt.show()