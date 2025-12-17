import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Agent Handphone", layout="wide")

st.title("🤖 AI Agent Pembelian Handphone")

# Baca data
data = pd.read_csv("data_hp.csv")

# ======================
# DASHBOARD RINGKAS
# ======================
st.subheader("📈 Dashboard Ringkas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Handphone", len(data))

with col2:
    st.metric("Harga Termurah", f"Rp {data['harga'].min():,}")

with col3:
    st.metric("Harga Termahal", f"Rp {data['harga'].max():,}")

# ======================
# GRAFIK
# ======================
st.subheader("📊 Grafik Harga Handphone")
st.bar_chart(data.set_index("model")["harga"])

# ======================
# DATA TABEL
# ======================
st.subheader("📋 Data Handphone")
st.dataframe(data)

# ======================
# AI AGENT REKOMENDASI
# ======================
st.subheader("🔍 Cari Rekomendasi Handphone")

budget = st.number_input(
    "Masukkan Budget (Rp)",
    min_value=1000000,
    step=500000
)

if st.button("Cari Rekomendasi"):
    hasil = data[data["harga"] <= budget]

    if hasil.empty:
        st.error("❌ Tidak ada handphone sesuai budget.")
    else:
        st.success("✅ Rekomendasi Handphone:")
        st.dataframe(hasil)
