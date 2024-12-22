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

        /* Styling for menu items */
        .menu-button {
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: #800080;
            padding: 10px 20px;
            cursor: pointer;
            border: 2px solid #800080;
            background-color: transparent;
            margin-right: 20px;
            border-radius: 5px;
        }

        .menu-button:hover {
            background-color: #800080;
            color: white;
        }

        /* Active button styling */
        .active-button {
            background-color: #800080;
            color: white;
            font-weight: 700;
        }
    </style>
""", unsafe_allow_html=True)

# Create a container for text and menu aligned on the same line
with title_container:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    
    # Left side: "Iris Predict" text
    st.markdown('<span class="header-text">Iris Predict</span>', unsafe_allow_html=True)

    # Right side: Custom Menu Buttons
    # Create buttons to switch between pages
    home_button = st.button("Home", key="home", help="Go to the Home page")
    prediction_button = st.button("Prediction", key="prediction", help="Go to the Prediction page")
    visualisation_button = st.button("Visualisation", key="visualisation", help="Go to the Visualisation page")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Action for menu buttons
if home_button:
    Tabs["Home"].app(df, x, y)
elif prediction_button:
    Tabs["Prediction"].app(df, x, y)
elif visualisation_button:
    Tabs["Visualisation"].app(df, x, y)
