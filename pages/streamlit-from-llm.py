#
# Prompt:
# Generate a streamlit app which downloads the weather temperatures for the twin cities of minnesota and 
# plots the temperatures on a map and on a line chart where the x axis is the days. 
#

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API settings
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Twin cities coordinates
cities = {
    'Minneapolis': {'lat': 44.9778, 'lon': -93.2650},
    'St. Paul': {'lat': 44.9537, 'lon': -93.0900},
}

@st.cache_data
def fetch_weather(city):
    params = {
        'lat': city['lat'],
        'lon': city['lon'],
        'units': 'metric',
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

st.title('Twin Cities Weather Data')

# Fetch and plot data
for city_name, coordinates in cities.items():
    data = fetch_weather(coordinates)
    st.write(data)
    continue
    temps = [entry['main']['temp'] for entry in data['list']]
    time = [entry['dt_txt'] for entry in data['list']]

    df = pd.DataFrame({'Temperature': temps}, index=pd.to_datetime(time))

    st.subheader(f"Weather for {city_name}")
    st.map({'lat': [coordinates['lat']], 'lon': [coordinates['lon']], 'Temperature': temps[:1]})
    
    st.line_chart(df)
