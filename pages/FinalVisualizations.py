import streamlit as st
import os

# Construct paths relative to the current file
current_dir = os.path.dirname(__file__)
image1_path = os.path.join(current_dir, "../MLV1.jpg")
image2_path = os.path.join(current_dir, "../MLV2.jpg")
image3_path = os.path.join(current_dir, "../MLV3.jpg")


st.set_page_config(page_title="Midterm Visualizations")

st.title("Midterm Visualizations")
st.write("Here are our visualizations for the midterm.")

# Display images
st.image(image1_path, caption="Logistic Regression Visualization", use_column_width=True)
st.image(image3_path, caption="Random Forest Visualization", use_column_width=True)
st.image(image2_path, caption="K-means Visualization", use_column_width=True)
