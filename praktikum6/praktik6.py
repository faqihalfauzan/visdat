import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Praktikum 6 Visualisasi Data")
st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Mardhiyyah = 0110222128
""")

stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [150, 300, 200]

# Digunakan untuk chart 2 & 3
stores_sales = ['Store A', 'Store B', 'Store C'] 
product_a = [150, 200, 180]
product_b = [150, 300, 200]

q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 216]

# 1 Grafik Stacked Vertical Bar Chart
st.subheader("1. Stacked Vertical Bar Chart")

fig1, ax1 = plt.subplots()
x1 = np.arange(len(stores))
ax1.bar(x1, male, label='Male', color='blue')
ax1.bar(x1, female, bottom=male, label='Female', color='pink')

ax1.set_title('Population by Gender and Store')
ax1.set_xlabel('Stores')
ax1.set_ylabel('Population')

ax1.set_xticks(x1)
ax1.set_xticklabels(stores)
ax1.legend()

st.pyplot(fig1)

# 2 Grafik Stacked Vertical Bar Chart dengan Matplotlib
st.subheader("2. Stacked Vertical Bar Chart dengan Matplotlib")

fig2, ax2 = plt.subplots()
x2 = np.arange(len(stores_sales))
ax2.bar(x2, product_a, label='Product A', color='blue')
# PERBAIKAN: bottom harus menggunakan product_a agar menumpuk
ax2.bar(x2, product_b, bottom=product_a, label='Product B', color='green') 

ax2.set_title('Sales Transaction by Store')
ax2.set_xlabel('Stores')
ax2.set_ylabel('Sales')

ax2.set_xticks(x2)
ax2.set_xticklabels(stores_sales)
ax2.legend()

st.pyplot(fig2)

# 3 Grafik Kustomisasi Stacked Vertical Bar Chart
st.subheader("3. Kustomisasi Stacked Vertical Bar Chart")

# Menggunakan fig2 yang sudah dibuat untuk menambahkan teks
for i in range(len(x2)) :
    ax2.text(x2[i], product_a[i]/2, str(product_a[i]), ha='center', color='black')
    ax2.text(x2[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='red')
st.pyplot(fig2)

# 4 Grafik Multiple Stacked Vertical Bar Chart
st.subheader("4. Multiple Stacked Vertical Bar Chart")

fig4, ax4 = plt.subplots()
width = 0.4
x4 = np.arange(len(stores))

# Quarter 1 (Stacked, digeser ke kiri)
ax4.bar(x4 - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax4.bar(x4 - width/2, q1_female, bottom=q1_male, label='Q1 Female', color='red', width=width)

# Quarter 2 (Stacked, digeser ke kanan)
# PERBAIKAN: Menggunakan x4 + width/2 untuk menggeser Q2, dan Q2 Female bertumpu pada Q2 Male
ax4.bar(x4 + width/2, q2_male, label='Q2 Male', color='lightpink', width=width)
ax4.bar(x4 + width/2, q2_female, bottom=q2_male, label='Q2 Female', color='orange', width=width)

ax4.set_title('Population by Gender and Store (Multiple Quarters)')
ax4.set_xlabel('Stores')
ax4.set_ylabel('Population')
ax4.set_xticks(x4)
ax4.set_xticklabels(stores)
ax4.legend()

st.pyplot(fig4)