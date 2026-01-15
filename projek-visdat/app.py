import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import os
import numpy as np
from collections import Counter

# =========================
# 1. KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Instagram Analytics Pro",
    page_icon="📸",
    layout="wide"
)

# Custom CSS untuk Estetika Premium
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    
    /* Sidebar Gradient ala Instagram */
    [data-testid="stSidebar"] {
        background-image: linear-gradient(#405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color: white;
    }
    
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: white !important;
    }

    /* Styling Kartu Metrik */
    div[data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-left: 6px solid #C13584;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] {
        height: 45px; background-color: white; border-radius: 10px;
        padding: 10px 25px; font-weight: bold; color: #C13584; border: 1px solid #eee;
    }
    .stTabs [aria-selected="true"] {
        background-image: linear-gradient(to right, #833AB4, #E1306C) !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================
# 2. LOAD DATA
# =========================
@st.cache_data
def load_data():
    file_path = "instagram_reviews.csv"
    if not os.path.exists(file_path): return None
    try:
        df = pd.read_csv(file_path, encoding="utf-8")
    except:
        df = pd.read_csv(file_path, encoding="latin1")
    
    df.columns = df.columns.str.strip()
    if "Review Text" in df.columns: df = df.rename(columns={"Review Text": "review"})
    if "Rating" in df.columns: df = df.rename(columns={"Rating": "rating"})
    
    def label_sentiment(r):
        if r >= 4: return "Positif"
        elif r == 3: return "Netral"
        else: return "Negatif"
    df["sentiment"] = df["rating"].apply(label_sentiment)
    return df

df = load_data()
if df is None:
    st.error("File 'instagram_reviews.csv' tidak ditemukan!")
    st.stop()

df = df.dropna(subset=["review", "rating"])
df["review_length"] = df["review"].astype(str).apply(len)

# =========================
# 3. SIDEBAR (LOGO, FILTER & IDENTITAS)
# =========================
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>📸 ANALYTICS</h1>", unsafe_allow_html=True)
    st.divider()
    
    # 1. Filter Data (Sekarang di Atas)
    st.subheader("⚙️ Filter Data")
    sentimen_pilihan = st.multiselect(
        "Pilih Sentimen:",
        options=df["sentiment"].unique(),
        default=df["sentiment"].unique()
    )
    st.divider()

    # 2. Identitas Kelompok (Sekarang di Bawah Filter)
    st.markdown("### 👥 Kelompok Visualisasi")
    st.markdown("""
    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.3); backdrop-filter: blur(5px);">
    <p style='margin-bottom: 10px;'><b>1. Faizal Fandi Mulyadi</b><br><small>011022084</small></p>
    <p style='margin-bottom: 10px;'><b>2. Faqih Al Fauzan</b><br><small>0110222152</small></p>
    <p style='margin-bottom: 0px;'><b>3. Afnan Ainul Mardhiyyah</b><br><small>0110222128</small></p>
    </div>
    """, unsafe_allow_html=True)

filtered_df = df[df["sentiment"].isin(sentimen_pilihan)]

# =========================
# 4. HEADER & METRIK
# =========================
st.markdown("<h1 style='color: #262626;'>Dashboard Insight Instagram Indonesia</h1>", unsafe_allow_html=True)
st.write("Eksplorasi hierarki ulasan dan analisis teks mendalam.")

m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Total Ulasan", f"{len(filtered_df):,}")
with m2: st.metric("Avg Rating", f"{filtered_df['rating'].mean():.2f} ⭐")
with m3: st.metric("Max Karakter", f"{filtered_df['review_length'].max()}")
with m4: 
    pos_rate = (len(filtered_df[filtered_df['sentiment']=='Positif']) / len(filtered_df) * 100) if len(filtered_df)>0 else 0
    st.metric("Satisfaction Rate", f"{pos_rate:.1f}%")

st.write("")

# =========================
# 5. VISUALISASI UTAMA (TABS)
# =========================
tab1, tab2, tab3 = st.tabs(["📊 Tren & Hierarki", "📏 Kedalaman Teks", "☁️ Analisis Kata"])

insta_colors = {"Positif": "#C13584", "Netral": "#95a5a6", "Negatif": "#262626"}

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Volume Sentimen")
        fig_bar = px.histogram(filtered_df, x="sentiment", color="sentiment", 
                               color_discrete_map=insta_colors, template="plotly_white")
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        st.subheader("Hierarki Sentimen vs Rating")
        # NEW VISUAL 1: Sunburst Chart
        fig_sun = px.sunburst(filtered_df, path=['sentiment', 'rating'], 
                              color='sentiment', color_discrete_map=insta_colors)
        st.plotly_chart(fig_sun, use_container_width=True)

with tab2:
    c3, c4 = st.columns(2)
    with c3:
        st.subheader("Distribusi Karakter (Box Plot)")
        fig_box = px.box(filtered_df, x="sentiment", y="review_length", color="sentiment",
                         color_discrete_map=insta_colors, template="plotly_white")
        st.plotly_chart(fig_box, use_container_width=True)
    with c4:
        st.subheader("Sebaran Panjang Teks per Rating")
        # NEW VISUAL 3: Strip Plot
        fig_strip = px.strip(filtered_df, x="rating", y="review_length", color="sentiment",
                             color_discrete_map=insta_colors, stripmode='overlay')
        st.plotly_chart(fig_strip, use_container_width=True)

with tab3:
    c5, c6 = st.columns([1, 1.2])
    
    # Pre-processing untuk Bar Chart Kata
    stop_words = ["yang", "dan", "di", "ini", "itu", "saya", "ada", "sudah", "ke", "ga", "tapi", "aplikasi", "ig", "instagram", "untuk", "aja", "bisa", "gak"]
    all_words = " ".join(filtered_df["review"].astype(str)).lower().split()
    clean_words = [w for w in all_words if w not in stop_words and len(w) > 2]
    word_freq = Counter(clean_words).most_common(15)
    word_df = pd.DataFrame(word_freq, columns=['Kata', 'Frekuensi'])

    with c5:
        st.subheader("Top 15 Kata Kunci")
        # NEW VISUAL 2: Bar Chart Frekuensi Kata
        fig_word = px.bar(word_df, x='Frekuensi', y='Kata', orientation='h', 
                          color='Frekuensi', color_continuous_scale='magma')
        fig_word.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_word, use_container_width=True)

    with c6:
        st.subheader("Awan Kata (Visual)")
        text = " ".join(filtered_df["review"].astype(str))
        if len(text) > 10:
            wc = WordCloud(width=800, height=500, background_color="white", 
                           stopwords=set(stop_words), colormap="magma").generate(text)
            wc_array = np.array(wc.to_image())
            fig_wc, ax = plt.subplots()
            ax.imshow(wc_array, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig_wc)

# =========================
# 6. TABLE DETAIL
# =========================
st.divider()
with st.expander("📄 Lihat Sampel Data Ulasan"):
    st.dataframe(filtered_df[["UserName", "rating", "sentiment", "review"]].head(50), use_container_width=True)

st.markdown("<p style='text-align: center; color: #999;'>STT Terpadu Nurul Fikri - Projek Visdat 2026</p>", unsafe_allow_html=True)