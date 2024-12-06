import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.html('''<style>
    [data-testid="stSidebar"]{
        background:url('https://img.freepik.com/free-vector/evening-fog-tops-trees-pine-forest_1284-27059.jpg?uid=R171161164&ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');
        background-repeat: no-repeat;
        background-position: center;
        filter: grayscale(.7);
        border-top-right-radius: 30px;
        border-bottom-right-radius: 30px;
        box-shadow: rgba(0, 0, 0, .90) 0px 22px 60px 6px;
        background-size: cover;}</style>''')

st.html('''<style>
    [data-testid="stSidebarNavLink"]:hover{
        background: white;
        color:black;}</style>''')


st.columns(3)[1].markdown(""" # **About** 📄""")
st.divider()
def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
url='https://lottie.host/0908d5e3-34b5-4418-b933-5765a7ad9945/EM4lfxVwGe.json'
data=load(url)
st_lottie(data,key="Click",loop=True,width=670,height=400)
st.divider()
st.image('C:/Users/ukesh/OneDrive/Desktop/Python/icon_fin.jpg',width=100)
st.markdown(":violet[Hi there, I’m Ukesh! Currently, I am mastering the art of data science at Guvi. This website is my second project, created with the aim of helping users predict car prices using machine learning algorithms. By providing certain inputs, such as car features and specifications, you can estimate the price of a car with the power of data science.Enjoy exploring, and feel free to interact with the features on this site!.]")
st.markdown(":red[Quote of the day] : :green[Every expert was once a beginner 🎯]")
senti=st.feedback("faces")
selected=['Sad','Not satisfied','Satisfied','Happy','Extremly happy']
if senti:
    st.write(selected[senti])
if st.columns(5)[2].button("Know more",type="primary"):
    with st.chat_message("user"):
        def fd_btn():
            st.columns(3)[1].markdown(":green[Thanks for your feedback...!]")
            st.balloons()
        st.write(":green[This Website is not fully created and fully functional yet ,  if you do have any suggestions feel free to share it with me]:wave:")
        txt=st.text_area(label="Enter your Suggetions/feedback: ",max_chars=1000,placeholder="Feedback or suggestions ")
        btn=st.columns(5)[2].button("Submit",type="primary",on_click=fd_btn)
st.video('https://youtu.be/n4E117TygeI?si=IGXdp0_lMPssKkmB',loop=True,autoplay=True,subtitles=None,muted=False)
st.columns(3)[0].write(':copyright: App Deployed by :blue[ukesh]')


