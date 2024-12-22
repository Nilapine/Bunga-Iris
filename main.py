import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise


#load dataset
df,x,y = load_data()

# Header dengan logo dan judul
title_container = st.container()
col1, col2 = title_container.columns([1, 5])
with col1:
    st.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png", width=100)
with col2:
    selected_tab = st.tabs(list(Tabs.keys())) # Tabs are now within the second column

#sidebar menu
Tabs = {
    "Home": home,
    "Prediction" : predict,
    "Visualisation" : visualise,
}

# Membuat tab horizontal
selected_tab = st.tabs(list(Tabs.keys()))

# Kondisi untuk menjalankan fungsi app di setiap tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
