document.addEventListener('DOMContentLoaded', function () {
    const getWeatherBtn = document.getElementById('getWeatherBtn');
    const weatherDataContainer = document.getElementById('weatherData');
    const cityInput = document.getElementById('city');

    getWeatherBtn.addEventListener('click', function () {
        const city = cityInput.value;
        
        // Make an AJAX request to the WeatherAPI.com endpoint
        fetch(`https://api.weatherapi.com/v1/current.json?key=61fdda5978b547f3bd2232525232309&q=${city}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    // Handle API errors
                    weatherDataContainer.innerHTML = `<p>${data.error.message}</p>`;
                } else {
                    // Extract weather data
                    const temperature = data.current.temp_c;
                    const conditions = data.current.condition.text;
                    const humidity = data.current.humidity;
                    const wind_speed = data.current.wind_kph;

                    // Update the HTML content with weather data
                    weatherDataContainer.innerHTML = `
                        <h2>Weather in ${city}:</h2>
                        <p>Temperature: ${temperature}°C</p>
                        <p>Conditions: ${conditions}</p>
                        <p>Humidity: ${humidity}%</p>
                        <p>Wind Speed: ${wind_speed} km/h</p>
                    `;
                }
            })
            .catch(error => {
                console.error('Error fetching weather data:', error);
                weatherDataContainer.innerHTML = '<p>Error fetching weather data</p>';
            });
    });
});
