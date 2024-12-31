import streamlit as st
from produk import tampil_produk, daftar_produk

def manajemen_stok():
    st.title("Manajemen Stok Produk")

    tampil_produk()

    produk_nama = [produk.nama for produk in daftar_produk]
    produk_terpilih = st.selectbox("Pilih Produk", produk_nama)

    produk_dipilih = next(produk for produk in daftar_produk if produk.nama == produk_terpilih)

    jumlah_tambah = st.number_input("Jumlah stok yang ingin ditambahkan", min_value=0, value=0)
    if st.button("Tambah Stok"):
        produk_dipilih.tambah_stok(jumlah_tambah)
        st.success(f"Stok {produk_dipilih.nama} berhasil ditambahkan. Stok sekarang: {produk_dipilih.stok}")

    jumlah_kurang = st.number_input("Jumlah stok yang ingin dikurangi", min_value=0, value=0)
    if st.button("Kurangi Stok"):
        produk_dipilih.kurangi_stok(jumlah_kurang)
        st.success(f"Stok {produk_dipilih.nama} berhasil dikurangi. Stok sekarang: {produk_dipilih.stok}")

    # Menampilkan stok terbaru
    st.subheader("Stok Terbaru")
    for produk in daftar_produk:
        st.write(f"{produk.nama}: {produk.stok}")
