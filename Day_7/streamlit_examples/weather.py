import streamlit as st
import requests
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered"
)

# Title and description
st.title("🌤️ Weather Dashboard")
st.markdown("Enter a city name to get current weather information")

# Sidebar for API key input
with st.sidebar:
    st.header("Configuration")
    st.markdown("Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)")
    
    # API Key input (with password masking)
    api_key = st.text_input("Enter your OpenWeatherMap API Key:", type="password")
    
    if api_key:
        st.success("API Key saved!")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app uses OpenWeatherMap API to display current weather conditions for any city.")
    
    # Add some example cities
    st.markdown("### Example Cities")
    example_cities = ["London", "New York", "Tokyo", "Paris", "Sydney", "Mumbai"]
    selected_example = st.selectbox("Try an example:", [""] + example_cities)

# Main content
city = st.text_input("🏙️ Enter City Name:", value=selected_example if selected_example else "")

# Function to get weather data
def get_weather_data(city_name, api_key):
    """Fetch weather data from OpenWeatherMap API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use metric units (Celsius)
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None
    except KeyError:
        st.error("Invalid API key or city not found")
        return None

# Function to get weather icon
def get_weather_icon(weather_id):
    """Return appropriate emoji based on weather condition"""
    if weather_id >= 200 and weather_id < 300:  # Thunderstorm
        return "⛈️"
    elif weather_id >= 300 and weather_id < 400:  # Drizzle
        return "🌧️"
    elif weather_id >= 500 and weather_id < 600:  # Rain
        return "🌧️"
    elif weather_id >= 600 and weather_id < 700:  # Snow
        return "❄️"
    elif weather_id >= 700 and weather_id < 800:  # Atmosphere
        return "🌫️"
    elif weather_id == 800:  # Clear
        return "☀️"
    elif weather_id > 800:  # Clouds
        return "☁️"
    else:
        return "🌈"

# Display weather data when city is entered and API key is provided
if city and api_key:
    with st.spinner(f"Fetching weather data for {city}..."):
        weather_data = get_weather_data(city, api_key)
    
    if weather_data and weather_data.get('cod') == 200:
        # Extract weather information
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        description = weather_data['weather'][0]['description']
        weather_id = weather_data['weather'][0]['id']
        wind_speed = weather_data['wind']['speed']
        country = weather_data['sys']['country']
        city_name = weather_data['name']
        
        # Get weather icon
        weather_icon = get_weather_icon(weather_id)
        
        # Create columns for layout
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Temperature", f"{temp:.1f}°C")
        
        with col2:
            st.metric("Feels Like", f"{feels_like:.1f}°C")
        
        with col3:
            st.metric("Humidity", f"{humidity}%")
        
        # Main weather display
        st.markdown(f"## {weather_icon} Weather in {city_name}, {country}")
        st.markdown(f"### {description.capitalize()}")
        
        # Additional weather information in columns
        col4, col5, col6 = st.columns(3)
        
        with col4:
            st.metric("Wind Speed", f"{wind_speed} m/s")
        
        with col5:
            st.metric("Pressure", f"{pressure} hPa")
        
        with col6:
            # Get sunrise and sunset times
            if 'sys' in weather_data:
                sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M')
                sunset = datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M')
                st.metric("Sunrise", sunrise)
                st.metric("Sunset", sunset)
        
        # Add a visual separator
        st.markdown("---")
        
        # Display additional details in an expander
        with st.expander("📊 More Details"):
            st.json(weather_data)
            
    elif weather_data and weather_data.get('cod') != 200:
        error_message = weather_data.get('message', 'Unknown error')
        st.error(f"Error: {error_message}")
        
elif not api_key:
    st.warning("⚠️ Please enter your OpenWeatherMap API key in the sidebar.")
elif city:
    st.warning("⚠️ Please enter both city name and API key.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and OpenWeatherMap API")