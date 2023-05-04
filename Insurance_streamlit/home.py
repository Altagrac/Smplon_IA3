#    ******* PACKAGES*********
import streamlit as st
import pandas as pd
import numpy as np
import requests as req

#*************************
    #   *** Mise en forme du site ***

title = '<h1 style="font-family:verdana; text-align:center; color:Yellow; font-size: 100px;">Welcome to MedFiz</h1>'
title_2 = '<h2 style="font-family:trebuchet; text-align:center; color:Yellow; font-size: 100px;">Cost prediction ($)  </h2>'
title_3 = '<h2 style="font-family:trebuchet; text-align:center; color:Yellow; font-size: 100px;">Conversion table currency </h2>'
script = '<p style="font-family:trebuchet; text-align:center; color:Yellow; font-size: 30px;">Medical expenses have always been and will be a priority expenses in our life. Medfiz aims to predict the cost of these charges for better financial management.</p>'

menu = ["About","MedFiz"," International MedFiz "]
choice = st.sidebar.selectbox("Menu",menu)

#@st.cache
def get_data(url):
    resp = req.get(url)
    return resp.json()


if choice == "About":
    st.markdown(title, unsafe_allow_html=True)
    st.markdown(script,unsafe_allow_html=True)
    st.write("Select in the menu ")
    st.write("## MedFiz for rediction in local currency ($)")
    st.write("## :earth_africa:  MedFiz :earth_africa: for Prediction in others currency")

elif choice == "MedFiz":
    st.markdown(title_2, unsafe_allow_html=True)
    age = st.slider('How old are you?', 0, 130, 25)
    bmi = st.text_input("Corporal Mass indice")
    children = st.text_input("How namy children?")
    genre = st.radio("What\'s your gender",('Male', 'female'))
    smok = st.radio("Do you smok?",('No', 'Yes'))
    base_url = f"https://dcac-185-175-148-123.eu.ngrok.io?age={age}&bmi={bmi}&children={children}&sex={genre}&smoker={smok}&region=No"
    st.write(base_url)
    data = get_data(base_url)
    st.write(f'Your insurance will cost you {data["prédiction charge"]}$')

else :
    st.markdown(title_3, unsafe_allow_html=True)
