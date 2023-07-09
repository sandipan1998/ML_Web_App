import numpy as np
import pickle
import streamlit as st
# loading the saved model
loaded_model=pickle.load(open("C:/Users/sandipan/ML_Deply/venv/M_HeartDisease/trained_model.sav",'rb'))
def diabetes_prediction(input_data):
    input_data_array=np.asarray(input_data,dtype=np.float64)

    input_data_reshaped=input_data_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    if(prediction==1):
        return"The Person have Heart Disesase!"
    else:
        return"The Person do no have Heart Disease"
def main():
    st.title("Cardiovascular Health Assessment")
    description = '1 is typical angina Pain, 2 is atypical angina Pain, 3 is non-anginal Pain'
    description1="Represents the resting blood pressure (in mm Hg) of the patient."
    description2="Indicates the level of serum cholesterol (in mg/dL) in the patient's blood."
    description3="Fasting blood sugar level of the patient (1 = greater than 120 mg/dL, 0 = less than or equal to 120 mg/dL)."
    description4="Describes the results of the resting electrocardiogram.  0: Normal ECG result, 1: Abnormal ECG result indicating ST-T wave abnormalities,   2: ECG result indicating probable or definite left ventricular hypertrophy (LVH)                                               ."
    description5="Refers to the maximum heart rate achieved by the patient during exercise stress testing."
    description6="Indicates whether the patient experienced angina (chest pain) during exercise. It is a binary value (1 for yes, 0 for no)."
    description7="The ST depression feature is measured in millimeters (mm) on an electrocardiogram (ECG). In this case, a value of x mm would indicate the extent of ST segment depression observed during exercise compared to the resting state."
    description8="Describes the slope of the peak exercise ST segment. It is categorized as upsloping, flat, or downsloping."
    description9="Indicates the number of major blood vessels colored by fluoroscopy. It typically ranges from 0 to 3."
    description10=" Represents a blood disorder. It is categorized as normal, fixed defect, or reversible defect."
    # Get user input for the chest pain type
    age = st.text_input(
        label="Age",
        help=f"Description for input: Age of the person",
        key='age'
    )
    sex = st.text_input(
        label="Gender",
        help=f"Description for input: 1 for Male and 0 for Female",
        key='Gender'
    )
    chest_pain_type = st.text_input(
        label="Chest pain type",
        help=f"Description for input: {description}",
        key='chest_pain_type'
    )
    trestbps = st.text_input(
        label="Resting Blood Pressure",
        help=f"Description for input: {description1}",
        key='trestbps'
    )
    chol = st.text_input(
        label="Serum Cholesterol",
        help=f"Description for input: {description2}",
        key='chol'
    )
    fbs = st.text_input(
        label="Fasting Blood Sugar",
        help=f"Description for input: {description3}",
        key='fbs'
    )
    restecg = st.text_input(
        label="Resting Electrocardiographic Results",
        help=f"Description for input: {description4}",
        key='restecg'
    )
    thalach = st.text_input(
        label="Maximum heart achieved",
        help=f"Description for input: {description5}",
        key='thalach'
    )
    exang = st.text_input(
        label="Exercise Induced Angina",
        help=f"Description for input: {description6}",
        key='exang'
    )
    oldpeak = st.text_input(
        label="ST Depression",
        help=f"Description for input: {description7}",
        key='oldpeak'
    )
    slope= st.text_input(
        label="Slope of the ST segment",
        help=f"Description for input: {description8}",
        key='slope'
    )
    ca= st.text_input(
        label="Number of Major Vessels",
        help=f"Description for input: {description9}",
        key='ca'
    )
    thal=st.text_input(
        label="Thalassemia",
        help=f"Description for input: {description10}",
        key='thal'
    )
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Cardiovascular Test Result'):
        diagnosis = diabetes_prediction([age,sex,chest_pain_type, trestbps, chol,fbs, restecg, thalach, exang, oldpeak,slope,ca,thal])
        
        
    st.success(diagnosis)

# getting input data
#63	1	3	145	233	1	0	150	0	2.3	0	0	1	1
if __name__ == '__main__':
    main()



























    
        
     
