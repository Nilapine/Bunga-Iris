import streamlit as st
from web_functions import load_data

def app(df, x, y):
    # Judul Halaman Aplikasi
    st.title("Aplikasi Prediksi Jenis Tanaman Iris")
    
    # Menambahkan Button Start
    if st.button("Start"):
        # Menu Prediction
        st.subheader("Prediksi Jenis Tanaman Iris")
        # Add any prediction logic here if needed
        
        # Gambar Bunga Iris
        st.image([
            'https://images.squarespace-cdn.com/content/v1/61eeea89d60f57793d9e114b/1706854176756-Y4XKV9Q0OQ5F2C0ICPDI/iris%2Bsetosa%2B%25282%2529.jpg?format=1000w',  # Replace with the actual image URL
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAhHAQgQSBvRdWjZS3rp0wVvLum8zgHC0djx-rGJupnYYyKaGkMvGoQNTa3GV4FjBe8d0&usqp=CAU',  # Replace with the actual image URL
            'https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg'   # Replace with the actual image URL
        ], caption=["Iris Setosa", "Iris Versicolor", "Iris Virginica"], use_column_width=True)
        
        # Deskripsi tentang Bunga Iris
        st.subheader("Deskripsi Bunga Iris")
        st.write("""
            Bunga Iris adalah tanaman berbunga yang dikenal karena keindahannya.
            Iris memiliki berbagai warna seperti ungu, biru, putih, dan kuning. 
            Tanaman ini tumbuh dengan daun sempit panjang dan bunga yang memiliki tiga kelopak.
            Iris sering ditemukan di habitat basah seperti rawa dan tepi danau.
        """)
    
    # Menampilkan Data Tanaman
    df.drop('Id', axis=1)
    st.write(df)

