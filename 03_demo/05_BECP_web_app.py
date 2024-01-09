# BUILDING ENERGY CONSUMPTION PREDICTOR (BECP) Web application
### *by Jose Correa*

### import libraries
import pandas as pd
import streamlit as st
import joblib

#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file

#######################################################################################################################################
### Create a title
st.title("Healthcare Building Electricity Consumption Predictor App")
st.write("Welcome to the Healthcare Building Electricity Consumption Predictor App!")
st.write("WHAT IT DOES: This intuitive tool harnesses the predictive power of the Random Forest Regressor Machine Learning model. By integrating user-provided inputs, it accurately forecasts hourly electricity consumption for healthcare buildings.")
st.write("HOW IT WORKS: Easily tailor the weather forecasts and datetime inputs on the left of the screen and instantly obtain the electricity consumption prediction on the right, after by scrolling past the 'Historical hourly electricity consumption'. Compare this forecasted consumption with your actual electricity usage to evaluate potential energy savings.")
st.write("Empower your building's energy efficiency journey with insightful predictions at your fingertips!")

#######################################################################################################################################
# Add a line chart for Hourly electricity consumption
# Create a header
st.subheader("Historical hourly electricity consumption")

# DATA LOADING
df = pd.read_csv('C:/Users/jluco/Desktop/0_Data_Science_Bootcamp/2_Projects/50_Capstone/01_github_repo/03_demo/data_BECP.csv') 

# Plotting the line chart using Streamlit
st.line_chart(df.set_index('timestamp')['meter_reading'])

#######################################################################################################################################
### MODEL INFERENCE: we use Random Forest Regressor model for prediction

# Create a header
st.subheader("User inputs summary")

# Load the model using joblib
model = joblib.load('C:/Users/jluco/Desktop/0_Data_Science_Bootcamp/2_Projects/50_Capstone/01_github_repo/03_demo/05_becp_rf_reg.pkl')

# Create a header
st.sidebar.header("User inputs")

### create sliders for the features

# hour #############################################################################
hour = st.sidebar.slider("Hour", min_value=1, max_value=24, step=1)

# Month #############################################################################
month = st.sidebar.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

# Map the selected month to a numerical value (1 to 12)
month_mapping = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}
month_encoded = month_mapping[month]

# Day #############################################################################
day = st.sidebar.slider("Day of the month", min_value=1, max_value=31, step=1)

# air temperature #############################################################################
air_temperature = st.sidebar.slider("Air temperature (C)", min_value=-20, max_value=40, step=1)

# dew temperature #############################################################################
dew_temperature = st.sidebar.slider("Dew temperature (C)", min_value=-30, max_value=30, step=1)

# Sea level pressure #############################################################################
sea_level_pressure = st.sidebar.slider("Sea level pressure (millibar/hectopascals)", min_value=-1000, max_value=1000, step=1)

# Wind direction #############################################################################
wind_direction = st.sidebar.slider("Wind direction (degrees)", min_value=0, max_value=360, step=1)

# Wind speed #############################################################################
wind_speed = st.sidebar.slider("Wind speed (m/s)", min_value=0.0, max_value=13.5, step=0.1)


##########################################################################################################################
# Make a prediction based on user input
input_data = pd.DataFrame({
                           'Air temperature': [air_temperature],
                           'Dew temperature': [dew_temperature],
                           'Sea level pressure': [sea_level_pressure],
                           'Wind direction': [wind_direction],
                           'Wind speed': [wind_speed],
                           'month':[month],
                           'day':[day],
                           'hour':[hour]
                          })

# display user input
st.dataframe(input_data)

# create a header for the prediction
st.markdown(
    f'<h3 style="color: lightblue; text-align: center;">Electricity consumption prediction (kWh) = </h3>',
    unsafe_allow_html=True
)

# processed input_data (change the order of features to be properly used in the Random Forest Regressor model)
pro_input_data = pd.DataFrame({
                               'air_temperature': [air_temperature],
                               'dew_temperature': [dew_temperature],
                               'sea_level_pressure': [sea_level_pressure],
                               'wind_direction': [wind_direction],
                               'wind_speed': [wind_speed],
                               'month':[month_encoded],
                               'day':[day],
                               'hour':[hour]
                              })

# predict the pro_input_data
prediction = model.predict(pro_input_data)

# create a box and display the prediction value inside that
st.markdown(
    f'<div style="display: flex; justify-content: center; align-items: center; margin: auto; width: 120px; height: 40px; border: 2px solid lightblue; border-radius: 5px;">'
    f'<span style="color: lightblue; font-weight: bold; font-size: 28px ;">{prediction}</span>'
    f'</div>',
    unsafe_allow_html=True
)

