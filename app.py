from flask import Flask, request, jsonify
import requests

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
        </head>
        <body>
            <h1>Weather App</h1>
            <div>
                <label for="city">Enter City: </label>
                <input type="text" id="city" placeholder="City">
                <button id="getWeatherBtn">Get Weather</button>
            </div>
            <div id="weatherData">
                <!-- Weather data will be displayed here -->
            </div>
            <script src="static/script.js"></script>
        </body>
        </html>
        """

@app.route('/weather')
def get_weather():
        city = request.args.get('city')

        # Make a request to WeatherAPI.com
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}')
        data = response.json()

        # Extract relevant weather data
        weather_data = {
            'temperature': data['current']['temp_c'],
            'conditions': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }

        return jsonify(weather_data)

if __name__ == '__main__':
        app.run(debug=True)


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Make a request to WeatherAPI.com
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}')
    data = response.json()

    # Extract relevant weather data
    weather_data = {
        'temperature': data['current']['temp_c'],
        'conditions': data['current']['condition']['text'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph']
    }

    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)
