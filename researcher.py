import streamlit as st
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import hiplot as hip
from streamlit import runtime
from streamlit_option_menu import option_menu
from math import radians, sin, cos, sqrt, atan2
import geocoder


# Set page config to wide layout
st.set_page_config(layout="wide")
# Set the background image

#'https://images.unsplash.com/photo-1687120096244-ca75c057e5ef?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY5NzU2ODI1NA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080'
# CSS styles
bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://images.unsplash.com/photo-1687120096244-ca75c057e5ef?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY5NzU2ODI1NA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080');
background-size: cover;
background-repeat: no-repeat;
}
</style>
'''
#https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17
#https://www.gettyimages.ca/detail/photo/splashed-with-fresh-air-royalty-free-image/1127069296?adppopup=true
#WQD6TCLOozg
#st.markdown(bg_img, unsafe_allow_html=True)
#st.title('Air Quality Analysis')
#st.markdown(f'<h1 style="color:#336BFF;font-size:45px;">{"BreezoScan"}</h1>', unsafe_allow_html=True)
#st.markdown('**Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.**')
#st.markdown("**Celebrating Clean Air: Welcome to our revolutionary Air Quality Analyzer website. Our mission is to empower individuals, communities, and businesses with accurate and real-time data about the air they breathe. We understand the vital importance of clean air for overall well-being, and our advanced analyzers are designed to provide precise, actionable insights. Whether you're a concerned parent, an eco-conscious professional, or a city planner aiming for sustainable urban environments, our website serves as your comprehensive resource. Explore our website to make informed decisions about your environment. Together, let's pave the way for a healthier, cleaner world.**")


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#336BFF;margin-top: 40px;">
  <a class="navbar-brand" href="#" target="_blank">BreezoScan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
   
  </div>
</nav>
""", unsafe_allow_html=True)


def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    import subprocess
    subprocess.run(["streamlit", "run", "proj_2.py"])


#if st.sidebar.markdown(f'<a href="https://example.com"><button>Go back to Home Page</button> </a>', unsafe_allow_html=True):
#    pass

st.sidebar.markdown(f'<h1 style="color:#336BFF;font-size:25px;">{"Welcome to BreezoScan advanced research page"}</h1>', unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:justify;'>This page offers a platform for researchers to conduct sophisticated analyses on Air Quality Index parameters. Additionally, it furnishes details about the data, enables researchers to upload new data, and facilitates the prediction of the air quality index based on other influential features.</p>",unsafe_allow_html=True)
if st.sidebar.button('Logout'):
    redirect_to_streamline()

df_air=pd.read_csv('/Users/sahanamanjunath/Downloads/AQI and Lat Long of Countries.csv')

tabs = st.tabs(["About Air Quality Index(AQI) Data",  "Air Quality Index Prediction", "Upload new Air Quality Index (AQI) Data to Database", "Key takeaways from recent analysis"])


with tabs[0]:
    st.markdown("<p style='text-align:justify;'>The Global Air Quality dataset is collected from the kaggle website 'World Air Quality Index by City and Coordinates'. It considers four major air pollutants namely Carbon monoxide, Nitrogen dioxide, Ozone and PM2.5 which are used to calculate the Air Quality Index of a particular region.</p>",unsafe_allow_html=True)
    col1 , col2, col3 = st.columns(3)
    countries=list(df_air['Country'].unique())
    cities=list(df_air['City'].unique())
    aqi=list(df_air['AQI Value'].unique())
    with col1:
        num_countries = len(countries)
        st.metric("No of Countries for which AQI data is available", value=num_countries)
    with col2:
        num_cities = len(cities)
        st.metric("No of cities for which AQI data is available", value=num_cities)
    with col3:
        avg_aqi = int(np.mean(aqi))
        st.metric("Average Global AQI Value", value=avg_aqi)
    
    
    st.write(df_air)
    st.markdown("## In depth relationship between pollutants and Air Quality Index")
    st.markdown("Hover over each row in the following table to see the relationship between all the pollutants and Air Quality Index")
    print(f"HiPlot=={hip.__version__}")
    df_air_new=df_air[['PM2.5 AQI Value','NO2 AQI Value','CO AQI Value','Ozone AQI Value','AQI Category','AQI Value']]
    exp=hip.Experiment.from_dataframe(df_air_new)
    exp_html=exp.to_html()
    st.components.v1.html(exp_html,height=1400)

    

def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    #st.markdown('Hii')
    import subprocess
    subprocess.run(["streamlit", "run", "researcher.py"])
    
with tabs[1]:
    
    st.markdown('In this segment, researchers can input diverse values for air pollutants data pertaining to a specific region. Subsequently, our sophisticated machine learning models predict the overall Air Quality Index (AQI) value.')
    countries=list(df_air['Country'].unique())
    country_value = st.selectbox("Choose Country", countries)
    df_city=df_air[(df_air['Country']==country_value)]
    cities=list(df_city['City'].unique())
    city_value = st.selectbox("Choose City", cities)
    co_value = st.slider("CO Value", min_value=0, max_value=500, step=1)
    ozone_value = st.slider("Ozone Value", min_value=0, max_value=500, step=1)
    no2_value = st.slider("NO2 Value", min_value=0, max_value=500, step=1)
    pm25_value = st.slider("Dust particles Value", min_value=0, max_value=500, step=1)

    df_aqi=df_air[(df_air['Country']==country_value)& (df_air['City']==city_value)]
    lat=list(df_aqi['lat'])[0]
    lng=list(df_aqi['lng'])[0]


    def fetch_category(value):
        if 0<=value<=50:
            return 0
        elif 51<=value<=100:
            return 1
        elif 101<=value<=150:
            return 2
        elif 151<=value<=200:
            return 3
        elif 201<=value<=300:
            return 4
        elif value>=301:
            return 5
    

        
    ozone_category=fetch_category(ozone_value)   
    no2_category=fetch_category(no2_value)   
    pm25_category=fetch_category(pm25_value) 
    co_category=fetch_category(co_value) 

    test_data = {'CO AQI Value': [co_value], 'CO AQI Category': [co_category], 'Ozone AQI Value': [ozone_value], 'Ozone AQI Category': [ozone_category], 'NO2 AQI Value': [no2_value], 'NO2 AQI Category': [no2_category], 'PM2.5 AQI Value': [pm25_value],
        'PM2.5 AQI Category': [pm25_category],'lat':[lat],'lng':[lng]}
    df_test = pd.DataFrame(test_data)

    from sklearn.preprocessing import StandardScaler
    import joblib
    import pickle


    loaded_scaler = joblib.load('scaler_model.joblib')
    loaded_scaled_data = joblib.load('scaled_data.joblib')
    X_test_scaled = loaded_scaler.transform(df_test)

    # Load the pickled model
    with open('model_reg1.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    predictions = loaded_model.predict(X_test_scaled)

    print(int(predictions))

    v=fetch_category(predictions[0])
    print(v)
    
          
    
    ## Create a button
    if st.button('Predict Satsfication', help='Click to predict satisfaction'):
        predictions = loaded_model.predict(X_test_scaled)

        predicted_aqi_value=int(predictions)
        
        predicted_aqi_category=fetch_category(predicted_aqi_value)
        
        if predicted_aqi_category == 0:
            pred = "Good"
        elif predicted_aqi_category == 1:
            pred = "Moderate"
        elif predicted_aqi_category == 2:
            pred = "Unhealthy for Sensitive Groups"
        elif predicted_aqi_category == 3:
            pred = "Unhealthy"
        elif predicted_aqi_category == 4:
            pred = "Very Unhealthy"
        elif predicted_aqi_category == 5:
            pred = "Hazardous"
        
        ## Display Results
        st.success(f'Predicted Air Quality is : {(pred.title())}')
        st.success(f'Predicted Air Quality Index is : {(predicted_aqi_value)}')
        
        
with tabs[2]:
    st.markdown("<p style='text-align:justify;'>This section allows the researchers to upload new data to the Global Air Quality Index (AQI) database. Please ensure that the files adhere to the correct format. Refer to the 'About Air Quality Index (AQI) data' section for more detailed information about the dataset.</p>",unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Please upload the test data in csv file format", type=["csv"])

    if uploaded_file is not None:
        # File upload successful
        

        # Process the uploaded file (you can customize this part based on your needs)
        try:
            
            df = pd.read_csv(uploaded_file)
            columns_equal = list(df.columns) == list(df_air.columns)
            df_equal = df.equals(df_air)
            if columns_equal and df_equal:
                st.success("File uploaded successfully to the database!")
                st.write("Uploaded Data:")
                st.write(df)
            else:
                st.error('Data mismatch')
                
              
            
            # Display the uploaded data
            
            
            # Add further processing or analysis as needed
        except Exception as e:
            st.error(f"Error reading the file: {e}")

with tabs[3]:
    #Summary Report by Researcher Section creation
    st.markdown("**Kindly view the information presented by our esteemed analysts, we present an analysis of the Air Quality Index (AQI) data collected on October 3rd, 2023, from various countries using our Air Sampling equipment. The findings indicate alarming trends in air quality across the globe.**")
    bullet_points = [
    "**Notably, cities in Korea and Bahrain are experiencing the most severe air pollution, falling under the 'Hazardous' category, while cities in Palau and Maldives boast the best air quality standards.**",
    "**A concerning pattern emerges in populous countries like India and China, where cities with large populations and extensive manufacturing plants exhibit extremely poor air quality levels.**",
    "**Geographically, Asia demonstrates the poorest air quality, contrasting with the Pacific region, which boasts the best AQI ratings.**",
    "**Our visual analysis of Air Quality Index categories reveals a direct correlation between Dust Particles and the Air Quality Index, indicating a linear relationship. Conversely, understanding the connection between CO and NO2 pollutants proves challenging when their levels are below 50. However, once these levels surpass 50, they are classified as 'Unhealthy' or 'Hazardous.'**",
    "**Particularly alarming is the prevalence of Dust particles and Ozone pollutants, both exhibiting high Air Quality Index values and falling within the 'Unhealthy' to 'Hazardous' range. These pollutants pose a significant threat to human health, especially impacting the respiratory system.**",
    "**On a slightly positive note, the spread of Carbon Monoxide and Nitrogen Dioxide pollutants, while present, does not pose a significant hazard globally. In contrast, Dust Particles and Ozone are widespread and pose a substantial threat to Asian countries, exacerbating their air quality challenges.**"
    ]
    bullet_points_formatted = "\n".join([f"- {item}" for item in bullet_points])
    st.markdown(bullet_points_formatted)


    
    
    

        




