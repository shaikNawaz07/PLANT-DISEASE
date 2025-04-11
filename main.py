import streamlit as st

#Sidebar
st.sidebar.title("FarmCure")
app_mode = st.sidebar.selectbox("Select Page",["HOME","DISEASE RECOGNITION"])
#app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

# import Image from pillow to open images
