import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise

# Sidebar menu
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise,
}

# Load dataset
df, x, y = load_data()

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
            margin-bottom: 1px;  /* Space below the header */
        }
        .header-logo {
            margin-right: 1px;  /* Space between logo and menu */
        }
        div[role='tablist'] {
            display: flex;
            justify-content: center;
        }
        div[role='tablist'] > div {
            margin-right: 50px;  /* Space between individual tabs */
        }
    </style>
""", unsafe_allow_html=True)
    
    # Add the tabs below the image, in the same header section
    selected_tab = st.tabs(list(Tabs.keys()))
    st.markdown('</div>', unsafe_allow_html=True)

# Run the app functionality for each selected tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
