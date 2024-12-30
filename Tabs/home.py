import streamlit as st
from web_functions import load_data

def app(df, x, y):
    # Add a large horizontal image of the Iris flower at the bottom of the page
    st.image(
        'https://asset.kompas.com/crops/pBgd0CVrw5satlJj1P_ud_0EAoM=/0x0:1000x667/1200x800/data/photo/2022/10/30/635db6ae22aa4.jpg',
        caption="Iris Flower - Horizontal",
        use_column_width=True  # Make the image stretch across the full width of the page
    )

    # Center the content and add padding
    st.markdown(
        """
        <style>
        .stApp {
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add a title for the application
    st.title("Aplikasi Prediksi Jenis Tanaman Iris")

    # Display iris flower images in columns (side by side) with uniform sizes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('https://images.squarespace-cdn.com/content/v1/61eeea89d60f57793d9e114b/1706854176756-Y4XKV9Q0OQ5F2C0ICPDI/iris%2Bsetosa%2B%25282%2529.jpg?format=1000w', caption="Iris Setosa", use_column_width=True)

    with col2:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAhHAQgQSBvRdWjZS3rp0wVvLum8zgHC0djx-rGJupnYYyKaGkMvGoQNTa3GV4FjBe8d0&usqp=CAU', caption="Iris Versicolor", use_column_width=True)

    with col3:
        st.image('https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg', caption="Iris Virginica", use_column_width=True)

    # Add description about the iris flowers
    st.subheader("Deskripsi Bunga Iris")
    st.write("""
        Bunga Iris adalah tanaman berbunga yang dikenal karena keindahannya.
        Iris memiliki berbagai warna seperti ungu, biru, putih, dan kuning. 
        Tanaman ini tumbuh dengan daun sempit panjang dan bunga yang memiliki tiga kelopak.
        Iris sering ditemukan di habitat basah seperti rawa dan tepi danau.
    """)

    # Show the dataset (without the 'Id' column)
    if 'Id' in df.columns:
        df = df.drop('Id', axis=1)
    st.write(df)
