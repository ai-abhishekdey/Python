
import streamlit as st
from PIL import Image

## Title

st.title("Example of widgets in streamlit")

## Text input: st.text_input

st.markdown("## Name")


first_name = st.text_input("First name")
middle_name = st.text_input("Middle name")
last_name = st.text_input("Last name")

## Calender: st.date_input

st.markdown("## Date of Birth")

dob = st.date_input("Select your date of birth")

## Slider: st.slider

age = st.slider("select your age", 0, 100)

## Radio button: st.radio

st.markdown("## Gender")

st.radio("Select your gender",options=["Male", "Female"])

## Drop Down: st.selectbox

st.markdown("## Select District")

st.selectbox("Select District", options=["Bongaigaon", "Kamrup", "Jorhat", "Nagon"])

## File upload: st.file_uploader

st.markdown("## Upload your image")

uploaded_image = st.file_uploader("Upload image")


## Image display: st.image

if uploaded_image is not None:

    image=Image.open(uploaded_image)

    st.image(image)
