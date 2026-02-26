# pip install streamlit

import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(layout='wide')

# Com uma visão mensal
# faturamento por unidade
# tipo de produto mais vendido, contribuição por filial
# Desempenho, formas de pgto...


#%% 

st.set_page_config(page_title= 'Dashboard', layout='wide')

st.title('Dashboard Supermarket Sales')


# streamlit run dashboards.py

# API details:
# API_KEY = "ae7aa6f59ead485b880111900252108"   # API usada na aula
# API_KEY = "28724b0ea5ea48298a0143142261902"
API_KEY = "coding-f7a8b9c1d2e3f4a5b6c7d8"
BASE_URL = "http://api.dashboardsapi.com/v1/current.json"

# Sidebar settings
st.sidebar.header("⚙️ Settings")
unit = st.sidebar.selectbox('Temperature Unit', ['Celsius','Farenheit'])
days = st.sidebar.slider('Forecast Days', min_value=1, max_value=7, value=3)  # up to 7 day forecast
show_humidity = st.sidebar.checkbox('Show Humidity', value=True)
show_wind = st.sidebar.checkbox('Show Wind Speed', value=True)

#%%
'''
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

'''

#%% CSV read


df = pd.read_csv('supermarket_sales.csv', sep=",", decimal=',')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(df['Date'])
df["Sales"] = pd.to_numeric(df["Sales"])





#%% CONTENT

df['Month'] = df['Date'].apply(lambda x:str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox('Mês', df['Month'].unique())

df_filtered = df[df['Month']== month]
df_filtered 

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x='Date', y='Sales', color='City', title='Faturamento por dia')
col1.plotly_chart(fig_date, use_container_widht=True)

fig_prod = px.bar(df_filtered, x='Date', y='Product line', color='City', title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(fig_date, use_container_widht=True)

city_total = df_filtered.groupby('City')[['Sales']].sum().reset_index()
fig_city = px.bar(df_filtered, x='City', y='Sales', title='Faturamento por filial')
col3.plotly_chart(fig_city, use_container_widht=True)

fig_kind = px.pie(df_filtered, values='Sales', names='Payment', title='Faturamento por tipo de pagamento')
col4.plotly_chart(fig_kind, use_container_widht=True)

fig_rating = px.pie(df_filtered, y='Rating', x='City', title='Avaliação')
col5.plotly_chart(fig_rating, use_container_widht=True)









        
        
        
        
        
        
        
        
        
        














