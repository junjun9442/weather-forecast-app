import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌦️")
st.title("🌦️ Simple Weather Forecast App")

# --- Input ---
city = st.text_input("Enter a city name:")

if st.button("Get Weather"):
    if city:
        api_key = "ddaf578b6644786504b664833f77b8f1"  # replace with your real API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            icon = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon}.png"

            st.image(icon_url)
            st.write(f"**Weather:** {weather}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind} m/s")
        else:
            st.error("City not found. Please try again.")
    else:
        st.warning("Please enter a city name.")
