import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image  # Import Image from the PIL library
from joblib import load  # Import load from joblib
import warnings

st.set_page_config(page_title="Heart Failure Prediction",
                   page_icon="💉",
                   layout='centered',
                   initial_sidebar_state='auto')

# Data columns
feature_names_best = [
    'age', 'sex', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
    'ejection_fraction', 'high_blood_pressure', 'platelets',
    'serum_creatinine', 'serum_sodium', 'smoking', 'time'
]

gender_dict = {"Male": 1, "Female": 0}
feature_dict = {"Yes": 1, "No": 0}


def load_image(img):
  im = Image.open(os.path.join(img))
  return im


def load_model(modelfile):
  loaded_model = load(modelfile)
  return loaded_model


def get_value(val, my_dict):
  for key, value in my_dict.items():
    if val == key:
      return value


def get_fvalue(val):
  feature_dict = {"Yes": 1, "No": 0}
  for key, value in feature_dict.items():
    if val == key:
      return value


# title
html_temp = """
<div>
<h1 style="color:crimson;text-align:left;">Prediction of Survival in Patients with Heart Failure</h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

# How does it work section
'''
## How does it work ❓
Complete all the questions and the machine learning model will predict the survival of patients with heart failure
'''

# Logo
st.sidebar.image('real-heart-icon-png-.png', width=120)
st.sidebar.title("Prediction Form📋")

# Age of the patient
age = st.sidebar.number_input("Age", 1, 100)
# Male or Female
sex = st.sidebar.radio("Sex", tuple(gender_dict.keys()))
# Decrease of red blood cells or hemoglobin
anaemia = st.sidebar.radio("Anaemia ?", tuple(feature_dict.keys()))
# Level of the CPK enzyme in the blood
creatinine_phosphokinase = st.sidebar.number_input(
    "Creatinine phosphokinase (mcg/L)", 1, 7861)
# If the patient has diabetes
diabetes = st.sidebar.selectbox("Diabetes", tuple(feature_dict.keys()))
# Percentage of blood leaving
ejection_fraction = st.sidebar.number_input("Ejection fraction %", 1, 100)
# If a patient has hypertension
high_blood_pressure = st.sidebar.radio("High blood pressure",
                                       tuple(feature_dict.keys()))
# Platelets in the blood
platelets = st.sidebar.number_input("Platelets (kiloplatelets/mL)", 0.0,
                                    100000.0)
# Level of creatinine in the blood
serum_creatinine = st.sidebar.number_input("Serum creatinine (mg/dL)", 0.0,
                                           100.0)
# Level of sodium in the blood
serum_sodium = st.sidebar.number_input("Serum sodium (mEq/L)", 1, 1000)
# If the patient smokes
smoking = st.sidebar.radio("Smoking", tuple(feature_dict.keys()))
# Follow-up period
time = st.sidebar.number_input("Time (follow-up-period)", 1, 1000)

feature_list = [
    age,
    get_value(sex, gender_dict),
    get_fvalue(anaemia), creatinine_phosphokinase,
    get_fvalue(diabetes), ejection_fraction,
    get_fvalue(high_blood_pressure), platelets, serum_creatinine, serum_sodium,
    get_fvalue(smoking), time
]
pretty_result = {
    "Age": age,
    "Sex": sex,
    "Anaemia": anaemia,
    "Creatinine phosphokinase (mcg/L)": creatinine_phosphokinase,
    "Diabetes": diabetes,
    "Ejection fraction %": ejection_fraction,
    "High blood pressure": high_blood_pressure,
    "Platelets (kiloplatelets/mL)": platelets,
    "Serum creatinine (mg/dL)": serum_creatinine,
    "Serum sodium (mEq/L)": serum_sodium,
    "Smoking": smoking,
    "Time": time
}
'''
## These are the values you entered 🧑‍⚕
'''
st.json(pretty_result)
single_sample = np.array(feature_list).reshape(1, -1)

if st.button("Predict"):
		'''
		## Results 👁‍🗨

		'''
		loaded_model = load_model('model.pkl')
		prediction = loaded_model.predict(single_sample)
		pred_prob = loaded_model.predict_proba(single_sample)
		
		if prediction == 1:
			st.error("The patient will die")
		else:
			st.success("The patient will live")
			
		for live, die in loaded_model.predict_proba(single_sample):
				live = f"{live*100:.2f}%"
				die = f"{die*100:.2f} %"
				st.table(pd.DataFrame({'Live ':live,
								'Die': die}, index=['probability']))

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
