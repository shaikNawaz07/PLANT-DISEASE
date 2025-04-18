import streamlit as st
from PIL import Image

# Load an image to display at the top of the title
top_image = "top_image.jpg"  # Replace with the path to your image file

# Apply CSS styles for centering elements
center_style = """
    <style>
        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    </style>
"""
st.markdown(center_style, unsafe_allow_html=True)

# Create a container for centered elements
st.markdown('<div class="centered">', unsafe_allow_html=True)

# Display the top image
st.image(top_image, caption="Plant Disease Detection", use_column_width=False)

# Title of the app
st.title("Plant Disease Detection App")

# Subtitle
st.subheader("Upload an image to detect plant diseases!")

# Close the container
st.markdown('</div>', unsafe_allow_html=True)

# File uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Process the uploaded file
if uploaded_file is not None:
    try:
        # Open and display the image
        img = Image.open(uploaded_file)
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Simulate disease detection (placeholder functionality)
        st.markdown('<div class="centered"><p>Analyzing the image...</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="centered"><b>Disease Detected: Leaf Blight</b></div>', unsafe_allow_html=True)

    except Exception as e:
        st.error("Error processing the image. Please upload a valid file.")

# Footer
st.markdown("""
<div class="centered">
<p>Receive instant predictions.</p>
<b>How It Works</b>
<p>Navigate to the "Disease Recognition" page.<br>
Upload an image of the affected plant.<br>
Get instant results along with disease information.</p>
<i>Developed by Team AgriSens | Powered by Streamlit</i>
</div>
""", unsafe_allow_html=True)
