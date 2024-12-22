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
# Header with text and menu
title_container = st.container()

# Add CSS for styling
st.markdown("""
    <style>
        /* Import Google Font for Poppins */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        /* Container for logo and menu aligned horizontally */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background-color: #f9f9f9;  /* Light background color */
        }

        /* Styling for text */
        .header-text {
            font-family: 'Poppins', sans-serif;  /* Apply Poppins font */
            font-size: 24px;  /* Font size */
            font-weight: 600;  /* Bold font */
            color: #800080;  /* Purple color */
        }
        
        /* Styling for menu items */
        div[role='tablist'] {
            display: flex;
            justify-content: flex-end;  /* Align menu items to the right */
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
        }

        div[role='tablist'] > div {
            color: #800080;  /* Purple color */
            font-size: 16px;
            padding: 12px 20px;  /* Padding for menu items */
            cursor: pointer;
        }

        /* Active tab styling */
        div[role='tablist'] > div[aria-selected='true'] {
            color: #5e1d99;  /* Darker purple for active tab */
            font-weight: 700;  /* Bold active tab */
        }
    </style>
""", unsafe_allow_html=True)

# Create a container for text on the left, and menu on the right
with title_container:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    
    # Left side: "Iris Predict" text
    st.markdown('<span class="header-text">Iris Predict</span>', unsafe_allow_html=True)

    # Right side: Menu
    selected_tab = st.tabs(list(Tabs.keys()))

    st.markdown('</div>', unsafe_allow_html=True)
    
# Kondisi untuk menjalankan fungsi app di setiap tab
for i, tab in enumerate(selected_tab):
    with tab:
        page_name = list(Tabs.keys())[i]
        Tabs[page_name].app(df, x, y)
