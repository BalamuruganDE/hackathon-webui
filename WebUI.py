
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title('Vehicle Insurance Prediction')


df = pd.read_csv('train.csv')

Gender = st.selectbox("Gender",pd.unique(df['Gender']))
Age = st.number_input("Age",min_value=20,max_value=90,step=1)
Driving_License = st.selectbox("Driving_License",pd.unique(df['Driving_License']))
Region_Code  = st.selectbox("Region_Code",pd.unique(df['Region_Code']))
Previously_Insured = st.selectbox("Previously_Insured",pd.unique(df['Previously_Insured']))
Vehicle_Age = st.selectbox("Vehicle_Age",pd.unique(df['Vehicle_Age']))
Vehicle_Damage = st.selectbox("Vehicle_Damage",pd.unique(df['Vehicle_Damage']))
Annual_Premium = st.number_input("Annual_Premium",step=1)
Policy_Sales_Channel = st.selectbox("Policy_Sales_Channel",pd.unique(df['Policy_Sales_Channel']))
Vintage = st.selectbox("Vintage",pd.unique(df['Vintage']))

inputs = {
'Gender'                  :   Gender,
'Age'                     :   Age,
'Driving_License'         :   Driving_License,
'Region_Code'             :   Region_Code,
'Previously_Insured'      :   Previously_Insured,
'Vehicle_Age'             :   Vehicle_Age,
'Vehicle_Damage'          :   Vehicle_Damage,
'Annual_Premium'          :   Annual_Premium,
'Policy_Sales_Channel'    :   Policy_Sales_Channel,
'Vintage'                 :   Vintage
}



# loading ML-Model from the pickel-file
# model = joblib.load('cross-sell-pred-pkl.gz')
# model = joblib.load('../cross-sell-pred-xgb-pkl.gz')
model = joblib.load('cross-sell-pred-xgb-pkl.gz')

# Action for submit button
if st.button ('Predict'):
    X_input = pd.DataFrame(inputs,index=[0])
    prediction = model.predict(X_input)
    if prediction == 0:
        st.write(f"Customer is **NOT INTERESTED**  in buying Vehicle Insurance")
    else:
        val = 'YES'
        st.write(f"Customer is **INTERESTED** in buying Vehicle Insurance")



#file upload experiment
st.subheader ("Please upload the csv file for prediction")
upload_file=st.file_uploader("Choose the csv file",type=['csv'])


if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.write("File uploaded successfully")
    st.write(df.head(2))

    if st.button("Predict the uploaded file"):
        df['Response'] = model.predict (df)
        st.write("Prediction completed")
        st.write(df.head(2))
        
        st.download_button(label="Download Prediction",data=df.to_csv(index=False),file_name="Prediction.csv",mime="text/csv")

        st.session_state.download_message = False


