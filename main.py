import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise
from streamlit_navigation_bar import st_navbar
import pages as pg

# *** IMPORTED NAVIGATION BAR
st.set_page_config(initial_sidebar_state="collapsed")
pages = ["Home", "Prediction", "Visualisation"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(
    parent_dir, "https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg")
styles = {
    "nav": {
        "background-color": "#5D7298",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
        "width": "150px",
        "height": "150px"

    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "#A6B2C9",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

Tabs = st_navbar(
    pages,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

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
