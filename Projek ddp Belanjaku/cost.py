import streamlit as st 

def tampil_costumer():
    if "Costu" not in st.session_state:
        st.session_state["Costu"] = []

    with st.form("Costumer"):
        nama = st.text_input("Masukkan Nama: ")
        umur = st.number_input("Masukkan Umur Anda: ", min_value=0)  # Menambahkan min_value untuk validasi
        alamat = st.text_area("Masukkan Alamat Anda: ")
        submit = st.form_submit_button("Simpan")
    
        if submit:
            st.session_state["Costu"].append({
                "Nama": nama,
                "Umur": umur,
                "Alamat" : alamat,
            })
            st.success("Berhasil Menambahkan")

# Menampilkan semua data yang ada di session state
    st.write("Data Costumer: ")
    for session in st.session_state["Costu"]:
        st.write(f"Nama: {session['Nama']}, \n\nUmur: {session['Umur']}, \n\nAlamat: {session['Alamat']}")

