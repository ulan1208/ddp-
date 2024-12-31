import streamlit as st 
from produk import *

def tampil_diskon():
    st.title("Hitung Diskon Produk")

    tampil_produk()

    produk_nama = [produk.nama for produk in daftar_produk]
    produk_terpilih = st.selectbox("Pilih Produk", produk_nama)

    produk_dipilih = next(produk for produk in daftar_produk if produk.nama == produk_terpilih)

    diskon = st.number_input("Masukkan persentase diskon (%)", min_value=0, max_value=100, value=0)

    # Menghitung total harga setelah diskon
    total_harga_setelah_diskon = produk_dipilih.harga * (1 - (diskon / 100))

    st.write(f"Harga asli: Rp {produk_dipilih.harga:.2f}")
    st.write(f"Diskon: {diskon}%")
    st.write(f"Total harga setelah diskon: Rp {total_harga_setelah_diskon:.2f}")

