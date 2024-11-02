import streamlit as st 
import pandas as pd 
import pickle
import time
data1= pickle.load(open("Models/diabetes_disease.sav",'rb'))
#-----------------------------------------------------------------------------
st.sidebar.info(" ### :blue[Your medical guide to detecting diseases] 🧐")
tab1, tab2, tab3= st.tabs(['| About Diabetes |','| About Model |','| Testing For Diabetes |'])

tab1.image('img/19.jpg', width=450)

tab1.markdown("##### Diabets is a chronic disease that occurs either when the pancreas dose not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood glucose.")
tab1.info('##### Hyperglycaemia, also called raised blood glucose or raised blood sugar, is a common effect of uncontrolled diabetes and over time leads to serious damage to many of the bodys systems, especially the nerves and blood vessels.')  
tab1.info('##### Diabets can be treated and its consequences avoided or delayed with diet, physical activity,and avoiding tobacco use, medication and regular screening and treatment for complications.')


#---------------------------------------------------------------------------
tab2.info('##### Model accuracy : :green[95%] ')
tab2.markdown("### The attributes :")
tab2.info('###### 1-Gender: Refers to the biological sex of the individual, which can have an impact on their susceptibility to diabetes.')
tab2.info('###### 2-Age: The person Age In :red[Years]. Age is an important factor as diabetes is more commonly diagnosed in older adults.')
tab2.info('###### 3-Hypertension: Is a medical condition in which the blood pressuer in the arteries is persistenttly elevated.')
tab2.info('###### 4-Heart Disease: Is another medical condition that is associated wiht an increased risk of developing diabetes.')
tab2.info('###### 5-BMI: Body Mass Index is a measure of body fat based on weight and height. :red[BMI Less Than (18.5) Is Underweight\ (18.5-24.9) Is Normal\ (25-29.9) Is Overweight\ (30 Or More) Is Obese.]')
tab2.info('###### 6-Smoking History: Is considered a risk factor for diabetes and can exacerbate the complications associated.')
tab2.info('###### 7-Blood Glucose Level: Refers to the amount of glucose in the blood stream at a given time. high blood glucose levels are a key indicator of diabetes')
#tab2.info('###### 8-HBA1C Level: Hemoglobin A1c level is a measure of a persons average blood suger level over the :red[Past 2-3] months. mostly more than :red[6.5%] of HbA1c level indicates diabetes')
#--------------------------------------------------------------------------

with tab3.form('form'):
    col1,col2,= st.columns(2, gap="large")
    with col1:
        gender=['Male', 'Female']
        gender1=[1, 0]
        gender_new=dict(zip(gender,gender1))
        bt=st.radio('Gender?', gender)
        gender2= gender_new[bt]
        #--------------------------------------------------------------------
        hypertension=['Yas', 'No']
        hypertension1=[1, 0]
        hypertension_new=dict(zip(hypertension,hypertension1))
        bt2=st.radio('hypertension ?', hypertension)
        hypertension2= hypertension_new[bt2]
        #-------------------------------------------------------------------
        heart_disease=['Yes', 'No']
        heart_disease1=[1, 0]
        heart_disease_new=dict(zip(heart_disease,heart_disease1))
        bt3=st.radio('heart disease ?', heart_disease)
        heart_disease2= heart_disease_new[bt3]
        #--------------------------------------------------------------------
    with col2:
        bt1=st.slider('Age?', 1, 90)
        #--------------------------------------------------------------------
        smoking_history=['never','No info','former','current','not current','ever']
        smoking_history1=[4 , 0 , 3 , 1 , 5 , 2]
        smoking_history_new=dict(zip(smoking_history,smoking_history1))
        bt4=st.selectbox('smoking history ?', smoking_history)
        smoking_history2= smoking_history_new[bt4]
        #-------------------------------------------------------------------
        #bt6=st.number_input('Hemoglobin_A1c_level?', 0, 9)
        #--------------------------------------------------------------------
        bt7=st.text_input('blood glucose level?')
        #--------------------------------------------------------------------
        bt5=st.text_input('Body mass index?')
        #--------------------------------------------------------------------
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
    df1=pd.DataFrame({'gender':gender2, 'smoking_history':smoking_history2, 'age':bt1,
     'hypertension':hypertension2, 'heart_disease':heart_disease2, 'bmi':bt5,
       'blood_glucose_level':bt7,},index=[0])
    bt_predict=st.form_submit_button("Predict...❗")
if bt_predict:
        with st.spinner('Processing...🔄'):
            time.sleep(2)
            result=data1.predict(df1)

            if result == 0:
                tab3.header(' :blue[Patient Report :]')
                tab3.subheader(' Inquiry About  Diabetes ')
                c1,= st.columns(1)
                #_______
                tab3.markdown("####  Sex :")
                tab3.warning(bt)
                #_______
                tab3.markdown("####  Age :")
                tab3.warning(bt1)
                #_______
                tab3.markdown('####  hypertension ?')
                tab3.warning(bt2)
                #_______
                tab3.markdown('####  heart_disease ?')
                tab3.warning(bt3)
                #_______
                tab3.markdown('####  smoking_history :')
                tab3.warning(bt4)
                #_______
                tab3.markdown('#### Body Mass Index : ')
                tab3.warning(bt5)
                #_______
                #tab3.markdown('####  Hemoglobin A1c_level :')
                #tab3.warning(bt6)
                #_______
                tab3.markdown('####  blood_glucose_level :')
                tab3.warning(bt7)
                #_______
                tab3.markdown('#### Degree Of Risk :')
                tab3.success("LOW")
                #_______
                tab3.markdown('#### Query Result :')
                tab3.success("The patient is healthy, take care of yourself.")
            else:
                tab3.header(':blue[Patient Report :]')
                tab3.subheader(' Inquiry About Diabetes ')
                c1,= st.columns(1)
                #_______
                tab3.markdown("#### Sex :")
                tab3.info(bt)
                #_______
                tab3.markdown("####  Age :")
                tab3.info(bt1)
                #_______
                tab3.markdown('####  hypertension ?')
                tab3.info(bt2)
                #_______
                tab3.markdown('####  heart_disease ?')
                tab3.info(bt3)
                #_______
                tab3.markdown('####  smoking_history :')
                tab3.info(bt4)
                #_______
                tab3.markdown('####  Body Mass Index :')
                tab3.info(bt5)
                #_______
                #tab3.markdown('####  Hemoglobin A1c_level :')
                #tab3.info(bt6)
                #_______
                tab3.markdown('#### blood_glucose_level :')
                tab3.info(bt7)
                #_______
                tab3.markdown('#### Degree Of Risk : ')
                tab3.error("High")
                #_______
                tab3.markdown('#### Query Result : ')
                tab3.error("The patient may requer attention, please go to the doctor.")