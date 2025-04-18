import streamlit as st
from PIL import Image

# Load an image to display at the top of the title
top_image = "top_image.jpg"  # Replace with the path to your image file

# Display the top image
st.image(top_image, caption="Plant Disease Detection", use_column_width=True)

# Title of the app
st.title("Plant Disease Detection App")

# Subtitle
st.subheader("Upload an image to detect plant diseases!")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Process the uploaded file
if uploaded_file is not None:
    try:
        # Open and display the image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Simulate disease detection (placeholder functionality)
        st.write("Analyzing the image...")
        # Example result (this would be replaced by actual ML model prediction)
        st.success("Disease Detected: Leaf Blight")

    except Exception as e:
        st.error("Error processing the image. Please upload a valid file.")

# Footer
st.write("Receive instant predictions.")
st.markdown("""
**How It Works**
- Navigate to the "Disease Recognition" page.
- Upload an image of the affected plant.
- Get instant results along with disease information.

*Developed by Team AgriSens | Powered by Streamlit*
""")
