import streamlit as st
import pandas as pd

st.title("🤖 AI Agent Pembelian Handphone")

# Baca data
data = pd.read_csv("data_hp.csv")

st.subheader("📊 Data Handphone")
st.dataframe(data)

st.subheader("🔍 Cari Rekomendasi")

# Input pengguna (GANTI input() → st.)
budget = st.number_input(
    "Masukkan budget (Rp)",
    min_value=1000000,
    step=500000
)

# Tombol proses
if st.button("Cari Rekomendasi"):
    rekomendasi = data[data["harga"] <= budget]

    if rekomendasi.empty:
        st.warning("❌ Tidak ada handphone sesuai budget.")
    else:
        st.success("✅ Rekomendasi Handphone:")
        st.dataframe(rekomendasi)
