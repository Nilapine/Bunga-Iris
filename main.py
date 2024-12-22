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

# Header with logo and title
title_container = st.container()
st.markdown("""
    <style>
        /* Align the logo and title to the center */
        .header-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;  /* Space below the header */
        }
        .header-logo {
            margin-right: 10px;  /* Space between logo and title */
        }
        div[role='tablist'] {
            justify-content: center;
            margin-bottom: 30px;  /* Increase spacing between tabs */
        }
        div[role='tablist'] > div {
            margin-right: 20px;  /* Increase space between individual tabs */
        }
    </style>
""", unsafe_allow_html=True)

# Container for header
with title_container:
    # Create a container to center align the logo and title
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown('<div class="header-logo">', unsafe_allow_html=True)
    st.image("https://png.pngtree.com/png-vector/20240528/ourmid/pngtree-blue-and-purple-iris-flower-png-image_12520393.png", width=100)
    st.markdown('</div>', unsafe_allow_html=True)

# Create tabs for page navigation
selected_tab = st.tabs(list(Tabs.keys()))

# Run the app functionality for each selected tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
