import requests
import os
from datetime import datetime, timedelta
import geocoder 

def get_weather_data(location, api_key, days=1):
    """Fetches weather data for current conditions and/or forecast.

    Args:
        location (str): Location (city name or coordinates).
        api_key (str): OpenWeatherMap API key.
        days (int, optional): Number of days for forecast (default: 1 for today only).
    """

    if days == 1:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    else:
        # Using coordinates for more reliable forecast if available
        try:
            g = geocoder.ip('me')
            coords = g.latlng
            url = f"https://api.openweathermap.org/data/2.5/onecall?lat={coords[0]}&lon={coords[1]}&exclude=current,minutely,hourly,alerts&appid={api_key}"
        except Exception:  # Fallback to city name
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        return None  # Indicate an error

    return data 

def process_weather_data(data):
    """Extracts and processes relevant weather information."""

    if 'weather' in data:  # Current conditions
        return {
            'temp': data['main']['temp'] - 273.15,
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    elif 'daily' in data:  # Forecast
        forecast = []
        for day in data['daily'][:5]:  # Get next 5 days
            forecast.append({
                'date': datetime.fromtimestamp(day['dt']).strftime('%d %b %Y'),
                'temp': day['temp']['day'] - 273.15,
                'description': day['weather'][0]['description']
            })
        return forecast 

def save_weather_to_file(data, location, forecast=False):
    """Saves weather data to the 'weatherinfo.txt' file."""
    
    with open("wetherinfo.txt", "w+") as f: 
        f.write(f"Weather Stats for - {location.upper()} || {datetime.now().strftime('%d %b %Y | %I:%M:%S %p')}\n")
        f.write("-------------------------------------------------------------\n")

        if forecast:
            for day in data:
                f.write(f"Date: {day['date']}\n")
                f.write(f"Temperature:  {day['temp']:.2f} °C\n")
                f.write(f"Description:  {day['description']}\n")
                f.write("-------------------------\n")
        else:  
            f.write(f"Current Temperature: {data['temp']:.2f} °C\n")
            f.write(f"Current weather desc: {data['description']}\n")
            f.write(f"Current Humidity: {data['humidity']} %\n")
            f.write(f"Current wind speed: {data['wind_speed']} km/h \n")


def main():
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if api_key is None:
        print("Error: API key not found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
        return  # Exit the program

    # Get location (attempt geolocation first)
    try:
        g = geocoder.ip('me')
        location = g.city
    except Exception:
        location = input("Enter the city name: ")

    # Get weather data
    weather_data = get_weather_data(location, api_key)

    if weather_data is None:
        print("Invalid location or API error. Please try again.")
        return

    # Ask for output preference
    output_choice = input("Print to console or save to file? (console/file): ")

    if output_choice.lower() == 'file':
        save_weather_to_file(weather_data, location)
        print("Weather information saved to 'weatherinfo.txt'")
    else:  # Print to console
        print_weather_info(weather_data)

if __name__ == "__main__":
    main()
