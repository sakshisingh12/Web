import streamlit as st
import hydralit_components as hc
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

menu_data = [
    {'label':"About Me"},
    {'label':"Skills"},
    {'label':"Projects"},
    {'label':"Contact"},
]

#soverride = st.selectbox('Menu override',[31,10,20,30,31,32,33,40,0,81])
menu_id = hc.nav_bar(menu_definition=menu_data,key='PrimaryNav')

if menu_id == "" or menu_id == "About Me":
    st.markdown("""
        <style>
        .big-font {
            font-size:25px !important;
            font-family: 'Times New Roman', Times, serif;
            width: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Hello, nice to meet you!<br> I am Sakshi, Sophomore at Indian Institute of Information Technology Vadodara-International Campus Diu, I am interested in Scientific Programming, Mathematics, Algorithms, Data Science and Machine Learning. I love doing adventures, like travelling, tracking, rapelling, hill-climbing etc. Currently I am learning Julia, Machine Learning and Algorithms Analysis. I am the part of various communities who supports unrepresented groups in technology. I would like to make a change in world for better!</p>',
        unsafe_allow_html=True
    )

if menu_id == "Skills":
    skill_type = st.multiselect(
        "Choose the Skill Type",
        ("Programming Languages", "Machine Learning", "Web-Frameworks", "Softwares")
    )
    if skill_type.__contains__("Programming Languages"):
        with st.container():
            st.subheader("Python")
            my_bar = st.progress(96)
            st.subheader("Java")
            my_bar = st.progress(90)
            st.subheader("Julia")
            my_bar = st.progress(90)
            st.subheader("Dart")
            my_bar = st.progress(96)

    if skill_type.__contains__("Machine Learning"):
        with st.container():
            st.subheader("Tensorflow")
            my_bar = st.progress(80)
            st.subheader("PyTorch")
            my_bar = st.progress(84)
            st.subheader("scikit-learn")
            my_bar = st.progress(83)
            st.subheader("Dataframes.jl")
            my_bar = st.progress(84)

    if skill_type.__contains__("Web-Frameworks"):
        with st.container():
            st.subheader("Flask")
            my_bar = st.progress(80)
            st.subheader("Django")
            my_bar = st.progress(80)
            st.subheader("React")
            my_bar = st.progress(70)

    if skill_type.__contains__("Softwares"):
        with st.container():
            st.subheader("MATLAB")
            my_bar = st.progress(80)
            st.subheader("Octave")
            my_bar = st.progress(80)
            st.subheader("Git")
            my_bar = st.progress(90)
    
    if len(skill_type) == 0:
        st.subheader("Python")
        my_bar = st.progress(96)
        st.subheader("Java")
        my_bar = st.progress(90)
        st.subheader("Julia")
        my_bar = st.progress(90)
        st.subheader("Dart")
        my_bar = st.progress(96)
        st.subheader("Tensorflow")
        my_bar = st.progress(80)
        st.subheader("PyTorch")
        my_bar = st.progress(84)
        st.subheader("scikit-learn")
        my_bar = st.progress(83)
        st.subheader("Dataframes.jl")
        my_bar = st.progress(84)
        st.subheader("Flask")
        my_bar = st.progress(80)
        st.subheader("Django")
        my_bar = st.progress(80)
        st.subheader("React")
        my_bar = st.progress(70)
        st.subheader("MATLAB")
        my_bar = st.progress(80)
        st.subheader("Octave")
        my_bar = st.progress(80)
        st.subheader("Git")
        my_bar = st.progress(90)


if menu_id == "Projects":
    st.markdown("""
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        </head>
        <div class="row row-cols-1 row-cols-md-2 g-4">
            <div class="col" id="left">
              <div class="card">
                <img src="https://lightifyapp.herokuapp.com/static/images/Rectangle%203.be81bf65f735.png" class="card-img-top" alt="...">
                <div class="card-body">
                  <h2 class="card-title">Lightify
                    <a href="https://github.com/Barenyakumar/lightify"><button class = "btn"style="font-size:24px"><i class="fa fa-github"></i></button></a>
                    <a href="https://lightifyapp.herokuapp.com/"><button class = "btn"style="font-size:24px"><i class="fa fa-link"></i></button></a>
                  </h2>
                  <p class="card-text">Lightify is platform which helps visually impaired students to get
                    writers/scribes and give online exams. This application includes a audio quiz with real time speech
                    recognition and registration platform for students and scribes.
                  </p>
                </div>
              </div>
            </div>
            <div class="col" id="right">
              <div class="card">
                <img src="https://freepngimg.com/thumb/pokemon/37475-6-pikachu-transparent-image.png" class="card-img-top" alt="...">
                <div class="card-body">
                  <h2 class="card-title">Get Your PokeMon
                    <a href="https://github.com/sakshisingh12/pokemon"><button class = "btn"style="font-size:24px"><i class="fa fa-github"></i></button></a>
                    <a href="https://pokemon-a26c5.web.app/"><button class = "btn"style="font-size:24px"><i class="fa fa-link"></i></button></a>
                  </h2>
                  <p class="card-text"> Get Your Pokemon is website which helps us to know more
                      about our favourite Pokemon. It includes around 100 different pokemon cards
                      and each card contains pokemon details. I have made this website using PokeApi 
                      and JavaScript.
                  </p>
                </div>
              </div>
            </div>
            <div class="col" id="left">
              <div class="card">
                <img src="https://images.firstpost.com/wp-content/uploads/2021/03/Bitcoin-Ether-Cryptocurrency-min.jpg" class="card-img-top" alt="...">
                <div class="card-body">
                  <h2 class="card-title">Crypto Tracker
                    <a href="https://github.com/sakshisingh12/sakshisingh12.github.io"><button class = "btn"style="font-size:24px"><i class="fa fa-github"></i></button></a>
                    <a href="https://sakshisingh12.github.io/"><button class = "btn"style="font-size:24px"><i class="fa fa-link"></i></button></a>
                  </h2>
                  <p class="card-text">Crypto Tracker is a website which gives us real time prize of 
                      popular crypto-currency in comparison to INR currency. I have build this website 
                      using coinranking api and JavaScript.
                  </p>
                </div>
              </div>
            </div>
            <div class="col" id="right">
              <div class="card">
                <img src="https://empire-s3-production.bobvila.com/slides/43321/original/small_house_decor.jpg" class="card-img-top" alt="...">
                <div class="card-body">
                  <h2 class="card-title">House Finder 
                      <a href="https://github.com/sakshisingh12/Project"><button class = "btn"style="font-size:24px"><i class="fa fa-github"></i></button></a>
                </h2>
                  <p class="card-text">House Finder is a C program which tells us about the 
                      house according to buyer's needs and budgets. This also helps buyers to 
                      choose house as per their comfort level.
                  </p>
                </div>
              </div>
            </div>
          </div>
    </html>
    """, unsafe_allow_html=True)

    st.markdown("""
       <style>
           img{
               height: 400px;
           }
           .card-text, .card-title{
               color: black;
           }
           .btn{
               background-color: white;
               border: white;
           }
           #left{
               padding-left: 10%;
               padding-right: 2.5%;
               padding-top: 5%;
           }
           #right{
               padding-left: 2.5%;
               padding-right: 10%;
               padding-top: 5%;
           }
       </style>
    """, unsafe_allow_html=True)


if menu_id == "Contact":
    st.markdown("""
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        </head>
        <div class="container">
        <a href="https://www.linkedin.com/in/sakshisingh125/"><button class = "btn"style="font-size:50px"><i class="fa fa-linkedin"></i></button></a>
        <a href="https://github.com/sakshisingh12"><button class = "btn"style="font-size:50px"><i class="fa fa-github"></i></button></a>
        <a href="https://twitter.com/SakshiSingh127"><button class = "btn"style="font-size:50px"><i class="fa fa-twitter"></i></button></a>
        </div>
    </html>
    <style>
        .container{
            margin-top: 10%;
            text-align: center;
            background-color: #0E1117;
        }
        .btn{
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)
