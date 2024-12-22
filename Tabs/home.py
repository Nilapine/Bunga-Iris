import streamlit as st
from web_functions import load_data

# Function to set background image
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def app(df, x, y):
    # Set background image (flower image)
    background_image_url = "https://images.squarespace-cdn.com/content/v1/61eeea89d60f57793d9e114b/1706854176756-Y4XKV9Q0OQ5F2C0ICPDI/iris%2Bsetosa%2B%25282%2529.jpg?format=1000w"  # Replace with actual image URL
    set_background_image(background_image_url)
    
    # Center the button on the page
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            padding: 15px 32px;
            text-align: center;
            display: block;
            margin: 0 auto;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Add a title for the application
    st.title("Aplikasi Prediksi Jenis Tanaman Iris")
    
    # Show the "Start" button to move to the prediction page
    if st.button("Start"):
        # Transition to the prediction page
        st.subheader("Prediksi Jenis Tanaman Iris")
        
        # Display iris flower images in columns (side by side)
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
    df.drop('Id', axis=1, inplace=True)
    st.write(df)
