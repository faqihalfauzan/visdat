# import library
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# dataset
Suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
Penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 160]

#data penjualan
Penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
Penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

#data untuk analisis
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanila': [82, 80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Stroberi': [55, 50, 55, 60, 65, 60, 65, 70, 72],
    'kelembapan': [50, 65, 70, 75, 80, 85, 90, 95, 100]
}
#konversi ke dataframe
df = pd.DataFrame(data)

#layout utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header('Pengaturan Visualisasi')

#menu di sidebar
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"

    )

)

#identitas kelompok
st.caption("Praktikum 5")
st.markdown("""
nama lengkap anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")

# basic scater plot
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(Suhu, Penjualan)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)

# basic scater plot
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(Suhu, Penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan')
    ax.grid(True)
    st.pyplot(fig)

# 3 Multiple Scatter plot
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(Suhu, Penjualan_weekdays, color='green', label="Hari kerja", s=80)
    ax.scatter(Suhu, Penjualan_weekend, color='purple', label="Akhir Pekan", s=80)
    
    
    ax.grid(True)
    st.pyplot(fig)

# 4 Analisis Scatter Plot
def scatter_3_variable():
    st.subheader("3. Analisis Scatter Plot")
    #opsi jenis eskrim
    jenis_eskrim = st.selectbox('Pilih Jenis Es krim', ['Cokelat', 'Vanila', 'stroberi'])
    
    # logika untuk opsi jenis eksirm berdasarkan pilihan
    if jenis_eskrim == 'Cokelat':
        Penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        Penjualan = df['Penjualan_Vanila']
    else:
        Penjualan = df["Penjualan_Stroberi"]

    st.subheader("Data penjualan dan Suhu")
    st.dataframe(df)

    # scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], Penjualan, c=df['kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    # styling
    ax.set_title('Hubungan Penjualan {jenis_eskrim} vs Suhu kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='kelembapan (%)')

    st.pyplot(fig)

    #ringkasan hubungan
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik menunjukkan hubungan antara suhu, kelembaban, dan penjualan eskrim jenis **(jenis_eskrim)**')
     
# Routing berdasarkan menu sidebar
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variable()