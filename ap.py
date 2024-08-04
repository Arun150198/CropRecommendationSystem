import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import pickle as pk
import json
from streamlit_lottie import st_lottie

pg_bg_img="""
<style>
[data-testid="stAppViewContainer"] {
background-image: url("crop.png");
background-size: cover;
}
</style>
"""

st.set_page_config(page_title='CROP_RECOMMENDATION_SYSTEM',layout='wide',page_icon='🌱')


attribution="""

- N - ratio of Nitrogen content in soil
- P - ratio of Phosphorous content in soil
- K - ratio of Potassium content in soil
- temperature - temperature in degree Celsius
- humidity - relative humidity in %
- ph - ph value of the soil
- rainfall - rainfall in mm
"""

st.markdown(pg_bg_img,unsafe_allow_html=True)

#horizontal menu :
selected=option_menu(
        menu_title='🌾CROP RECOMMENDATION SYSTEM¶🌾',
        options=['inf','predict'],
        icons=['info-circle-fill','person-circle'],
        menu_icon='🌾',
        orientation='horizontal',
        default_index=0,
        styles={
        "container": {"padding": "5!important","background-color":'#6AC6F7'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#8EF314"},
        "nav-link-selected": {"background-color": "white"},
            }                 
    )

if selected=='predict':
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color:#6AC6F7;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #0C0C0C ;
        color:#ff99ff;
        }
    </style>""", unsafe_allow_html=True)
    model=pk.load(open('model.pkl','rb'))
    with st.expander('Data fields'):
        st.markdown(attribution)
    p1,p2=st.columns(2)
    with p1:
        
        pp1,pp2,pp3=st.columns(3)
            
        with pp1:
            N=st.number_input('Nitrogen(N)',0,140)
            P=st.selectbox('Phosphorous(P)',range(5,145))
            K=st.selectbox('Potassium(K)',range(5,205))  
             
        with pp2:
            temperature=st.selectbox('Temperature',range(8,44)) 
            humidity=st.number_input('humidity',14,100)
            ph=st.selectbox('ph',range(3,10))
            
        with pp3:
            rainfall=st.selectbox('rainfall',range(20,299))
            if st.button('predict.'):
                with p2:
                    
                    
                    input_data_module=pd.DataFrame([[N,P,K,temperature,humidity,ph,rainfall]],
                    columns=['N','P','K','temperature','humidity','ph','rainfall']
                    )
                    with st.expander('View you selected Soil nutrien values'):
                        st.dataframe(input_data_module)
                    l1,l2=st.columns(2)
                    crop=model.predict(input_data_module)
                    if crop==1:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Rice 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('1.png',width=180)    
                    elif crop==2:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Maize 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('2.PNG',width=180)    
                    elif crop==3:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Chickpea 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('3.png',width=180)    
                    elif crop==4:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Kidneybeans 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('4.png',width=180)    
                    elif crop==5:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Pigeonpeas 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('5.png',width=180)    
                    elif crop==6:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Mothbeans 
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('6.png',width=180)    
                    elif crop==7:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Mungbean
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('7.png',width=180)    
                    elif crop==8:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Blackgram
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('8.png',width=180)    
                    elif crop==9:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Lentil
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('9.png',width=180)    
                    elif crop==10:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Pomegranate
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('10.png',width=180)    
                    elif crop==11:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Banana
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('11.png',width=180)    
                    elif crop==12:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Mango
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('12.png',width=180)    
                    elif crop==13:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Grapes
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('13.png',width=180)    
                    elif crop==14:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Blackgram
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('14.png',width=180)    
                    elif crop==15:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Muskmelon
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('15.png',width=180)    
                    elif crop==16:
                        st.write('apple')
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Apple
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('16.png',width=180)    
                    elif crop==17:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Orange
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('17.png',width=180)    
                    elif crop==18:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Papaya
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('18.png',width=180)    
                    elif crop==19:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Coconut
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('19.png',width=180)    
                    elif crop==20:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Cotton
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('20.png',width=180)    
                    elif crop==21:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - jute
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('21.png',width=180)    
                    elif crop==22:
                        l1.markdown("""
                                    Recommend Crop...         
                                    - Coffee
                                    Is the best crop to Be 
                                    cultivated right there""")
                        l2.image('22.png',width=180)    



if selected=='inf':
    with st.container():
        st.header('🎯 Objective')
        st.markdown("""
                    - Our project aims to create a small Crop Recommendation System that uses soil nutrient data to suggest the best crops for a specific farming area . 
                    - By using advanced machine learning . we want to help farmers choose the right crops. boosting productivity and sustainability .
                    - Our goal is to empower farmers with accurate recommendations for better harvests and efficient resource use. 
                    """)
    
    i1,i2=st.columns(2)
    with i1:
        st.subheader('🚀 Project Highlights:')
        st.markdown("""
                
                    - 🌿 Dataset: We've gathered comprehensive soil nutrient data, setting the foundation for our analysis.
                    - 🧐 Exploratory Data Analysis (EDA): Insights gained from EDA guided our understanding of the data's patterns and outliers.
                    - 🧹 Data Preprocessing: We meticulously cleaned and organized the data to ensure accuracy and reliability.
                    - 💡 Modeling: Advanced machine learning techniques were applied to build our intelligent recommendation system.
                    - 🌟 Results: Our efforts culminated in accurate crop recommendations that can empower farmers to enhance productivity and sustainability.

                    """)
        st.subheader('Conclusion...')
        st.markdown("""
                    - This machine learning model has been developed and traing historical data.
                    - As we can see RandomForestClassifier performing best (with accuracy 0.99)
                    - Model	                        Score
                    - 1	RandomForestClassifier	     99.31
                    - 2	Support Vector Classifer	 97.66
                    - 3	Desision_Tree_classification 97.66
                    - 4	KNeighborsClassifier	     97.38
                    - 5	Logistic_Regression	         92.29

                    """)
    with i2:
        lin_butt="""
        <style>
        .st-emotion-cache-1mcbg9u {
        background-color: #6AC6F7;
        }
        </style>
        
        """
        st.markdown(lin_butt,unsafe_allow_html=True)
        st.link_button('About-Me🌿','https://www.linkedin.com/in/muruga-perumal-iyadurai-7693592a7/')
        def get(path:str):
            with open(path,'r') as p:
                return json.load(p)
        path=get('./nani.json')
        st_lottie(path,height=300,width=600)
        
