import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise


st.markdown(f"""
<style>
    Tabs{{
        onsubmit: "streamlit.button.click()";
    }}
    .navbar{{
        padding-right: 10px;
        padding-left: 30px;
    }}
    .navbar-brand img{{
        max-height: 50px;
    }}
</style>
<Tabs action="">
    <nav class="navbar">
        <a class="navbar-brand" href="#"></a>
    </nav>
</Tabs>

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
