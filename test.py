import streamlit as st

st.title("contoh program streamlit")
with st.form(key="my_form"):
    nama = st.text_input("nama lengkap")
    jenis_kelamin = st.radio("Jenis kelamin",("Laki-Laki", "perempuan"))
    submit = st.form_submit_button(label="kirim")