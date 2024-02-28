# Weather Script 🌦️🌦️🌦️🌦️🌦️🌦️

This script fetches weather data for current conditions and/or forecasts from the OpenWeatherMap API. It allows for the retrieval and processing of relevant weather information for a specific location.

## Usage🌤️🌤️🌤️🌤️🌤️🌤️🌤️🌤️

To use this script, follow these steps:

1. Clone the repository.
2. Set your OpenWeatherMap API key in the environment variable `OPENWEATHERMAP_API_KEY`.
3. Make sure you have Python installed on your machine.
4. Install the required dependencies using `pip install -r requirements.txt`.

## Getting Started⛈️⛈️⛈️⛈️⛈️⛈️⛈️

1. Obtain an API key from OpenWeatherMap and set it as the value for the `OPENWEATHERMAP_API_KEY` environment variable.
2. Run the script using `python weather_script.py`.
3. You will be prompted to either print the weather information to the console or save it to a file.

## ⛆⛆⛆⛆⛆Dependencies⛆⛆⛆⛆⛆

- `requests`
- `os`
- `datetime`
- `geocoder`

## Functionality⋆｡°•☁️⋆｡°•☁️⋆｡°•☁️⋆｡°•☁️

### `get_weather_data(location, api_key, days=1)`

Fetches weather data for current conditions and/or forecast.

- `location`: Location (city name or coordinates).
- `api_key`: OpenWeatherMap API key.
- `days`: Number of days for forecast (default: 1 for today only).

### `process_weather_data(data)`

Extracts and processes relevant weather information.

### `save_weather_to_file(data, location, forecast=False)`

Saves weather data to the 'weatherinfo.txt' file.

## Contributing🔥🔥🔥🔥🔥🔥🔥

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

