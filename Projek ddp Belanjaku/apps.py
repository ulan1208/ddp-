import streamlit as st
from produk import *
from cost import *
from diskon import *
from stok import *

st.header("Selamat Datang di Aplikasi Belanjaku!")
st.sidebar.title("Belanjaku")
st.snow()

# Pilihan menu di sidebar
menu = st.sidebar.selectbox("Pilih Halaman", ("Daftar Produk", "Menambahkan Diskon", "Input Costumer", "Manajemen Stok"))

# Menampilkan konten dari pilihan menu
if menu == "Daftar Produk":
    tampil_produk()

if menu == "Input Costumer":
    tampil_costumer()

if menu == "Menambahkan Diskon":
    tampil_diskon()

if menu == "Manajemen Stok":
    manajemen_stok()