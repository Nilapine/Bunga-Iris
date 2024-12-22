import streamlit as st
from web_functions import load_data

# CSS untuk memodifikasi posisi elemen di sidebar
def center_sidebar_menu():
    st.markdown(
        """
        <style>
        /* Memusatkan elemen sidebar */
        section[data-testid="stSidebar"] .css-ng1t4o { 
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Terapkan CSS untuk sidebar
center_sidebar_menu()

def app(df,x,y):
    # Judul Halaman Aplikasi
    st.title("Aplikasi Prediksi Jenis Tanaman Iris")
    df.drop('Id',axis=1)
    st.write(df)
    
