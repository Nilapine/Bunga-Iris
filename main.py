import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise

# CSS untuk memposisikan sidebar menu di tengah
def sidebar_center_style():
    st.markdown(
        """
        <style>
        /* Mengatur posisi sidebar menu */
        .block-container {
            padding-top: 2rem;
        }
        .css-1y4p8pa {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Terapkan CSS untuk sidebar
sidebar_center_style()

#sidebar menu

Tabs = {
    "Home": home,
    "Prediction" : predict,
    "Visualisation" : visualise,
}

#membuat sidebar
st.sidebar.title("Navigasi")

#membuat radio option
page = st.sidebar.radio("Pages",list(Tabs.keys()))


#load dataset
df,x,y = load_data()
#kondisi call app function
if page in ["Prediction","Visualisation"]:
    Tabs[page].app(df,x,y)
else:
    Tabs[page].app(df,x,y) # type: ignore
