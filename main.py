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

# Header with custom navigation menu
title_container = st.container()

# Add CSS for styling
st.markdown("""
    <style>
        /* Import Google Font for Poppins */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        /* Container for header with text and menu */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;  /* Center the content */
            padding: 20px;
            margin-bottom: 20px;  /* Space below the header */
        }

        /* Styling for the text "Iris Predict" */
        .header-text {
            font-family: 'Poppins', sans-serif;  /* Apply Poppins font */
            font-size: 24px;  /* Font size */
            font-weight: 600;  /* Bold font */
            color: #800080;  /* Purple color */
            margin-right: 50px;  /* Space between text and menu */
        }

        /* Styling for the navigation menu (no border or background) */
        .menu-item {
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: #800080;
            text-decoration: none;  /* Remove underline */
            margin-right: 30px;  /* Space between menu items */
            cursor: pointer;
        }

        /* Hover effect for menu items */
        .menu-item:hover {
            color: #5e1d99;  /* Darker purple for hover effect */
        }
    </style>
""", unsafe_allow_html=True)

# Create a container for text and menu aligned on the same line
with title_container:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    
    # Left side: "Iris Predict" text
    st.markdown('<span class="header-text">Iris Predict</span>', unsafe_allow_html=True)

    # Right side: Custom Menu Items (no border, styled text links)
    st.markdown('<a href="#" class="menu-item" id="home-link">Home</a>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="menu-item" id="prediction-link">Prediction</a>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="menu-item" id="visualisation-link">Visualisation</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Action for clicking on the menu items
home_button = st.session_state.get('home_button', False)
prediction_button = st.session_state.get('prediction_button', False)
visualisation_button = st.session_state.get('visualisation_button', False)

# Use JavaScript to trigger action when the menu items are clicked
if 'home-button' in st.session_state:
    Tabs["Home"].app(df, x, y)
elif 'prediction-button' in st.session_state:
    Tabs["Prediction"].app(df, x, y)
elif 'visualisation-button' in st.session_state:
    Tabs["Visualisation"].app(df, x, y)
