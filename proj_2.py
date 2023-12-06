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


def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    #st.markdown('Hii')
    import subprocess
    subprocess.run(["streamlit", "run", "proj_1.py"])


def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of Earth in kilometers (use 3959 for miles)

    return distance

def find_nearest_location(input_lat, input_lon, locations):
    nearest_location = None
    min_distance = float('inf')

    for location in locations:
        lat, lon = location
        distance = haversine(input_lat, input_lon, lat, lon)

        if distance < min_distance:
            min_distance = distance
            nearest_location = location

    return nearest_location

image = Image.open('/Users/sahanamanjunath/Downloads/girl-transformed.jpg')
st.markdown(f'<h1 style="color:#336BFF;font-size:45px;">{"BreezoScan"}</h1>', unsafe_allow_html=True)
st.markdown('**Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.**')
#st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
st.markdown("")
st.markdown("<p style='text-align:justify;'><strong>Welcome to our Air Quality Analyzer website. Our mission is to empower individuals, communities, and businesses with accurate and real-time data about the air they breathe. We understand the vital importance of clean air for overall well-being, and our advanced analyzers are designed to provide precise, actionable insights. Whether you're a concerned parent, an eco-conscious professional, or a city planner aiming for sustainable urban environments, our website serves as your comprehensive resource. Explore our website by clicking on the  following tabs to make informed decisions about your environment. Together, let's pave the way for a healthier, cleaner world.</strong></p>", unsafe_allow_html=True)



st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)










df_air=pd.read_csv('/Users/sahanamanjunath/Downloads/AQI and Lat Long of Countries.csv')

tabs = st.tabs(["About","Check Air Quality for current location",  "Check Air Quality for any desired location", "Check Global Air Quality data","Researcher Login","Bio"])

with tabs[0]:
    col1,col2=st.columns([4,1])
    with col1:
        st.markdown("<p style='text-align:justify;'>This segment furnishes comprehensive details about our website, addressing queries regarding its purpose, navigation guidelines, and clarification of essential terminology. Furthermore, users are offered a preview of our Air Quality data.</p>", unsafe_allow_html=True)
    image = Image.open('/Users/sahanamanjunath/Downloads/girl-transformed.jpg')
    st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
    col1,col2=st.columns([4,1])
    with col1:
        st.subheader('**Purpose**')
        st.markdown("<p style='text-align:justify;'>This website utilizes the Global Air Quality data to furnish valuable insights for both the general public and researchers. Users have the ability to access information about the air quality in their vicinity or any chosen location. Additionally, they can explore global air quality statistics, such as identifying the most polluted countries and observing the dispersion of pollutants worldwide.</p>", unsafe_allow_html=True)

        st.subheader('**Navigation Guidelines**')
        st.markdown("<p style='text-align:justify;'>This website caters to two distinct user categories :</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'><strong>Air Quality Enthusiasts :</strong><ul><li>Access features enabling the checking of air quality in both their local and specified regions.</li><li>Retrieve comprehensive information on global Air Quality data.</li></ul></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'><strong>Researchers :</strong><ul><li>Mandatory authorization is required for access to the confidential account page.</li><li>Access a dashboard offering in-depth global air quality analysis.</li><li>Privileged access to machine learning model predictions.</li><li>Authority to upload data into our database, contributing to the expansion of the Global Air Quality Index (AQI) database.</li></ul></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>The homepage features five tabs, each serving a specific function :</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'><ul><li><strong>About :</strong>Presents comprehensive information about the website, including explanations of jargons</li><li><strong>Check Air Quality for Current Location :</strong>Allows users to submit Air Quality data specific to their current region.</li><li><strong>Check Air Quality for Any Desired Region :</strong>Enables the users to retrieve information about the air quality in any chosen region, offering the flexibility to select both country and city.</li><li><strong>Check Global Air Quality Data :</strong>Provides users with a detailed overview of global Air Quality statistics.</li><li><strong>Researcher Login :</strong>Authorizes researchers to access the confidential account page, unlocking additional features for their use.</li></ul></p>", unsafe_allow_html=True)

    
    col1,col2=st.columns([4,1])
    with col1:
        st.subheader('**Learn about Air Quality Index**')
        st.markdown("<p style='text-align:justify;'>The Air Quality Index (AQI) is a numerical scale used to communicate how polluted the air currently is or how polluted it is forecast to become. It quantifies the concentration of specific air pollutants into a single number, which can help people understand the potential health impacts of breathing the air in a particular area. The pollutants commonly measured to calculate the AQI include:</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'><ul><li>Ground-level ozone (O3)</li><li>Particulate matter (PM2.5 and PM10)</li><li>Carbon monoxide (CO)</li><li>Nitrogen dioxide (NO2)</li></ul></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>The AQI scale typically ranges from 0 to 500, with lower values indicating better air quality and higher values indicating worse air quality. The scale is divided into different categories, each corresponding to a range of AQI values and indicating a different level of health concern. These categories are :</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'><ul><li>0-50 (Good): Air quality is considered satisfactory, and air pollution poses little or no risk.</li><li>51-100 (Moderate): Air quality is acceptable; however, some pollutants may be a concern for a small number of individuals who are sensitive to air pollution.</li><li>101-150 (Unhealthy for sensitive groups): Members of sensitive groups may experience health effects, but the general public is less likely to be affected.</li><li>151-200 (Unhealthy): Everyone may begin to experience adverse health effects, and members of sensitive groups may experience more serious effects.</li><li>201-300 (Very Unhealthy): Health alert! Everyone may experience more serious health effects.</li><li>301-500 (Hazardous): Health warnings of emergency conditions; the entire population is more likely to be affected.</li></ul></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>It's important to note that different countries might have their own AQI scales with slight variations in the pollutants measured and the corresponding health categories. The AQI is often reported by weather agencies and environmental organizations and is widely used to inform the public about air quality conditions in their area. People can use this information to make decisions to protect their health, such as reducing outdoor activities on days with poor air quality, especially for individuals with respiratory or heart conditions, children, and the elderly.", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("Curious about the Air Quality in your area? If yes, then go ahead and select the checkbox below and grant our website permission to access your location. If you are interested to check the Air Quality of a different region ? Then please select the 'Check Air Quality for any desired location' tab above")
   
    if st.checkbox('Allow the website to access my current location'):
        g = geocoder.ip('me')
        lat_me,lng_me=g.latlng
        lat_data = df_air['lat'].values
        lng_data = df_air['lng'].values
        locations = list(zip(lat_data, lng_data))
        lat,lng=find_nearest_location(lat_me, lng_me, locations)
        df_cc=df_air[(df_air['lat']==lat) & (df_air['lng']==lng)]
        country=list(df_cc['Country'].values)
        city=list(df_cc['City'].values)
        column1=country[0]
        column2=city[0]
        countries=list(df_air['Country'].unique())
        #st.markdown("**This page allows the user to examine the quality of the air in a particular region by selecting the country and city of their choice. To view the safe Air Quality Index (AQI) index levels, please refer to the AQI table below.**")
        #image = Image.open('/Users/sahanamanjunath/Downloads/aqi_table2.jpg')
        #st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
        col1,col2=st.columns(2)
        with col1:
            user_reg = column1
            st.metric("Current Country", value=user_reg)
        with col2:
            user_reg = column2
            st.metric("Current City", value=user_reg)
        df_city=df_air[(df_air['Country']==column1)]
        cities=list(df_city['City'].unique())
        
        df_aqi=df_air[(df_air['Country']==column1)& (df_air['City']==column2)]
        quality=list(df_aqi['AQI Category'])
        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Your Air Quality is : "}</h1>', unsafe_allow_html=True)
        air_results = list(df_aqi['AQI Category'])
        #st.metric("Overall Air Quality", value=user_casual[0])
        st.markdown(f'<h1 style="color:green;font-size:35px;">Overall Air Quality is : {air_results[0]}</h1>', unsafe_allow_html=True)
        #st.markdown(f'<h1 style="color:green;font-size:45px;">{}</h1>', unsafe_allow_html=True)
        
        col1,col2=st.columns(2)
        with col1:
            g = geocoder.ip('me')
            lat,lon=g.latlng
            df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [lat, lon],columns=['lat', 'lon'])
            st.map(df,color='#808080')

        with col2:  
            st.markdown("Want to know more about the air pollutants' contents ? Then please expand the below icon")
            with st.expander("Pollutants Information"):
                col1, col2 = st.columns(2)

                with col1:
                    value = str(list(df_aqi['CO AQI Value'])[0])+' - '+list(df_aqi['CO AQI Category'])[0]
                    st.metric("Carbonmonoxide Content", value=value)

                with col2:
                    value = str(list(df_aqi['NO2 AQI Value'])[0])+' - '+list(df_aqi['NO2 AQI Category'])[0]
                    st.metric("Nitrogendoxide Content", value=value)
                col3 , col4 = st.columns(2)
                with col3:
                    value = str(list(df_aqi['PM2.5 AQI Value'])[0])+' - '+list(df_aqi['PM2.5 AQI Category'])[0]
                    st.metric("Dust Particles Content", value=value)
                with col4:
                    value = str(list(df_aqi['Ozone AQI Value'])[0])+' - '+list(df_aqi['Ozone AQI Category'])[0]
                    st.metric("Ozone Content", value=value)
                class meter():
                    def draw_meter(self,a,b):
                        plt.figure(figsize=(2, 2))
                        data_per = [50,50,50,50,50,50]
                        #explode = (0, 0, 0.3, 0, 0, 0)
                        categories=['Good','Moderate','Unhealthy for SGs','Unhealthy','Very Unhealthy','Hazardous']
                    
                        plt.pie(data_per,  colors=['green','yellow','orange','red','purple','brown'])
                        #plt.legend(categories, loc='upper left')
                        circle = plt.Circle( (0,0), 0.7, color='white')
                        arrow=plt.arrow(0, -0.05, a, b, 
                                head_width = 0.2, 
                                width = 0.1,color='black')
                        p=plt.gcf()
                        p.gca().add_artist(circle)
                        p.gca().add_artist(arrow)
                        return p
                meter_placeholder = st

                col6,col7,col8=st.columns(3)

                with col6:
                    if quality[0]=='Good':
                        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Good"}</h1>', unsafe_allow_html=True)
                        m=meter()
                        meter_placeholder.pyplot(m.draw_meter(0.35,0.23))

                    elif quality[0]=='Moderate':
                        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Moderate"}</h1>', unsafe_allow_html=True)
                        m=meter()
                        meter_placeholder.pyplot(m.draw_meter(0,0.5))

                    elif quality[0]=='Unhealthy for Sensitive Groups':
                        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Unhealthy for sensitive groups"}</h1>', unsafe_allow_html=True)
                        m=meter()
                        meter_placeholder.pyplot(m.draw_meter(-0.35,0.23))

                    elif quality[0]=='Unhealthy':
                        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Unhealthy"}</h1>', unsafe_allow_html=True)
                        m=meter()
                        meter_placeholder.pyplot(m.draw_meter(-0.37,-0.14))

                    elif quality[0]=='Very Unhealthy':
                        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Very Unhealthy"}</h1>', unsafe_allow_html=True)
                        m=meter()
                        meter_placeholder.pyplot(m.draw_meter(0,-0.39))

                    elif quality[0]=='Hazardous':
                        #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Hazardous"}</h1>', unsafe_allow_html=True)
                        m=meter()
                        meter_placeholder.pyplot(m.draw_meter(0.35,-0.19))

                with col7:
                    image = Image.open('/Users/sahanamanjunath/Downloads/aqi_table2.jpg')
                    st.image(image,width=350)
                st.markdown('<p>To learn more about the pollutants, please visit this <a href="https://www.epa.gov/air-quality-management-process/managing-air-quality-air-pollutant-types#:~:text=They%20are%20particulate%20matter%20(often,environment%2C%20and%20cause%20property%20damage." target="_blank">website</a></p>', unsafe_allow_html=True)
        
        

with tabs[2]:
    countries=list(df_air['Country'].unique())
    st.markdown("This section allows the user to examine the quality of the air in a particular region. Please choose the desired country and city for which you want to check the air quality data.")
    #image = Image.open('/Users/sahanamanjunath/Downloads/aqi_table2.jpg')
    #st.image(image, caption='Breathing Innovation: Empowering Lives with Precision Air Quality Analysis.')
    
    column1 = st.selectbox("Choose Country", countries)
    df_city=df_air[(df_air['Country']==column1)]
    cities=list(df_city['City'].unique())
    column2 = st.selectbox("Choose City", cities)
    df_aqi=df_air[(df_air['Country']==column1)& (df_air['City']==column2)]
    quality=list(df_aqi['AQI Category'])
    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Your Air Quality is : "}</h1>', unsafe_allow_html=True)
    air_results = list(df_aqi['AQI Category'])
    #st.metric("Overall Air Quality", value=user_casual[0])
    st.markdown(f'<h1 style="color:green;font-size:35px;">Overall Air Quality is : {air_results[0]}</h1>', unsafe_allow_html=True)
    lat_m=list(df_aqi['lat'])[0]
    lng_m=list(df_aqi['lng'])[0]
    col1,col2=st.columns(2)
    with col1:
        df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [lat_m, lng_m],columns=['lat', 'lon'])
        st.map(df,color='#808080')

    with col2:  
        st.markdown("Want to know more about the air pollutants' contents? Then please expand the below icon")
        import streamlit as st

        st.markdown(
            """
        <style>
        [data-testid="stMetricValue"] {
            font-size: 20px;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )

        #st.metric(label="Dust Particles Content", value='Unhealthy for Sensitive Groups')
        with st.expander("Pollutants Information"):
            col1, col2 = st.columns(2)

            with col1:
                if list(df_aqi['CO AQI Category'])[0]=='Unhealthy for Sensitive Groups':
                    a='Unhealthy for SGs'
                else:
                    a=list(df_aqi['CO AQI Category'])[0]
                value = str(list(df_aqi['CO AQI Value'])[0])+' - '+a
                st.metric("Carbonmonoxide Content", value=value)

            with col2:
                if list(df_aqi['NO2 AQI Category'])[0]=='Unhealthy for Sensitive Groups':
                    a='Unhealthy for SGs'
                else:
                    a=list(df_aqi['NO2 AQI Category'])[0]
                value = str(list(df_aqi['NO2 AQI Value'])[0])+' - '+a
                st.metric("Nitrogendoxide Content", value=value)
            col3 , col4 = st.columns(2)
            with col3:
                if list(df_aqi['PM2.5 AQI Category'])[0]=='Unhealthy for Sensitive Groups':
                    a='Unhealthy for SGs'
                else:
                    a=list(df_aqi['PM2.5 AQI Category'])[0]
                value = str(list(df_aqi['PM2.5 AQI Value'])[0])+' - '+a
                st.metric("Dust Particles Content", value=value)
            with col4:
                if list(df_aqi['Ozone AQI Category'])[0]=='Unhealthy for Sensitive Groups':
                    a='Unhealthy for SGs'
                else:
                    a=list(df_aqi['Ozone AQI Category'])[0]
                value = str(list(df_aqi['Ozone AQI Value'])[0])+' - '+a
                st.metric("Ozone Content", value=value)
            class meter():
                def draw_meter(self,a,b):
                    plt.figure(figsize=(2, 2))
                    data_per = [50,50,50,50,50,50]
                    #explode = (0, 0, 0.3, 0, 0, 0)
                    categories=['Good','Moderate','Unhealthy for SGs','Unhealthy','Very Unhealthy','Hazardous']
                
                    plt.pie(data_per,  colors=['green','yellow','orange','red','purple','brown'])
                    #plt.legend(categories, loc='upper left')
                    circle = plt.Circle( (0,0), 0.7, color='white')
                    arrow=plt.arrow(0, -0.05, a, b, 
                            head_width = 0.2, 
                            width = 0.1,color='black')
                    p=plt.gcf()
                    p.gca().add_artist(circle)
                    p.gca().add_artist(arrow)
                    return p
            meter_placeholder = st

            col6,col7,col8=st.columns(3)

            with col6:
                if quality[0]=='Good':
                    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Good"}</h1>', unsafe_allow_html=True)
                    m=meter()
                    meter_placeholder.pyplot(m.draw_meter(0.35,0.23))

                elif quality[0]=='Moderate':
                    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Moderate"}</h1>', unsafe_allow_html=True)
                    m=meter()
                    meter_placeholder.pyplot(m.draw_meter(0,0.5))

                elif quality[0]=='Unhealthy for Sensitive Groups':
                    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Unhealthy for sensitive groups"}</h1>', unsafe_allow_html=True)
                    m=meter()
                    meter_placeholder.pyplot(m.draw_meter(-0.35,0.23))

                elif quality[0]=='Unhealthy':
                    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Unhealthy"}</h1>', unsafe_allow_html=True)
                    m=meter()
                    meter_placeholder.pyplot(m.draw_meter(-0.37,-0.14))

                elif quality[0]=='Very Unhealthy':
                    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Very Unhealthy"}</h1>', unsafe_allow_html=True)
                    m=meter()
                    meter_placeholder.pyplot(m.draw_meter(0,-0.39))

                elif quality[0]=='Hazardous':
                    #st.markdown(f'<h1 style="color:#336BFF;font-size:34px;">{"Air Quality is : Hazardous"}</h1>', unsafe_allow_html=True)
                    m=meter()
                    meter_placeholder.pyplot(m.draw_meter(0.35,-0.19))

            with col7:
                image = Image.open('/Users/sahanamanjunath/Downloads/aqi_table2.jpg')
                st.image(image,width=350)
            st.markdown('<p>To learn more about the pollutants, please visit this <a href="https://www.epa.gov/air-quality-management-process/managing-air-quality-air-pollutant-types#:~:text=They%20are%20particulate%20matter%20(often,environment%2C%20and%20cause%20property%20damage." target="_blank">website</a></p>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown("Ready to dive into fascinating facts about Global Air Quality? Whether you're an Air Quality Enthusiast or an Eco-conscious professional eager to uncover insights on the most polluted countries and worldwide pollutant patterns, you've landed in the perfect spot. Explore vibrant visualizations for a comprehensive view of global air quality!")
    countries=list(df_air['Country'].unique())
    cities=list(df_air['City'].unique())
    aqi=list(df_air['AQI Value'].unique())
    
    
    col4 , col5= st.columns(2)
    with col4:
        st.markdown(f'<p style="color:red;font-size:25px;">Top 5 polluted countries in the world</p>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>The following  visualization depicts the top 6 countries having hazardous air quality. It also gives information about the Air Quality index levels of each country. Air Quality Index is a numerical parameter used to measure the quality of air which ranges from 0-500 with lowest being the best air quality and highest being the worst.To know more about Air Quality Index (AQI) Please click on the ‘About' tab above</p>", unsafe_allow_html=True)
        AQI_Country =df_air.groupby('Country')['AQI Value'].agg(['mean', 'sum', 'max']).rename(columns={'mean':'Overall Air Quality Index','sum':'Overall_AQI','max':'Max_AQI'}).sort_values('Overall_AQI', ascending=False)
        for x in AQI_Country.columns:
            sns.set(font_scale=1.5)
            plt.figure(figsize=(16, 8))
            plt.xticks(rotation=45)
            st.pyplot(sns.barplot(
                data=AQI_Country .loc[:, [x]].reset_index().sort_values(x,ascending=False)[:5],
                x='Country',
                y=x).figure)
            

            break
    
    with col5:
        st.markdown(f'<p style="color:red;font-size:25px;">Top 5 countries in the world with best air quality</p>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>The following  visualization depicts the top 6 countries having best air quality. It also gives information about the Air Quality index levels of each country. Air Quality Index is a numerical parameter used to measure the quality of air which ranges from 0-500 with lowest being the best air quality and highest being the worst.To know more about Air Quality Index (AQI) Please click on the ‘About' tab above</p>", unsafe_allow_html=True)
        AQI_Country =df_air.groupby('Country')['AQI Value'].agg(['mean', 'sum', 'max']).rename(columns={'mean':'Overall Air Quality Index','sum':'Overall_AQI','max':'Max_AQI'}).sort_values('Overall_AQI', ascending=True)
        for x in AQI_Country.columns:     
            sns.set(font_scale=1.5)
            plt.figure(figsize=(16, 8))
            plt.xticks(rotation=45)
            st.pyplot(sns.barplot(
                data=AQI_Country .loc[:, [x]].reset_index().sort_values(x,ascending=True)[:5 ],
                x='Country',
                y=x).figure)
            
            
            break
            
   

    
    col8,col9=st.columns(2)
    with col8:
        st.markdown(f'<p style="color:red;font-size:25px;text-align:justify;">Check the proportion of air quality for each country</p>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>Air quality is classified into categories such as Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, and Hazardous.(For more information, Please refer to the ‘About’ section). The following chart illustrates the proportion of such air quality categories in each country. Select the country for which you'd like to view the air quality distribution. Our reports indicate that densely populated countries, such as China and India, exhibit bad air quality across their cities.</p>", unsafe_allow_html=True)
        countries=list(df_air['Country'].unique())
        column5 = st.selectbox("Choose any Country", countries)
        df_country=df_air[df_air['Country']==column5]
        plt.figure(figsize=(20,10))
        fig=px.pie(values=df_country['AQI Value'], names=df_country['AQI Category'])
        st.plotly_chart(fig, theme="streamlit")

        


    with col9:
        st.markdown(f'<p style="color:red;font-size:25px;">Explore the global dispersion of air pollutants.</p>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>The four major air pollutants affecting the quality of air are Ozone, Carbonmonoxide (CO), Nitrogendioxide (NO2) and Dust particles (PM 2.5). The following visualization shows the pollutants’ spread world wide. According to our reports, The Carbomonoxide and Nitrogendioxide are in safe levels across the globe. However, Asian countries are at threat due to unsafe levels of other pollutants in most of their cities. These issues must be addressed before they become hazardous for the nations.</p>", unsafe_allow_html=True)
        column1 = st.selectbox("Please select any air pollutant",('Dust Particles','Ozone','Carbon Monoxide','Nitrogen dioxide'))
    
        if column1=='Carbon Monoxide':
            pollutant_name='CO AQI Category'
        elif column1=='Nitrogen dioxide':
            pollutant_name='NO2 AQI Category'
        elif column1=='Ozone':
            pollutant_name='Ozone AQI Category'
        elif column1=='Dust Particles':
            pollutant_name='PM2.5 AQI Category'
            pollutant_name='AQI Category'
            if column1=='Carbon Monoxide':
                pollutant_name='CO AQI Category'
            elif column1=='Nitrogen dioxide':
                pollutant_name='NO2 AQI Category'
            elif column1=='Ozone':
                pollutant_name='Ozone AQI Category'
            elif column1=='Dust Particles':
                pollutant_name='PM2.5 AQI Category'
            


        scatterplot = sns.scatterplot(data=df_air, x=df_air['lng'], y=df_air['lat'], hue=df_air[pollutant_name])
        scatterplot.figure.set_size_inches(scatterplot.figure.get_size_inches()[0], 12)
        st.pyplot(scatterplot.figure)

def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    #st.markdown('Hii')
    import subprocess
    subprocess.run(["streamlit", "run", "researcher.py"])

with tabs[4]:
    with st.form(key='login_form'):
        st.subheader('Login Credentials')
        username = st.text_input('**Please enter your username:**')
        st.markdown('Default username: user')
        
        password = st.text_input('**Please enter your password:**', type='password')
        st.markdown('Default password: password')
        login_button = st.form_submit_button('Login')
        if login_button:
            if not username or not password:
                st.error("Please enter the credentials to login")
        if login_button:
            if username and password:
                # Based on the credentials login is redirected
                if not (username == 'user' and password == 'password'):
                    st.error("Invalid username/ password")
                if (username == 'user' and password == 'password'):                    
                    st.success('Login Successful!')
                    st.markdown(f'<a href="https://aqiproject-dcbypjgtfn7bexqbfcnbin.streamlit.app"><button>Go to Researcher Account page</button> </a>', unsafe_allow_html=True)
   


with tabs[5]:
    col1,col2=st.columns((2,1))
    
    with col1:
        st.markdown("<p style='text-align:justify;'>Hi everyone! I'm Sahana, a passionate individual with a keen interest in the fascinating world of data science. As a data science enthusiast, I thrive on turning raw data into meaningful insights and actionable strategies. My journey in this field has been an exciting exploration of analytics, problem-solving, and the ever-evolving landscape of data.Proficient in programming languages such as Python and R, I am always eager to embrace new technologies and methodologies to stay ahead in the dynamic field of data science.</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>Beyond the realm of data analytics, I find joy in the simple pleasures of life. One of my favorite pastimes is immersing myself in the world of movies. Whether it's a classic film or the latest blockbuster, I appreciate the art of storytelling and the emotions that movies evoke. It's a great way for me to unwind and draw inspiration from various narratives.In addition to being a movie buff, I have a flair for culinary adventures. Cooking is not just a hobby for me; it's a creative outlet where I experiment with flavors and techniques. Exploring diverse cuisines and crafting delicious meals bring a different kind of satisfaction to my life outside the world of data.</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:justify;'>Feel free to explore my web app and join me on this exciting journey of data exploration and analytics.</p>", unsafe_allow_html=True)
    with col2:
        image = Image.open('/Users/sahanamanjunath/Downloads/me2.jpeg')
        st.image(image,width=200)


    
    
    

        




