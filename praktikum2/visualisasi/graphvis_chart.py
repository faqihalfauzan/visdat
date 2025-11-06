import streamlit as st
import pandas as pd
import numpy as np

st.title("Graphviz Chart")
st.subheader("Praktikum-2 Visualisasi Data")
st.write("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota:**
1. Faizal Fandi Mulyadi - 011022084  
2. Faqih Al Fauzan - 0110222152  
3. Afnan Ainul Mardhiyyah - 0110222128
""")

st.title("Graphviz_Chart")
st.graphviz_chart("""
    digraph {
        node [shape=box, style=filled, color="#AED6F1", fontname="Arial", fontsize=12];
        edge [color="#5D6D7E"];

        "Training Data" -> "ML Algorithm";
        "ML Algorithm" -> "Model";
        "Model" -> "Results Forecasting";
        "New Data" -> "Model";
    }
""")
