# pip install streamlit

import streamlit as st
import requests

st.set_page_config(page_title= 'Weather App', layout='wide')

st.title('🌤️ Live Weather App')

#%% Symbols:

# Sun/Clear: ☀️ (Sun), 🌞 (Sun with Face), 🌤️ (Sun behind Small Cloud).
# Clouds/Overcast: ☁️ (Cloud), ⛅ (Sun Behind Cloud), 🌥️ (Sun Behind Large Cloud), 🌫️ (Fog).
# Rain/Showers: 🌧️ (Cloud with Rain), 🌦️ (Sun Behind Rain Cloud), ☔ (Umbrella with Rain Drops).
# Storms/Wind: 🌩️ (Cloud with Lightning), 🌪️ (Tornado), 🌀 (Cyclone), 🌬️ (Wind Face).
# Cold/Snow: ❄️ (Snowflake), 🌨️ (Cloud with Snow), ☃️ (Snowman)

#%%    

# streamlit run Weather_app.py

# API details:
# API_KEY = "ae7aa6f59ead485b880111900252108"   # API usada na aula
# API_KEY = "28724b0ea5ea48298a0143142261902"
API_KEY = "coding-gaavyhivrruzjxiztm8jeg"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Sidebar settings
st.sidebar.header("⚙️ Settings")
unit = st.sidebar.selectbox('Temperature Unit', ['Celsius','Farenheit'])
days = st.sidebar.slider('Forecast Days', min_value=1, max_value=7, value=3)  # up to 7 day forecast
show_humidity = st.sidebar.checkbox('Show Humidity', value=True)
show_wind = st.sidebar.checkbox('Show Wind Speed', value=True)

#%%

city = st.text_input('Enter your city name: ')

if st.button("Get Weather") and city:
    url = f"{BASE_URL}/forecast.json?key={API_KEY}&q={city}&days={days}&aqi=yes&alerts=no"
#     url = f"{BASE_URL}key={API_KEY}&q={city}&aqi=no"
    r = requests.get(url)
    
    if r.status_code == 200:
        data = r.json()
        # Current Weather
        loc = data['location']['name']
        country = data['location']['country']
        temp = data['current']['temp_c']
        cond = data['current']['condition']['text']
        icon = 'https:'+ data['current']['condition']['icon']
        humidity = data['current']['humidity']
        wind = data['current']['wind_kph']
        
        
        st.subheader(f'{loc}, {country}')
        st.image(icon,width=80)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f'🌡️ Temperature: {temp} {unit[0]}')

        with col2:
            st.write(f'🌤️ Condition: {cond}')
        
        if show_humidity:
            st.write(f' Humidity: {humidity}%')
            
        if show_wind:
            st.write(f' Wind speed: {wind} kph')            


        st.markdown('---')
        
        st.header(f'📅 {days}- Days Forecast')
        
        forecast_day = data['forecast']['forecastday']
        
        for day in forecast_day:
            date = day['date']
            if unit == 'Celsius':
                min_temp = day['day']['mintemp_c']
                max_temp = day['day']['maxtemp_c']
            else:
                min_temp = day['day']['mintemp_f']
                max_temp = day['day']['maxtemp_f']
                
        condition = day['day']['condition']['text']
        icon_url = 'https:'+ day['day']['condition']['icon']
        
        
        col1, col2, col3, col4 = st.columns([2, 2, 2, 2])        
        with col1:
            st.write(f'📅 {date}')
        with col2:
            st.image(icon_url, width=50)
        with col3:
            st.write(f"🔻 Min: {min_temp}°{unit[0]}")
        with col4:
            st.write(f"🔺 Max: {max_temp}°{unit[0]}")            
        st.write(f'🌤️ {condition}')        
        st.markdown('---')
        
    else:
        st.error('City not found!')








        
        
        
        
        
        
        
        
        
        
        
            






