import streamlit as st

from web_functions import predict_DT,predict_KNN,predict_NBC

def app(df, x, y):
    # Judul Halaman Aplikasi
    st.title("Halaman Prediksi Jenis Tanaman Iris")

    col1, col2 = st.columns(2)

    with col1:
        SepalLengthCm = st.text_input('Input Panjang Sepal (dalam cm) : ')
    with col1:
        SepalWidthCm = st.text_input('Input Lebar Sepal (dalam cm) : ')
    with col2:
        PetalLengthCm = st.text_input('Input Panjang Petal (dalam cm) : ')
    with col2:
        PetalWidthCm = st.text_input('Input Lebar Petal (dalam cm) : ')
    
    features = [SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]
    
    tipe_model = {
        "KNN": predict_KNN,
        "NBC" : predict_NBC,
    }
    
    predict = st.radio(label="Pilih Model ",options=["KNN","NBC"])

    #Tombol Prediksi
    if st.button("Prediksi"):
        if predict == "KNN":
            prediction, score = predict_KNN(x,y,features) # type: ignore
            score = score
            st.info("Prediksi Sukses....")

            if(prediction == "Iris-setosa"):
                st.success("Termasuk kedalam Iris jenis Setosa")
            elif(prediction == "Iris-versicolor"):
                st.success("Termasuk kedalam Iris jenis Versi Color")
            elif(prediction == "Iris-virginica"):
                st.success("Termasuk kedalam Iris jenis Virginica")

            st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")
        # elif predict == "DT":
        #     prediction, score = predict_DT(x,y,features) # type: ignore
        #     score = score
        #     st.info("Prediksi Sukses....")

        #     if(prediction == "Iris-setosa"):
        #         st.success("Termasuk kedalam Iris jenis Setosa")
        #     elif(prediction == "Iris-versicolor"):
        #         st.success("Termasuk kedalam Iris jenis Versi Color")
        #     elif(prediction == "Iris-virginica"):
        #         st.success("Termasuk kedalam Iris jenis Virginica")

        #     st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")
        else:
            prediction, score = predict_NBC(x,y,features) # type: ignore
            score = score
            st.info("Prediksi Sukses....")

        if prediction == "Iris-setosa":
            st.success("Termasuk kedalam Iris jenis Setosa")
            st.image("https://cdn.popmama.com/content-images/community/20230530/community-0ffa74b95b5ebdb3eca2a0e6e6573e0b.png?1685458076", caption="Iris-setosa", use_column_width=True)
        elif prediction == "Iris-versicolor":
            st.success("Termasuk kedalam Iris jenis Versicolor")
            st.image("https://cdn.popmama.com/content-images/community/20230530/community-14ba4def1a1a159e46112067b7f801f5.png?1685458076", caption="Iris-versicolor", use_column_width=True)
        elif prediction == "Iris-virginica":
            st.success("Termasuk kedalam Iris jenis Virginica")
            st.image("https://cdn.popmama.com/content-images/community/20230530/community-58bdaacae45cf8668bd65cd7a028b123.png?1685458076", caption="Iris-virginica", use_column_width=True)


            st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")
