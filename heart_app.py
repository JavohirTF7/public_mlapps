import streamlit as st
import pickle


model = pickle.load(open('xgboost_heartpredictor.pkl', 'rb'))


with st.sidebar:
    selected = st.selectbox('Select Prediction Type', 
                            ['Heart Disease Prediction', 'Diabetes Prediction'],
                            index=0)


if selected == 'Heart Disease Prediction':
    # Page Title
    st.title('Heart Condition Prediction using ML')

    
    race_options = {"American Indian/Alaskan Native": 0, "White": 5, "Black": 2, "Asian": 1, "Hispanic": 3, "Other": 4}
    sex_options = {"Male": 1, "Female": 0}
    age_categories = {"18-24": 0, "25-29": 1, "30-34": 2, "35-39": 3, "40-44": 4, "45-49": 5, "50-54": 6, "55-59": 7,
                      "60-64": 8, "65-69": 9, "70-74": 10, "75-79": 11, "80 or older": 12}
    bmi_categories = {"Underweight (BMI: below 18.5)": 3, "Normal weight (BMI: 18.5-25)": 0,
                      "Overweight (BMI: 25-30)": 2, "Obese (BMI: above 30)": 1}
    general_health_options = {"Excellent": 0, "Very Good": 4, "Good": 2, "Fair": 1, "Poor": 3}
    sports_played_categories = {"No": 0, "Yes": 1}
    smoking_categories = {"No": 0, "Yes": 1}
    alcohol_categories = {"No": 0, "Yes": 1}
    difficulty_walking_categories = {"No": 0, "Yes": 1}
    diabetes_categories = {"Yes (during pregnancy)": 3, "No, borderline diabetes": 1, "No": 0, "Yes": 2}
    stroke_categories = {"No": 0, "Yes": 1}
    asthma_categories = {"No": 0, "Yes": 1}
    kidney_disease_categories = {"No": 0, "Yes": 1}
    skin_cancer_categories = {"No": 0, "Yes": 1}

    
    col1, col2 = st.columns(2)

    
    with col1:
        st.markdown("### Provide All Inputs")
        selected_race = st.selectbox("1. Race:", list(race_options.keys()))
        selected_sex = st.selectbox("2. Sex:", list(sex_options.keys()))
        selected_age_category = st.selectbox("3. What's your age category:", list(age_categories.keys()))
        selected_bmi_category = st.selectbox("4. BMI Category:", list(bmi_categories.keys()))
        selected_general_health = st.selectbox("5. Describe your general health:", list(general_health_options.keys()))
        hours_of_sleep = st.number_input("6. How many hours on average do you sleep?", min_value=0, max_value=24, value=0, step=1)
        played_sports = st.selectbox("7. Have you played any sports in the past month?", ["No", "Yes"])
        smoked_cigarettes = st.selectbox("8. Have you smoked at least 100 cigarettes in your entire life?", ["No", "Yes"])
        drinks_of_alcohol = st.selectbox("9. Do you have more than 14 drinks of alcohol (men) or more than 7 (women) in a week?", ["No", "Yes"])
        days_physical_health_not_good = st.number_input("10. For how many days during the past 30 days was your physical health not good?", min_value=0, max_value=30, value=0, step=1)
        days_mental_health_not_good = st.number_input("11. For how many days during the past 30 days was your mental health not good?", min_value=0, max_value=30, value=0, step=1)
        difficulty_walking_or_climbing_stairs = st.selectbox("12. Do you have serious difficulty walking or climbing stairs?", ["No", "Yes"])
        ever_had_diabetes = st.selectbox("13. Have you ever had diabetes?", ["Yes (during pregnancy)", "No, borderline diabetes", "No", "Yes"])
        had_stroke = st.selectbox("14. Have you had a stroke in the past?", ["No", "Yes"])
        has_asthma = st.selectbox("15. Do you have asthma?", ["No", "Yes"])
        has_kidney_disease = st.selectbox("16. Do you have kidney disease?", ["No", "Yes"])
        has_skin_cancer = st.selectbox("17. Do you have skin cancer?", ["No", "Yes"])

    
    
    with col2:
        
        st.image("drxgboost.jpg", caption="Provide the inputs on the left. I'll help you diagnose your heart health! - Dr. XGBoost", width=340)
        st.markdown("### Descriptions")
        st.markdown(
            """
            Are you wondering about the condition of your heart? I'll help you diagnose your heart health. I'm Dr XGBoost!

            Did you know that machine learning models can help you predict heart disease pretty accurately?
            With this app, you can estimate your chance (probability) of heart having disease in seconds!
            The app is a result of training a gradient boosting model (XGBoost) using a dataset of over 300,000 United States residents from 2020.
            The overall prediction accuracy of the model is pretty high at 91.5%.

            To predict your heart disease status, simply follow the steps below:
            - **Enter the parameters that best describe you in an honest manner,**
            - **Press the "Predict" button at the end and wait for your result.**

            Keep in mind that this result is not equivalent to a medical diagnosis! This model has less than perfect accuracy, so if you have any problems, consult a human doctor.
            
            **Description of the Results**  
            A percentage probability of your heart having a disease will be returned. I took the freedom to class the probability into 4 groups, 0-25% as the "green zone", 25-50% as the "yellow zone", 50-75% as the "orange zone" and 75-100% as the "red zone".
            This may not mean anything, but it's just to get some picture of the result.

            **Author:** Jesse Gabriel, Port Moresby  
            [Email](mailto:optimusservices22@gmail.com). Connect with me at [LinkedIn](https://www.linkedin.com/in/jesse-gabriel-aa561157/)
            """
        )


    BMICategory = bmi_categories[selected_bmi_category]
    Smoking = smoking_categories[smoked_cigarettes]
    AlcoholDrinking = alcohol_categories[drinks_of_alcohol]
    Stroke = stroke_categories[had_stroke]
    PhysicalHealth = days_physical_health_not_good
    MentalHealth = days_mental_health_not_good
    DiffWalking = difficulty_walking_categories[difficulty_walking_or_climbing_stairs]
    Sex = sex_options[selected_sex]
    AgeCategory = age_categories[selected_age_category]
    Race = race_options[selected_race]
    Diabetic = diabetes_categories[ever_had_diabetes]
    PhysicalActivity = sports_played_categories[played_sports]
    GenHealth = general_health_options[selected_general_health]
    SleepTime = hours_of_sleep
    Asthma = asthma_categories[has_asthma]
    KidneyDisease = kidney_disease_categories[has_kidney_disease]
    SkinCancer = skin_cancer_categories[has_skin_cancer]

    input_data = [[BMICategory, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth,
                   DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth,
                   SleepTime, Asthma, KidneyDisease, SkinCancer]]

    if st.button('Predict'):
        prediction_proba = model.predict_proba(input_data)[:, 1]
        rounded_prediction = round(prediction_proba[0] * 100, 2)

        color_style = ""

        if rounded_prediction < 25:
            prediction_sentence = f"<b>The probability that you will have heart disease is {rounded_prediction}%. You are good and in the green zone.</b>"
            color_style = "color: #32CD32; font-size: 30px;"  
        elif 25 <= rounded_prediction < 50:
            prediction_sentence = f"<b>The probability that you will have heart disease is {rounded_prediction}%. You are in the yellow zone.</b>"
            color_style = "color: #FFD700; font-size: 30px;"  
        elif 50 <= rounded_prediction < 75:
            prediction_sentence = f"<b>The probability that you will have heart disease is {rounded_prediction}%. You are in the orange zone and you may need to consult a doctor.</b>"
            color_style = "color: #FF4500; font-size: 30px;"  
        else:
            prediction_sentence = f"<b>The probability that you will have heart disease is {rounded_prediction}%. You are in the red zone and it is advisable to seek advice from a human doctor.</b>"
            color_style = "color: #DC143C; font-size: 30px;"  

        st.markdown(f"<p style='{color_style}'>{prediction_sentence}</p>", unsafe_allow_html=True)

