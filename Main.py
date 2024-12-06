import streamlit as st 
import pandas as pd
import pickle
import numpy as np
import time



with open('Pipeline.pkl','rb') as fil:
    loaded=pickle.load(fil)

@st.cache_data
def read_data():
    data=pd.read_csv('cleaned_data.csv')
    return data
    

st.title(':red[Car price prediction]')


header="""<style>
    [data-testid="stHeader"]{
        background:rgba(0,0,0,0);
    
    }
</style>"""
st.markdown(header,unsafe_allow_html=True)




def css_style():
    st.html('''<style>
    h1{
        
        display: flex;
        align-items: center;
        justify-content: center;
        color: darkgray;
        font-weight: bolder;}</style>''')
    st.html('''<style>[data-testid="stMarkdownContainer"]{
        font-size: 20px;
        font-weight: bolder;
        color:white;}</style>''')
    st.html('''<style>[data-testid="stAppViewBlockContainer"]{
        background: linear-gradient(to right,rgba(0,0,0,0.9),rgba(0,0,0,0.6));
        border-radius: 5%;
        padding:80px;
        width: fit-content;}</style>''')
    st.html('''<style>[data-testid="stAppViewBlockContainer"]{
        cursor: pointer;
        box-shadow: rgba(0, 0, 0, 0.56) 0px 22px 70px 4px;
        transition: all .8s linear;}</style>''')
    st.html('''<style>
    button:hover{
        color: white;
        background:linear-gradient(to right,rgba(0,0,0,0.5),rgba(0,0,0,0.3));
        transform: translateY(-6px);
        transition: all 1s ease-in-out;}</style>''')
    st.html('''<style>[class="st-an st-ao st-ap st-aq st-ak st-ar st-am st-as st-at st-au st-av st-aw st-ax st-ay st-az st-b0 st-b1 st-b2 st-b3 st-b4 st-b5 st-b6 st-b7 st-b8 st-b9 st-ba st-bb st-bc"]:hover{
        background:linear-gradient(to right,rgba(0,0,0,0.5),rgba(0,0,0,0.3));
        cursor: pointer;}</style>''')


    

    st.html('''<style>
    [data-testid="stApp"]{
        background-image: url('https://img.freepik.com/free-vector/front-car-concept-illustration_114360-7978.jpg?uid=R171161164&ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');
        background-repeat: no-repeat;
        background-size: contain;
        background-position:center;
        opacity:1}</style>''')
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



def app(data):
    col1,col2,col3=st.columns(3)
    with col1:
        fuel=st.selectbox("# Select fuel type :",data['Fuel_type'].unique(),placeholder='Fuel type',index=None)
    with col3:
        body=st.selectbox("# Select body type :",data['Body_type'].unique(),placeholder='Body type',index=None)
    st.write('')
    st.write('')


    col4,col5,col6=st.columns(3)
    with col4:
        transmission=st.selectbox("# Select transmission type :",data['transmission'].unique(),placeholder='transmission type',index=None)
    with col6:
        brand=st.selectbox("# Select brand:",data['brand'].unique(),placeholder='Brand',index=None)
    st.write('')
    st.write('')


    col10,col11,col12=st.columns(3)
    with col10:
        owner=st.radio('# Select number of owners :',options=[0,1,2,3,4,5])
    with col12:
        mileage=st.number_input("# Mileage :",min_value=10,max_value=150,step=2)
        city=st.selectbox("# City :",data['city'].unique(),placeholder='city',index=None)
    st.write('')
    st.write('')
    model=st.selectbox("# Select car model :",data['model'].unique(),placeholder='Model',index=None)
    st.write('')
    st.write('')


    col7,col8,col9=st.columns(3)
    with col7:
        model_year=st.selectbox("# Select model year :",data['modelYear'].unique(),placeholder='Model year',index=None)
    with col9:
        insurance=st.selectbox("# Select Insurance type :",data['Insurance Validity'].unique(),placeholder='Insurance Validity',index=None)


    st.write('')   
    km_driven=st.slider("# Km's driven :",1000,550000,step=100)
    st.write('')
    st.write('')


    col13,col14,col15=st.columns(3)
    with col13:
        engine=st.selectbox("# Select Engine CC :",data['Engine'].unique(),placeholder='Engine CC',index=None)
    with col14:
        seat=st.selectbox("# Number of seats :",data['seat'].unique(),placeholder='seats',index=None)
    with col15:
        color=st.selectbox("# Select car color :",data['Color'].unique(),placeholder='car color',index=None)
    st.write('')
    st.divider()

    frame=pd.DataFrame({'Fuel_type':fuel,
                        'Body_type':body,
                        'transmission':transmission,
                        'ownerNo':owner,
                        'brand':brand,
                        'model':model,
                        'modelYear':model_year,
                        'Insurance Validity':insurance,
                        'Kms Driven':km_driven,
                        'Mileage':mileage,
                        'Engine':engine,
                        'seat':seat,
                        'Color':color,
                        'city':city},index=[1])
    
    button=st.columns(3)[1].button(' :red[Predict] 💵 ',use_container_width=True) 
    if button:
        with st.spinner('Predicting.....'):
            time.sleep(3)
        try:
            st.dataframe(frame,hide_index=True)
            output=loaded.predict(frame)
            st.success(f'The predicted price for {brand} with {engine}CC engine is : {np.round(output[0])} Lakhs')
        except:
            st.warning('Some values are missing kindly enter all values to predict the price...📋')

data=read_data()
app(data)
css_style()
