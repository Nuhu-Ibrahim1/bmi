import streamlit as st
from PIL import Image
st.title('Dr Nuhu bmi Calculator')
img =Image.open('pexels-dominika-poláková-18355832.jpg')
st.image(img,width = 450)
name = st.text_input('What is Your Name')
weight = st.number_input('Enter your weight(in kg)')
status = st.radio('select your height format:',('cms','meters','feet'))
if (status == 'cms'):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")
elif (status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
if(st.button('calculate BMI')):
    st.text('your BMI index is {}'.format(bmi))
if(bmi < 16):
    st.error('{} you are Extremely Underweight'.format(name))
elif(bmi >= 16 and bmi < 18.5):
    st.warning('{} you are underweight'.format(name))
elif(bmi >= 18.5 and bmi < 25):
    st.success('{} Healthy'.format(name))
elif(bmi >= 25 and bmi < 30):
    st.warning('{} You are overweight'.format(name))
else:
    st.warning('{} You are Extremely Overweight'.format(name))





























