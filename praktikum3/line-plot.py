import streamlit as st
import matplotlib.pyplot as plt

# membuat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Des']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# Data sample tambahan
product_C_sales = [18,21,22,23,14,55,67,53,63,55,77,88,99,98,76][:12]
product_D_sales = [31,21,33,43,32,55,36,71,12,43,88,97,64,43,76][:12]

# Layout streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", (
    "Single Line Plot",
    "Multiple & Costumizations",
    "Jenis Garis untuk Menunjukan Tren",
    "Subplot"
))

# Identitas Kelompok (Card Style)
st.subheader("Identitas Kelompok 3")
st.markdown(
    """
    <div style="
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        ">
        <h4>Nama Anggota:</h4>
        <ul>
            <li><b>Faizal Fandi Mulyadi</b> — 0110222184</li>
            <li><b>Faqih Al Fauzan</b> — 0110222152</li>
            <li><b>Afnan Ainul Marddhiyyah</b> — 0110222128</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.set_title('Penjualan Produk per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Multiple & Costumizations
def Costumimize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, linestyle='--', marker='o', linewidth=2)
    ax.plot(months, product_B_sales, linestyle='-.', marker='s', linewidth=2)
    ax.plot(months, product_C_sales, linestyle=':', marker='x', linewidth=2)
    ax.plot(months, product_D_sales, linestyle='-', marker='d', linewidth=2)
    ax.set_title("Multiple Line Plot with Custom Style")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Penjualan")
    ax.legend(["Product A", "Product B", "Product C", "Product D"])
    ax.grid(True)
    st.pyplot(fig)

# Tren Line Plot
def tren_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", linestyle="-.")
    ax.plot(months, product_B_sales, label="Product B", linestyle="dotted")
    ax.plot(months, product_C_sales, label="Product C", linestyle="--")
    ax.plot(months, product_D_sales, label="Product D", linestyle="-")
    ax.set_title("Jenis Garis untuk Menunjukan Tren")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Penjualan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Subplot
def subplots():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    # Grafik 1 (A & C)
    ax1.plot(months, product_A_sales, marker='o', label="Product A")
    ax1.plot(months, product_C_sales, marker='x', label="Product C")
    ax1.set_title("Product A & C Sales")
    ax1.grid(True)
    ax1.legend()

    # Grafik 2 (B & D)
    ax2.plot(months, product_B_sales, marker='s', label="Product B")
    ax2.plot(months, product_D_sales, marker='d', label="Product D")
    ax2.set_title("Product B & D Sales")
    ax2.grid(True)
    ax2.legend()

    st.pyplot(fig)

# Logika pemilihan menu
if option == "Single Line Plot":
    line_plot()

elif option == "Multiple & Costumizations":
    Costumimize_line_plot()

elif option == "Jenis Garis untuk Menunjukan Tren":
    tren_line_plot()

elif option == "Subplot":
    subplots()

else:
    st.write("Silakan pilih tipe visualisasi.")
