import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise


#sidebar menu
Tabs = {
    "Home": home,
    "Prediction" : predict,
    "Visualisation" : visualise,
}

#membuat radio option
#page = st.sidebar.radio("Pages",list(Tabs.keys()))

# Membuat tab horizontal
selected_tab = st.tabs(list(Tabs.keys()))

#load dataset
df,x,y = load_data()

# Kondisi untuk menjalankan fungsi app di setiap tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
