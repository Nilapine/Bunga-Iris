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

# Header with logo and menu
title_container = st.container()

# Add CSS for styling
st.markdown("""
    <style>
        /* Container for logo and menu aligned horizontally */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;  /* Space below the header */
        }
        .header-logo {
            margin-right: 20px;  /* Space between logo and menu */
        }
        div[role='tablist'] {
            display: flex;
            justify-content: center;
        }
        div[role='tablist'] > div {
            margin-right: 20px;  /* Space between individual tabs */
        }
    </style>
""", unsafe_allow_html=True)

# Create a container for logo and tabs in one header
with title_container:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown('<div class="header-logo">', unsafe_allow_html=True)
    st.image("https://png.pngtree.com/png-vector/20240528/ourmid/pngtree-blue-and-purple-iris-flower-png-image_12520393.png", width=100)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add the tabs below the image, in the same header section
    selected_tab = st.tabs(list(Tabs.keys()))
    st.markdown('</div>', unsafe_allow_html=True)
    
# Kondisi untuk menjalankan fungsi app di setiap tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
