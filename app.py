from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your WeatherAPI.com API key
API_KEY = '61fdda5978b547f3bd2232525232309'

@app.route('/')
def index():
    return """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            width: 50%;
            margin: 0 auto;
            margin-top: 50px;
        }
        #city {
            padding: 8px;
            width: 60%;
            font-size: 16px;
        }
        #getWeatherBtn {
            padding: 8px 20px;
            font-size: 16px;
        }
        #weatherData {
            margin-top: 20px;
        }
        #error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Weather App</h1>
    <div class="container">
        <label for="city">Enter City: </label>
         <input type="text" id="city" placeholder="City">
         <button id="getWeatherBtn">Get Weather</button>
         <div id="weatherData"></div>
         <div id="error"></div>
     </div>
     <script src="static/script.js"></script>
 </body>
 </html>
     """
@app.route('/weather')
 def get_weather():
     city = request.args.get('city')
     if not city:
         return jsonify({'error': 'City parameter is missing'})
 
     # Validate the city name using geopy
     geolocator = Nominatim(user_agent="weather_app")
     location = geolocator.geocode(city)
     if not location:
         return jsonify({'error': 'Invalid city name'})
 
     # Make a request to WeatherAPI.com
     response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}')
 
     if response.status_code != 200:
         return jsonify({'error': 'Failed to retrieve weather data'})
 
     data = response.json()
 
     if 'current' not in data or 'temp_c' not in data['current']:
         return jsonify({'error': 'No weather information found for the city'})

    # Extract relevant weather data
     weather_data = {
        'temperature': data['current']['temp_c'],
         'conditions': data['current']['condition']['text'],
         'humidity': data['current']['humidity'],
         'wind_speed': data['current']['wind_kph']
    }

    return jsonify(weather_data)

if __name__ == '__main__':
