import pandas as pd

print("=== AI Agent Pembelian Handphone ===")

# Baca data
data = pd.read_csv("data_hp.csv")

# Input dari pengguna
budget = int(input("Masukkan budget (Rp): "))

# Logika AI Agent
rekomendasi = data[data["harga"] <= budget]

# Hasil
print("\nRekomendasi Handphone:")
if rekomendasi.empty:
    print("Tidak ada handphone sesuai budget.")
else:
    print(rekomendasi)
