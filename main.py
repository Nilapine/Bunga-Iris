import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise

# CSS untuk memodifikasi posisi elemen di sidebar
def center_sidebar_menu():
    st.markdown(
        """
        <style>
        /* Memusatkan elemen sidebar */
        section[data-testid="stSidebar"] .css-ng1t4o { 
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Terapkan CSS untuk sidebar
center_sidebar_menu()

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
