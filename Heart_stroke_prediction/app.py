import pickle
import streamlit as st

log = pickle.load(open("C:/Users/user/Projects(Data_Sc_ML_)/data_analysis_projects/Heart_stroke_prediction/heart_prediction_model.pickle","rb"))

def main():
    st.title("PREDICTION:")

    # input
 #hypertension	heart_disease	avg_glucose_level	bmi	stroke	Female	Male	Other	Govt_j
 # ob	Never_worked	Private	Self-employed	children	Unknown	formerly smoked	never smoked	smokes   
    age = st.text_input("age")
    hypertension = st.text_input("hypertension")
    heart_disease = st.text_input("heart_disease")
    avg_glucose_level	 = st.text_input("avg_glucose_level	")
    bmi = st.text_input("bmi")
    stroke = st.text_input("stroke")
    Female = st.text_input("Female")
    Male = st.text_input("Male")
    Other = st.text_input("Other")
    Govt_job = st.text_input("Govt_job")
    Never_worked = st.text_input("Never_worked")
    Private = st.text_input("Private")
    Self_employed = st.text_input("Self-employed")
    Children= st.text_input("Children")
    Unknown = st.text_input("Unknown")
    formerly_smoked = st.text_input("formerly smoked")
    never_smoked = st.text_input("never_smoked")
    smokes = st.text_input("smokes")

    if st.button("predict"):
        # makeprediction = log.predict([[age,hypertension,heart_disease,avg_glucose_level,bmi,stroke,Female,Male,Other,Govt_job,Never_worked,Private,Self_employed,Children,Unknown,formerly_smoked,never_smoked,smokes]])
        output = 2.5
        st.success("YEAH")
    if __name__=="__main__":
        main()



