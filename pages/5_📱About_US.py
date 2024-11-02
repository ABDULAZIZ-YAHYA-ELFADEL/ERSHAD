import streamlit as st
st.sidebar.info(" ### :blue[Your medical guide to detecting diseases] 🧐")
col1,col2, = st.columns(2, gap ="large")
with col1:
    st.image('img/aziz1.jpg', width=115)
    st.markdown("#### :blue[*ABDULAZIZ YAHYA ELFADEL*]")
    st.success("##### IT Fresh Graduate",icon="👨🏽‍🎓")
    st.success("##### phone: +249999927842",icon="📞")
    st.info('###### email: jenkez27842@gmail.com', icon="📩")
with col2:
    st.image('img/Brof.jpg', width=100)
    st.markdown("#### :blue[*AHMED MOHAMMED AWAD*]")
    st.success("##### IT Fresh Graduate",icon="👨🏽‍🎓")
    st.success("##### phone: +249119520553",icon="📞")
    st.info('###### email: moawadahmed690@gmail.com',icon="📩")    
col3, col4= st.columns(2, gap="large")
with col3:
    st.write("\n")
    st.image('img/ah.jpg', width=100)
    st.markdown("#### :blue[*AHMED ABDELRHMAN HAMID*]")
    st.success("##### IT Fresh Graduate",icon="👨🏽‍🎓")
    st.success("##### phone: +249113192027",icon="📞")
    st.info('###### email: ahmedabdelrhman7990@gmail.com',icon="📩")   
with col4:
    st.image('img/omran.jpg', width=100)
    st.markdown("#### :blue[OMRAN MOHAMAED ABASS]")
    st.success("##### IT Fresh Graduate",icon="👨🏽‍🎓")
    st.success("##### phone: +249124872587",icon="📞")
    st.info('###### email: OmranAbass0990@gmail.com',icon="📩") 