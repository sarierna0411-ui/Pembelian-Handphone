st.subheader("📈 Dashboard Ringkas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Handphone", len(data))

with col2:
    st.metric("Harga Termurah", f"Rp {data['harga'].min():,}")

with col3:
    st.metric("Harga Termahal", f"Rp {data['harga'].max():,}")
