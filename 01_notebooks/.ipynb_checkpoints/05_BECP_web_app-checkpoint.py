# BECP: Web application
### *by Jose Correa*

### import libraries
import pandas as pd
import streamlit as st
import joblib

st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
    This is is just a very small window into its capabilities.')


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file



#######################################################################################################################################
### Create a title

st.title("Kickoff - Live coding an app")

# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)

#######################################################################################################################################
### MODEL INFERENCE

st.subheader("Using pretrained models with user input")

# A. Load the model using joblib
model = joblib.load('05_becp_rf_reg.pkl')

# B. Set up input field
text = st.text_input('Enter your review text below', 'bike station was empty')

# C. Use the model to predict sentiment & write result
# prediction = model.predict({text})

# if prediction == 1:
#    st.write('We predict that this is a positive review!')
# else:
#    st.write('We predict that this is a negative review!')


#######################################################################################################################################
### Streamlit Advantages and Disadvantages
    
st.subheader("Streamlit Advantages and Disadvantages")
st.write('**Advantages**')
st.write(' - Easy, Intuitive, Pythonic')
st.write(' - Free!')
st.write(' - Requires no knowledge of front end languages')
st.write('**Disadvantages**')
st.write(' - Apps all look the same')
st.write(' - Not very customizable')
st.write(' - A little slow. Not good for MLOps, therefore not scalable')
