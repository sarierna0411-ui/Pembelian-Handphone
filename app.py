import pandas as pd

# Judul aplikasi
print("=== AI Agent Pembelian Handphone ===")

# Membaca data pembelian HP
data = pd.read_csv("data_hp.csv")

# Menampilkan data
print("\nData Pembelian Handphone:")
print(data)
