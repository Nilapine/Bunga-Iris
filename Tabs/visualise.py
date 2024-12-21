import warnings
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
from sklearn import tree
import streamlit as st
import numpy as np
import pandas as pd
import os

from web_functions import train_model_DT,train_model_KNN,train_model_NBC,load_data

def app(df, x, y):
    warnings.filterwarnings('ignore')
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualisasi Prediksi Tanaman Iris")


    # if st.checkbox("Plot Decision Tree"):
    #     model,score = train_model_DT(x,y)
    #     dot_data = tree.export_graphviz(
    #         decision_tree=model, out_file=None, filled=True, rounded=True,
    #         feature_names=x.columns, class_names=['Iris-setosa','Iris-versicolor','Iris-virginica']
    #     )
    #     st.graphviz_chart(dot_data)
    # elif st.checkbox("Pairplot"):
    st.title("Pairplot")
    # s = sns.pairplot(df, hue="Species")
    st.pyplot(sns.pairplot(df, hue="Species")) # type: ignore
    st.subheader("Penjelasan Pair Plot")
    st.markdown("""
    Gambar di atas adalah *pair plot*, yang merupakan visualisasi dari hubungan antar variabel pada dataset *Iris*. Berikut adalah penjelasan lebih lanjut:

    1. **Dataset Iris**: Dataset ini terdiri dari tiga spesies bunga Iris—*Iris-setosa* (biru), *Iris-versicolor* (oranye), dan *Iris-virginica* (hijau)—yang diklasifikasikan berdasarkan empat fitur:
      - **SepalLengthCm**: Panjang kelopak bunga (sepal) dalam cm.
      - **SepalWidthCm**: Lebar kelopak bunga dalam cm.
      - **PetalLengthCm**: Panjang mahkota bunga (petal) dalam cm.
      - **PetalWidthCm**: Lebar mahkota bunga dalam cm.
      - **Id**: Indeks untuk identifikasi.

    2. **Distribusi diagonal**: Di sepanjang diagonal, terlihat distribusi (plot densitas atau histogram) dari masing-masing fitur secara individu. Warna-warna pada distribusi ini mewakili spesies yang berbeda.

    3. **Scatter plot non-diagonal**: Di bagian lain dari pair plot ini, terlihat plot pencar (scatter plot) yang menunjukkan hubungan antara dua fitur. Setiap titik pada scatter plot mewakili satu contoh dari dataset, dengan warnanya mencerminkan spesiesnya. 

    4. **Klasifikasi visual**: Gambar ini memberikan indikasi seberapa mudah atau sulit spesies bunga dapat diklasifikasikan berdasarkan fitur tertentu. Beberapa pasangan fitur memperlihatkan pemisahan yang lebih jelas antar spesies, sedangkan beberapa pasangan lainnya menunjukkan tumpang tindih yang lebih besar.
    """)

    # Menambahkan bagian untuk menampilkan gambar dari direktori
    st.subheader("Tampilkan Gambar dari Direktori")
    
    # Path gambar yang ingin ditampilkan
    image_path = 'media/virginica.jpg'  # Ganti dengan path gambar yang diinginkan
    
    if os.path.exists(image_path):
        # Jika file gambar ada, tampilkan gambar
        st.image(img, caption="Iris Virginica", use_column_width=True)
        
        # Menampilkan penjelasan gambar di bawah gambar
        st.markdown("""
        Gambar di atas adalah bunga Iris *Iris-virginica*, yang merupakan salah satu spesies bunga Iris dalam dataset.
        Bunga ini memiliki ciri khas seperti kelopak bunga yang lebih besar dan lebih lebar dibandingkan dengan spesies lainnya.
        """)

        
        
        
