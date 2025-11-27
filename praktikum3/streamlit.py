import streamlit as st
import matplotlib.pyplot as plt

# --- Sample data ---
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# --- FUNGSI PLOT ---

def line_plot():
    """Plot tunggal Produk A (sederhana)"""
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig) # Menampilkan di Streamlit

def customize_line_plot():
    """Plot ganda dengan marker, warna, dan grid (di satu sumbu)"""
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='-', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle='-', marker='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig) # Menampilkan di Streamlit

def trend_lines_plot():
    """Plot ganda dengan perbedaan linestyles untuk menunjukkan tren (di satu sumbu)"""
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A Trend', linestyle='--', color='blue')
    ax.plot(months, product_B_sales, label='Product B Trend', linestyle='-', color='red')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig) # Menampilkan di Streamlit

def subplots():
    """Plot ganda terpisah di dua sumbu vertikal"""
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot untuk Produk A
    axs[0].plot(months, product_A_sales, label='Product A', color='blue', marker='o')
    axs[0].set_title('Penjualan Produk A Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)
    
    # Plot untuk Produk B
    axs[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
    axs[1].set_title('Penjualan Produk B Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)
    
    plt.tight_layout()
    st.pyplot(fig) # Menampilkan di Streamlit

# --- LAYOUT STREAMLIT UTAMA ---
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox(
    "Pilih Tipe Visualisasi", 
    ("Line Plot", "Kustomisasi Line Plot", "Garis Berbeda untuk Menunjukkan Trend", "Subplot")
)

# Pemilihan Fungsi berdasarkan Opsi Sidebar
if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()