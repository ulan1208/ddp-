import streamlit as st 

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    def cetak_nama(self):
        st.write("\n\t\t ", self.nama,
            "\n\n Harga : ", self.harga,
            "\n\n Stok : ", self.stok
            ) 
               
    def tambah_stok(self, jumlah):
        self.stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
        else:
            st.warning("Stok tidak cukup untuk mengurangi.")
            
tas = Produk ("Tas", 120000, 84)
sepatu = Produk ("Sepatu", 200000, 24)
celana = Produk ("Celana", 150000, 33)      

daftar_produk = [tas, sepatu, celana]

def tampil_produk():
    st.subheader("Daftar Produk")
    for produk in daftar_produk:
        produk.cetak_nama()
 