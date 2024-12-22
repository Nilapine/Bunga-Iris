import streamlit as st
from web_functions import load_data


from Tabs import home, predict, visualise

#sidebar menu
with st.sidebar:
    selected = option_menu (
        menu_title="Main Menu",
        options=["Home": home,"Prediction" : predict, "Visualisation" : visualise,],
        default_index=0,
    )
"""
#horizontal menu
Tabs = {
    "Home": home,
    "Prediction" : predict,
    "Visualisation" : visualise,
}
"""

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
