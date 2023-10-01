from flask import Flask, render_template, request, jsonify
import requests
from configparser import ConfigParser

app = Flask(__name__)

def get_weather(city):
    api_file = 'weather_key.txt'
    file_a = ConfigParser()
    file_a.read(api_file)
    api_key = file_a['api_key']['key']
    url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

    response = requests.get(url_api)
    if response.status_code == 200:
        weather_data = response.json()

        # Convert temperature from Kelvin to Celsius and Fahrenheit
        temperature_in_kelvin = weather_data['main']['temp']
        temperature_in_celsius = temperature_in_kelvin - 273.15
        temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32

        weather_data['main']['temp_celsius'] = round(temperature_in_celsius, 2)
        weather_data['main']['temp_fahrenheit'] = round(temperature_in_fahrenheit, 2)

        return weather_data
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    city = request.args.get('city')
    weather_data = get_weather(city)
    if weather_data:
        return render_template('weather_partial.html', weather_data=weather_data)
    else:
        return jsonify({'error': 'Weather data not found'}), 404

@app.route('/cities')
def cities():
    city_list = [
        {"name": "New York", "country": "US"},
        {"name": "Los Angeles", "country": "US"},
        {"name": "Chicago", "country": "US"},
        {"name": "London", "country": "UK"},
        {"name": "Paris", "country": "France"},
        {"name": "Berlin", "country": "Germany"},
        {"name": "Toronto", "country": "Canada"},
        {"name": "Sydney", "country": "Australia"},
        {"name": "Tokyo", "country": "Japan"},
        {"name": "Beijing", "country": "China"},
        {"name": "Moscow", "country": "Russia"},
        {"name": "Rio de Janeiro", "country": "Brazil"},
        {"name": "Mumbai", "country": "India"},
        {"name": "Cairo", "country": "Egypt"},
        {"name": "Cape Town", "country": "South Africa"},
        {"name": "Rome", "country": "Italy"},
        {"name": "Athens", "country": "Greece"},
        {"name": "Seoul", "country": "South Korea"},
        {"name": "Mexico City", "country": "Mexico"},
        {"name": "Bangkok", "country": "Thailand"},
        {"name": "Dubai", "country": "UAE"},
        {"name": "Havana", "country": "Cuba"},
        {"name": "Lima", "country": "Peru"},
        {"name": "Stockholm", "country": "Sweden"},
        {"name": "Oslo", "country": "Norway"},
        {"name": "Helsinki", "country": "Finland"},
        {"name": "Amsterdam", "country": "Netherlands"},
        {"name": "Warsaw", "country": "Poland"},
        {"name": "Bangalore", "country": "India"},
        {"name": "Santiago", "country": "Chile"},
        {"name": "Nairobi", "country": "Kenya"},
        {"name": "Dublin", "country": "Ireland"},
        {"name": "Buenos Aires", "country": "Argentina"},
        {"name": "Jakarta", "country": "Indonesia"},
        {"name": "Singapore", "country": "Singapore"},
        {"name": "Kuala Lumpur", "country": "Malaysia"},
        {"name": "Zurich", "country": "Switzerland"},
        {"name": "Vienna", "country": "Austria"},
        {"name": "Brussels", "country": "Belgium"},
        {"name": "Madrid", "country": "Spain"},
        {"name": "Prague", "country": "Czech Republic"},
        {"name": "Budapest", "country": "Hungary"},
        {"name": "Copenhagen", "country": "Denmark"},
        {"name": "Lisbon", "country": "Portugal"},
        {"name": "Wellington", "country": "New Zealand"},
        {"name": "Auckland", "country": "New Zealand"},
        {"name": "Edinburgh", "country": "UK"},
        {"name": "Munich", "country": "Germany"},
        {"name": "Kyoto", "country": "Japan"},
        {"name": "St. Petersburg", "country": "Russia"},
        {"name": "Brasília", "country": "Brazil"},
        {"name": "Alexandria", "country": "Egypt"},
        {"name": "Osaka", "country": "Japan"},
        {"name": "Nagoya", "country": "Japan"},
        {"name": "Marrakech", "country": "Morocco"},
        {"name": "Florence", "country": "Italy"},
        {"name": "Panama City", "country": "Panama"},
        {"name": "Cologne", "country": "Germany"},
        {"name": "Casablanca", "country": "Morocco"},
        {"name": "Edmonton", "country": "Canada"},
        {"name": "Bogotá", "country": "Colombia"},
        {"name": "Hanoi", "country": "Vietnam"},
        {"name": "Johannesburg", "country": "South Africa"},
        {"name": "Reykjavik", "country": "Iceland"},
        {"name": "Chennai", "country": "India"},
        {"name": "Karachi", "country": "Pakistan"},
        {"name": "Lahore", "country": "Pakistan"},
        {"name": "Islamabad", "country": "Pakistan"},
        {"name": "Colombo", "country": "Sri Lanka"},
        {"name": "Dhaka", "country": "Bangladesh"},
        {"name": "Kathmandu", "country": "Nepal"},
        {"name": "Thimphu", "country": "Bhutan"},
        {"name": "Malé", "country": "Maldives"}
    ]
    return jsonify(city_list)

if __name__ == "__main__":
    app.run(debug=True)
