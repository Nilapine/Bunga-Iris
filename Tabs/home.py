import streamlit as st
from web_functions import load_data

# Function to set background image (scrap paper motif)
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
    # Set background image (scrap paper motif)
    scrap_paper_image_url = "https://www.freepik.com/free-vector/crumpled-paper-texture_9701046.htm"  # Replace with scrap paper image URL
    set_background_image(scrap_paper_image_url)
    
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
    
    # Display iris flower images in columns (side by side) with same size
    col1, col2, col3 = st.columns(3)
    
    # Set a fixed size for all images to make them uniform
    image_width = 350  # Fixed width for each image
    image_height = 350  # Fixed height for each image
    
    with col1:
        st.image('https://images.squarespace-cdn.com/content/v1/61eeea89d60f57793d9e114b/1706854176756-Y4XKV9Q0OQ5F2C0ICPDI/iris%2Bsetosa%2B%25282%2529.jpg?format=1000w', caption="Iris Setosa", width=image_width, height=image_height)
    
    with col2:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAhHAQgQSBvRdWjZS3rp0wVvLum8zgHC0djx-rGJupnYYyKaGkMvGoQNTa3GV4FjBe8d0&usqp=CAU', caption="Iris Versicolor", width=image_width, height=image_height)
    
    with col3:
        st.image('https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg', caption="Iris Virginica", width=image_width, height=image_height)

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
