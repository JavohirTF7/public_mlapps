import streamlit as st
import pickle


model = pickle.load(open('xgboost_heartpredictor.pkl', 'rb'))


with st.sidebar:
    selected = st.selectbox('Select Disease', 
                            ['Heart Disease Prediction','Diabetes Prediction (Under Development)'], 
                            index=0)


if selected == 'Heart Disease Prediction':
    # Page Title
    st.title('Yurak xastaliklarini aniqlash')

    
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
        st.markdown("### Siz kiritishingiz kerak bo'lgan malumotlar")
        selected_race = st.selectbox("1. Irq:", list(race_options.keys()))
        selected_sex = st.selectbox("2. Jins:", list(sex_options.keys()))
        selected_age_category = st.selectbox("3. qaysi yosh kategoriyasdasiz:", list(age_categories.keys()))
        selected_bmi_category = st.selectbox("4. BMI Category:", list(bmi_categories.keys()))
        selected_general_health = st.selectbox("5. Umumiy sog'lig'ingiz haqida malumot:", list(general_health_options.keys()))
        hours_of_sleep = st.number_input("6. Kuniga o'rtacha qancha uxlaysiz?", min_value=0, max_value=24, value=0, step=1)
        played_sports = st.selectbox("7. O'tgan oyda biron bir sport bilan shug'ullanganmisiz?", ["No", "Yes"])
        smoked_cigarettes = st.selectbox("8. Siz butun umringiz davomida kamida 100 ta sigaret chekganmisiz?", ["No", "Yes"])
        drinks_of_alcohol = st.selectbox("9. Sizda bir haftada 14 dan ortiq spirtli ichimliklar (erkaklar) yoki 7 dan ortiq (ayollar) bormi??", ["No", "Yes"])
        days_physical_health_not_good = st.number_input("10. So'nggi 30 kun ichida necha kun davomida jismoniy sog'ligingiz yaxshi emas edi?", min_value=0, max_value=30, value=0, step=1)
        days_mental_health_not_good = st.number_input("11. Oxirgi 30 kun ichida necha kun davomida ruhiy salomatligingiz yaxshi emas edi?", min_value=0, max_value=30, value=0, step=1)
        difficulty_walking_or_climbing_stairs = st.selectbox("12. Sizda yurish yoki zinapoyaga chiqishda jiddiy qiyinchiliklar bormi?", ["No", "Yes"])
        ever_had_diabetes = st.selectbox("13. Qandli diabet bilan kasallanganmisiz?", ["Yes (during pregnancy)", "No, borderline diabetes", "No", "Yes"])
        had_stroke = st.selectbox("14. Oldin insult bo'lganmisiz?", ["No", "Yes"])
        has_asthma = st.selectbox("15. Sizda astma bormi?", ["No", "Yes"])
        has_kidney_disease = st.selectbox("16. Sizda buyrak kasalligi bormi?", ["No", "Yes"])
        has_skin_cancer = st.selectbox("17. Sizda teri saratoni bormi?", ["No", "Yes"])

    
    
    with col2:
        
        st.image("drxgboost.jpg", caption="Chapdagi malumotlarni kiriting. Men sizga yurak sog'lig'ingizni tashxislashda yordam beraman!", width=340)
        st.markdown("### Yo'riqnoma")
        st.markdown(
            """
            Yuragingizning holati haqida qiziqyapsizmi? Men sizga yurak sog'lig'ingizni tashxislashda yordam beraman.

            Mashinani o'rganish modellari yurak xastaliklarini aniq bashorat qilishda yordam berishi mumkinligini bilasizmi? Ushbu ilova yordamida siz bir necha soniya ichida yurak xastaligi ehtimolini (ehtimolini) taxmin qilishingiz mumkin!

            Yurak kasalligining holatini taxmin qilish uchun quyidagi amallarni bajaring::
            - **Sizni eng yaxshi tavsiflovchi parametrlarni to'g'ri kiriting**
            - **Oxirida "Predict" tugmasini bosing va natijangizni kuting.**
            
            **Natijalarni tavsifi**  
            Yuragingizning kasal bo'lish ehtimoli foizga beriladi. Men ehtimollikni 4 guruhga bo'lish erkinligini oldim, 0-25% "yashil zona", 25-50% "sariq zona", 50-75% "to'q sariq zona" va 75-100%. "qizil zona".
              Bu hech narsani anglatmasligi mumkin, lekin bu shunchaki natijaning rasmini olish uchun.

            **Author:** Ermatova Bahora, Toshkent, Yuksalish maktabi
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

