import streamlit as st 
import pandas as pd 
import pickle
import time
data1= pickle.load(open("Models/depression_disease.sav",'rb'))
#-----------------------------------------------------------------------------
st.sidebar.info(" ### :blue[Your medical guide to detecting diseases] 🧐")
tab1, tab2, tab3= st.tabs(['| About Depression |','| About Model |','| Depression Test |'])

tab1.image('img/2.webp', width=300)

tab1.markdown("##### Depression is a mental state of low mood and aversion to activitty, which affects more than :red[280 million] people of all ages. Medically classified as a mental and behavioral disorder, the experience of depression affects a persons thoughts, behavior, motivations, feelings, and sense of well-being.")
tab1.info('##### Doctors diagnose depression based on symptoms, so the diagnosis may include subjecting the affected person to a general physical examination, and a psychological evaluation, where the mental health doctor asks the affected person a set of question, regarding symptoms, thoughts, feelings, and behavior patterns.')  
tab1.info('##### One recently published study showed that friendship protects you from depression. Friends also help reduce the risk of heart disease and strengthen the immune system. Friends are a protection against stress and depression.')


#---------------------------------------------------------------------------
tab2.info('##### Model accuracy : :green[99%] ')
tab2.markdown("### The attributes :")
tab2.info('###### 1-Age: Choose your age group. ')
tab2.info('###### 2-Feeling sad: Do you feel sad? ')
tab2.info('###### 3-Irritable towards peoplee: Do you react quickly to peoples actions? ')
tab2.info('###### 4-Trouble sleeping at night: Do you have problems with sleeping?')
tab2.info('###### 5-Problems concentrating or making decision: Do you have difficulty concentrating and making decisions? ')
tab2.info('###### 6-loss of appetite: Loss of appetite for eating?')
tab2.info('###### 7-Feeling of guilt: Do you feel of gilt?')
tab2.info('###### 8-Problems of bonding with people: Do you have problems establishing relationships with people?')
tab2.info('###### 9-Suicide attempt: Do you have previous attempts to commit suicide?')
#--------------------------------------------------------------------------
tab3.markdown('### :red[🚩 This test is valid for people who have these  symptoms for a long period of time, one or two months.]')
tab3.write("\n")
with tab3.form('form'):
    col1,col2,col3,= st.columns(3, gap="small")
    with col1:
        Age=['25-30', '30-35', '35-40', '40-45', '45-50']
        Age1=[0, 1, 2, 3, 4]
        Age_new=dict(zip(Age,Age1))
        bt=st.radio('Age Group?', Age)
        Age2= Age_new[bt]
        #--------------------------------------------------------------------
        Feeling_sad=['Yes', 'No', 'Sometimes']
        Feeling_sad1=[2, 0, 1]
        Feeling_sad_new=dict(zip(Feeling_sad,Feeling_sad1))
        bt2=st.radio('Feeling sad ?', Feeling_sad)
        Feeling_sad2= Feeling_sad_new[bt2]
        #-------------------------------------------------------------------
        Irritable_towards_peoplee=['Yes', 'No', 'Sometimes']
        Irritable_towards_peoplee1=[2, 0, 1]
        Irritable_towards_peoplee_new=dict(zip(Irritable_towards_peoplee,Irritable_towards_peoplee1))
        bt3=st.radio('Irritable_towards_peoplee ?', Irritable_towards_peoplee)
        Irritable_towards_peoplee2= Irritable_towards_peoplee_new[bt3]
        #--------------------------------------------------------------------
    with col2:
        Problems_concentrating=['Yes', 'No', 'Often']
        Problems_concentrating1=[2, 0, 1]
        Problems_concentrating_new=dict(zip(Problems_concentrating,Problems_concentrating1))
        bt5=st.radio('Problems concentrating or making decision ?', Problems_concentrating)
        Problems_concentrating2= Problems_concentrating_new[bt5]
        #--------------------------------------------------------------------
        loss_of_appetite=['Yes', 'No', 'Not at all']
        loss_of_appetite1=[2, 0, 1]
        loss_of_appetite_new=dict(zip(loss_of_appetite,loss_of_appetite1))
        bt6=st.radio('loss of appetite ?', loss_of_appetite)
        loss_of_appetite2= loss_of_appetite_new[bt6]
        #--------------------------------------------------------------------
        Feeling_guilt=['No', 'Yes', 'Maybe']
        Feeling_guilt1=[1, 2, 0]
        Feeling_guilt_new=dict(zip(Feeling_guilt,Feeling_guilt1))
        bt7=st.radio('Feeling of guilt ?', Feeling_guilt)
        Feeling_guilt2= Feeling_guilt_new[bt7]
        #--------------------------------------------------------------------
    with col3:
        Trouble_sleeping=['Two or more days a week', 'No', 'Yes']
        Trouble_sleeping1=[1, 0, 2]
        Trouble_sleeping_new=dict(zip(Trouble_sleeping,Trouble_sleeping1))
        bt4=st.radio('Trouble sleeping at night ?', Trouble_sleeping)
        Trouble_sleeping2= Trouble_sleeping_new[bt4]
        #-------------------------------------------------------------------
        Problems_of_bonding=['Yes', 'Sometimes', 'No']
        Problems_of_bonding1=[2, 1, 0]
        Problems_of_bonding_new=dict(zip(Problems_of_bonding,Problems_of_bonding1))
        bt8=st.radio('Problems of bonding with people ?', Problems_of_bonding)
        Problems_of_bonding2= Problems_of_bonding_new[bt8]
        #--------------------------------------------------------------------
        Suicide_attempt=['Yes', 'No', 'Not interested to say']
        Suicide_attempt1=[2, 0, 1]
        Suicide_attempt_new=dict(zip(Suicide_attempt,Suicide_attempt1))
        bt9=st.radio('Suicide attempt ?', Suicide_attempt)
        Suicide_attempt2= Suicide_attempt_new[bt9]
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        #--------------------------------------------------------------------
    df1=pd.DataFrame({'Age':Age2, 'Feeling sad':Feeling_sad2, 'Irritable towards people':Irritable_towards_peoplee2,
     'Trouble sleeping at night':Trouble_sleeping2, 'Problems concentrating or making decision':Problems_concentrating2,
      'loss of appetite':loss_of_appetite2, 'Feeling of guilt':Feeling_guilt2, 'Problems of bonding with people':Problems_of_bonding2,
      'Suicide attempt':Suicide_attempt2,},index=[0])
    bt_predict=st.form_submit_button("Predict...❗")
if bt_predict:
        with st.spinner('Processing...🔄'):
            time.sleep(2)
            result=data1.predict(df1)
            if result == 0:
                tab3.header(' :blue[Patient Report :]')
                tab3.subheader(' Inquiry About  Depression ')
                c1,= st.columns(1)
                #_______
                tab3.markdown("####  Age Group :")
                tab3.warning(bt)
                #_______
                tab3.markdown("####  Feeling sad ? ")
                tab3.warning(bt2)
                #_______
                tab3.markdown('####  Irritable towards people ?')
                tab3.warning(bt3)
                #_______
                tab3.markdown('####  Trouble sleeping at night ?')
                tab3.warning(bt4)
                #_______
                tab3.markdown('#### Problems concentrating or making decision ? ')
                tab3.warning(bt5)
                #_______
                tab3.markdown('####  loss of appetite ?')
                tab3.warning(bt6)
                #_______
                tab3.markdown('####  Feeling of guilt ?')
                tab3.warning(bt7)
                #_______
                tab3.markdown('####  Problems of bonding with people ?')
                tab3.warning(bt8)
                #_______
                tab3.markdown('#### Suicide attempt ?')
                tab3.warning(bt9)
                #_______
                tab3.markdown('#### Degree Of Risk :')
                tab3.success("LOW")
                #_______
                tab3.markdown('#### Query Result :')
                tab3.success("The patient is healthy, take care of  yourself.")
            else:
                tab3.header(' :blue[Patient Report :]')
                tab3.subheader(' Inquiry About  Depression ')
                c1,= st.columns(1)
                #_______
                tab3.markdown("####  Age Group :")
                tab3.info(bt)
                #_______
                tab3.markdown("####  Feeling sad ? ")
                tab3.info(bt2)
                #_______
                tab3.markdown('####  Irritable towards people ?')
                tab3.info(bt3)
                #_______
                tab3.markdown('####  Trouble sleeping at night ?')
                tab3.info(bt4)
                #_______
                tab3.markdown('#### Problems concentrating or making decision ? ')
                tab3.info(bt5)
                #_______
                tab3.markdown('####  loss of appetite ?')
                tab3.info(bt6)
                #_______
                tab3.markdown('####  Feeling of guilt ?')
                tab3.info(bt7)
                #_______
                tab3.markdown('####  Problems of bonding with people ?')
                tab3.info(bt8)
                #_______
                tab3.markdown('#### Suicide attempt ?')
                tab3.info(bt9)
                #_______
                tab3.markdown('#### Degree Of Risk : ')
                tab3.error("High")
                #_______
                tab3.markdown('#### Query Result : ')
                tab3.error("The patient may requer attention, please go to the doctor.")