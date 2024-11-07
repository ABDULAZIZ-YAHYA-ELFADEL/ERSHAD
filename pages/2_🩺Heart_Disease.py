import streamlit as st 
import pandas as pd 
import pickle
import time
data= pickle.load(open("Models/heart_disease.sav",'rb'))
#-----------------------------------------------------------------------------
st.sidebar.info("Your medical guide to detecting diseases🧐")
tab1, tab2, tab3= st.tabs(['| About Heart Disease |','| About Model |','| Testing For Heart Disease |'])

tab1.image('img/13.jpg', width=300)

tab1.markdown("##### The world health organization reports that heart disease is the most common cause of death globally, accounting for :red[17.9 Million] fatalities annually. ")
tab1.info('##### The signs of a women having a heart attack are much less noticeable than the signs of a male. In women, heart attacks may feel uncomfortable squeezing, pressure, fullness, or pain in the center of the chest. It may also cause pain in one or both arms, the back, neck, jaw or stomach, shortnesss of breath, nausea and other symptoms.')  
tab1.info('##### Men experience typical symptoms of heart attack, such as chest pain, discomfort, and stress. They may also esperience pain in other areas, such as arms, neck, back, jaw, and shortness of breath,sweating, and discomfort that mimics heartburn.')
#-----------------------------------------------------------------------------
tab2.info('##### Model accuracy : :green[91%] ')
tab2.markdown("### The Attributes :")
tab2.info('###### 1-Gender: The person sex. ')
tab2.info('###### 2-Age: The person age in :red[years] . ')
tab2.info('###### 3-Chest Pain Type: Asymptomatic/ Atypical Angina/ Non-Angina Pain/ Typical Angina. ')
tab2.info('###### 4-Cholesterol: The person cholesterol measurement in :red[mg/dl].')
tab2.info('###### 5-Fasting Blood Suger: Is :red[>120 ?]. ')
tab2.info('###### 6-Resting Electrocardiographic Results:  Normal/ Left Ventricular Hypertrophy(:red[By Estes Criteria])/ ST-T Wave Abnormality.')
tab2.info('###### 7-Exercise Angina: Exercise Induced Angina ?')
#tab2.info('###### 8-Oldpeak: ST depression induced by exercise relative to rest(ST relates to positions on the ECG plot).')
tab2.info('###### 8-ST_Slope: The slope oF the peak exercise ST segment(Downsloping/ Upsloping/ Flat).')
tab2.info('###### 9-Max HR: Maximum heart rate achieved.')  
tab2.info('###### 10_Resting Blood Pressure : The person resting blood pressure(:red[mm Hg])')
#------------------------------------------------------------------------------
tab3.warning('### :red[🏴 This test requires an ECG examination. ]')
tab3.write("\n")
tab3.write("\n")
tab3.write("\n")
tab3.markdown('### :red[🚩 All Fields Are Required: ]')
tab3.write("\n")
with tab3:
    col1,col2,col3,= st.columns(3, gap="large")
    with col1:
        sex=['Male', 'Female']
        sex1=[1, 0]
        sex_new=dict(zip(sex,sex1))
        bt=st.radio('Gender?',sex)
        sex2= sex_new[bt]
        #--------------------------------------------------------------------
        chestpain=['ATA', 'NAP', 'ASY', 'TA']
        chestpain1=[1, 2, 0, 3]
        chestpain_new=dict(zip(chestpain,chestpain1))
        bt1=st.radio('Chest pain type?',chestpain)
        chestpain2= chestpain_new[bt1]
        #--------------------------------------------------------------------
        s_slop=['Up', 'Flat', 'Down']
        s_slop1=[2, 1, 0]
        s_slop_new=dict(zip(s_slop,s_slop1))
        bt3=st.radio('ST_Slope?',s_slop)
        s_slop2= s_slop_new[bt3]
        #--------------------------------------------------------------------
    with col2:
        restingECG=['Normal', 'ST', 'LVH']
        restingECG1=[1, 2, 0]
        restingECG_new=dict(zip(restingECG,restingECG1))
        bt2=st.radio('Resting electrocardiographic results?',restingECG)
        restingECG2= restingECG_new[bt2]
        #--------------------------------------------------------------------
        ExerciseAngina=['N0', 'Yes']
        ExerciseAngina1=[0, 1]
        ExerciseAngina_new=dict(zip(ExerciseAngina,ExerciseAngina1))
        bt4=st.radio('Exercise angina?',ExerciseAngina)
        ExerciseAngina2= ExerciseAngina_new[bt4]
        #--------------------------------------------------------------------
        Fasting_BS=['N0', 'Yes']
        Fasting_BS1=[0, 1]
        Fasting_BS_new=dict(zip(Fasting_BS,Fasting_BS1))
        bt8=st.radio('Fasting blood suger more than 120 ?',Fasting_BS)
        Fasting_BS2= Fasting_BS_new[bt8]
        #--------------------------------------------------------------------
    with col3:
        bt5=st.slider('Age?', 1,90)
        #--------------------------------------------------------------------
        bt7=st.number_input('Cholesterol?',0,603)
        #--------------------------------------------------------------------
        bt6=st.number_input('Resting blood perssure?',0,200)
        #--------------------------------------------------------------------
        bt9=st.number_input('Maximum heart rate?',60,202)
        #--------------------------------------------------------------------
        #bt10=st.number_input('Old Peak?',-2,7)
        #-------------------------------------------------------------------
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
    df=pd.DataFrame({'Sex':sex2,'ChestPainType':chestpain2,
    'RestingECG':restingECG2,'ExerciseAngina':ExerciseAngina2,
    'ST_Slope':s_slop2,'Age':bt5,'RestingBP':bt6,
    'Cholesterol':bt7,'FastingBS':Fasting_BS2,'MaxHR':bt9,},index=[0])
    show= st.checkbox("Make sure you have filled in all fields")
    tab3.write("\n")
    tab3.write("\n")
    tab3.write("\n")
    if show:
        bt_predict=st.button("Predict...❗")
        if bt_predict:
            with st.spinner('Processing...🔄'):
                time.sleep(2)
                result=data.predict(df)
                if result == 0: 
                    tab3.header(' :blue[Patient Report :] ')
                    tab3.subheader('Inquiry About Heart Disease')
                    c1,= st.columns(1)
                    #_______
                    tab3.markdown("#### Sex :")
                    tab3.warning(bt)
                    #_______
                    tab3.markdown("#### Age :")
                    tab3.warning(bt5)
                    #_______
                    tab3.markdown('#### Chest Pain Type :')
                    tab3.warning(bt1)
                    #_______
                    tab3.markdown('#### Resting Electrocardiographic Results :')
                    tab3.warning(bt2)
                    #_______
                    tab3.markdown('#### ST_Slope :')
                    tab3.warning(bt3)
                    #_______
                    tab3.markdown('#### Exercise Angina :')
                    tab3.warning(bt4)
                    #_______
                    tab3.markdown('#### Resting Blood Pressure :')
                    tab3.warning(bt6)
                    #_______
                    tab3.markdown('#### Cholesterol :')
                    tab3.warning(bt7)
                    #_______
                    tab3.markdown('#### Fasting Blood Suger ?')
                    tab3.warning(bt8)
                    #_______
                    tab3.markdown('#### Maximum Heart Rate :')
                    tab3.warning(bt9)
                    #_______
                    #tab3.markdown('#### Old peak :')
                    #tab3.warning(bt10)
                    #_______
                    tab3.markdown('#### Degree Of Risk :')
                    tab3.success("LOW")
                    #_______
                    tab3.markdown('#### Query Result : ')
                    tab3.success("The patient is healthy, take care of yourself.")
                else:
                    tab3.header(':blue[Patient Report :]')
                    tab3.subheader(' Inquiry About Heart Disease')
                    c1,= st.columns(1)
                    #_______
                    tab3.markdown("#### Sex :")
                    tab3.info(bt)
                    #_______
                    tab3.markdown("#### Age :")
                    tab3.info(bt5)
                    #_______
                    tab3.markdown('#### Chest Pain Type :')
                    tab3.info(bt1)
                    #_______
                    tab3.markdown('#### Resting Electrocardiographic Results :')
                    tab3.info(bt2)
                    #_______
                    tab3.markdown('#### ST_Slope :')
                    tab3.info(bt3)
                    #_______
                    tab3.markdown('#### Exercise Angina :')
                    tab3.info(bt4)
                    #_______
                    tab3.markdown('#### Resting Blood Pressure :')
                    tab3.info(bt6)
                    #_______
                    tab3.markdown('#### Cholesterol :')
                    tab3.info(bt7)
                    #_______
                    tab3.markdown('#### Fasting Blood Suger ?')
                    tab3.info(bt8)
                    #_______
                    tab3.markdown('#### Maximum Heart Rate :')
                    tab3.info(bt9)
                    #_______
                    #tab3.markdown('#### Old peak :')
                    #tab3.info(bt10)
                    #_______
                    tab3.markdown('#### Degree Of Risk :')
                    tab3.error("High")
                    #_______
                    tab3.markdown('#### Query Result :')
                    tab3.error("The patient may requer attention, please go to the doctor.")
