# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('C:/Users/Dell/OneDrive/Desktop/nfl/diabetes_model.sav','rb'))
heart_model=pickle.load(open('C:/Users/Dell/OneDrive/Desktop/nfl/heart_disease_model.sav','rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction',
                         
                         [ 'Diabetes Prediction',
                           'Heart Disease Prediction'],
                                                          
                         icons =['activity','heart'],
                         default_index=0 )
    
    
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction Using ML')
    
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the Person')
    
    
    diab_dignosis =''
    
    if st.button('Diabetes Test Result'):
       features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction, Age]
       diab_prediction = diabetes_model.predict([features], dtype=float)
        
       
       if (diab_prediction[0]==1):
             diab_dignosis='The Person is Diabetic'
       else:
             diab_dignosis='The person is NON Diabetic'
    
    st.success(diab_dignosis)
    
    
    
    
    
    
    
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using ML')
    
    age = st.text_input('Age of Person')
    sex = st.text_input('Gender')
    cp = st.text_input('cp')
    tresrbps = st.text_input('tresrbps')
    chol = st.text_input('Cholosterol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    
    
    heart_dignosis =''
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([[age,sex,cp,tresrbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]],dtype=float)
        if (diab_prediction[0]==1):
             diab_dignosis='The Person is healthy'
        else:
             diab_dignosis='The person is NOt healthy'
    
    st.success(heart_dignosis)