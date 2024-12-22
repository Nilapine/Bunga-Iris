import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise

#sidebar menu
Tabs = {
    "Home": home,
    "Prediction" : predict,
    "Visualisation" : visualise,
}

#load dataset
df,x,y = load_data()

# Header dengan logo dan judul
title_container = st.container()
col1, col2 = title_container.columns([1, 5])
with col1:
    st.image("https://png.pngtree.com/png-vector/20240528/ourmid/pngtree-blue-and-purple-iris-flower-png-image_12520393.png", width=100)
with col2:
    st.markdown("<h1 style='text-align: right;'></h1>", unsafe_allow_html=True)  # Title aligned right
    selected_tab = st.tabs(list(Tabs.keys())) # Tabs are now within the second column

# Kondisi untuk menjalankan fungsi app di setiap tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
