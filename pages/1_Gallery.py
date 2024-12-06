import streamlit as st

st.columns(3)[1].markdown(""" # **Gallery** """)
st.divider()



def css_style():
    st.html('''<div class="photo">
        <div class="con1">
            <img src="https://images.pexels.com/photos/103286/pexels-photo-103286.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/849836/pexels-photo-849836.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/10248229/pexels-photo-10248229.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load">
            <img src="https://images.pexels.com/photos/18882375/pexels-photo-18882375/free-photo-of-blue-car-on-a-road-in-a-forest.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load">
            <img src="https://images.pexels.com/photos/27902450/pexels-photo-27902450/free-photo-of-vintage-chevrolet-camaro.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/1805053/pexels-photo-1805053.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/3156482/pexels-photo-3156482.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/1592384/pexels-photo-1592384.jpeg?auto=compress&cs=tinysrgb&w=600">
            <img src="https://images.pexels.com/photos/14330733/pexels-photo-14330733.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load">
        </div>
    </div>
    <style>
        .photo{
            margin-top: 50px;
            width: fit-content;
            border-radius: 80px;
            # background: linear-gradient(to right,rgba(0,0,0,0.5),rgba(0,0,0,0.3));
        }
        .con1{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        }
        .con1 img{
            padding: 2px;
            margin-left: 50px;
            margin-right: 50px;
            margin-top: 50px;
            width: 200px;
            height: 200px;
            border: 6px solid linear-gradient(to right,rgba(0,0,0,0.5),rgba(0,0,0,0.3));
            border-radius: 20px;
            box-shadow: 0px 0px 3px black,
            0px 0px 6px black,
            0px 0px 9px black; 
            transition: all 1.5s; 
        }
        .con1 img:hover{
            transform: scale(1.4);
            filter: grayscale(1);
            cursor: pointer;}</style>''')
    st.html('''<style>[data-testid="stSidebar"]{
        background:url('https://img.freepik.com/free-vector/evening-fog-tops-trees-pine-forest_1284-27059.jpg?uid=R171161164&ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');
        background-repeat: no-repeat;
        background-position: center;
        filter: grayscale(.7);
        border-top-right-radius: 30px;
        border-bottom-right-radius: 30px;
        box-shadow: rgba(0, 0, 0, .90) 0px 22px 60px 6px;
        background-size: cover;}</style>''')
    st.html('''<style>[data-testid="stSidebarNavLink"]:hover{
        background: white;
        color:black;}</style>''')
    st.html('''<style>
    [data-testid="stBaseButton-secondary"]{
        background:linear-gradient(to right,rgba(0,0,0,0.7),rgba(0,0,0,0.3));
        color: white;
        margin-top:50px;
        margin-left:100px;
        border-radius: 15px;
        width:100px;
        height:50px;}</style>''')

    st.html('''<style>
    [data-testid="stBaseButton-secondary"]:hover{
        transform: scale(1.1);
        transition:all .6s linear;}</style>''')
    st.html('''<style>
    [data-testid="stBaseButton-primary"]{
        background:linear-gradient(to right,rgba(0,0,0,0.7),rgba(0,0,0,0.3));
        color: white;
        margin-top:50px;
        border-radius: 15px;
        width:100px;
        height:50px;}</style>''')
    st.html('''<style>
    [data-testid="stBaseButton-primary"]:hover{
        transform: scale(1.1);
        transition:all .6s linear;}</style>''')

css_style()


def car_on_road():
    st.html('''<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAZrahFonz6MhOIWpkvpSTXO5LBNwPR4A5eQ&s" class="car">
    <style>
        .car{
            width: 90px;
            height: 50px;
            transition: all 5s linear;
            animation-name: rol;
            animation-duration: 5s;
            animation-iteration-count: infinite;
            animation-direction: alternate;
            
        }
        @keyframes rol {
            100%{
                transform: translateX(625px);
                
            } 
        }

    </style>''')

    st.html('''<div class="ball"></div>
    <style>
        .ball{
            width: 700px;
            margin-top: -30px;
            height: 20px;
            background: linear-gradient(to right,rgba(0,0,0,0.5),rgba(0,0,0,0.2));
            border-radius: 5px;
            # position: fixed;
        }
    </style>''')
st.write('')
st.write('')
st.write('')
car_on_road()
col1,col2,col3=st.columns(3)
with col1:
    ballon_btn=st.button('Ballon🎈')
with col3:
    snow_btn=st.button('Snow❄️',type='primary')
if ballon_btn:
    st.balloons()
if snow_btn:
    st.snow()

