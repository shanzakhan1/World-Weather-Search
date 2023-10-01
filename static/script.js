const searchButton = document.getElementById('searchButton');
const weatherResults = document.getElementById('weatherResults');
const cityInput = document.getElementById('cityInput');
const cityList = document.getElementById('cityList');

searchButton.addEventListener('click', fetchWeather);
cityInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        fetchWeather();
    }
});

fetch('/cities')
    .then(response => response.json())
    .then(data => {
        data.forEach(city => {
            const cityCountry = `${city.name}, ${city.country}`;
            const cityOption = document.createElement('option');
            cityOption.value = cityCountry;
            cityList.appendChild(cityOption);
        });
    })
    .catch(error => {
        console.error('Error fetching city data:', error);
    });

function fetchWeather() {
    const city = cityInput.value.trim();
    if (city === '') {
        alert('Please enter a valid city name.');
        return;
    }

    fetch(`/weather?city=${city}`)
        .then(response => response.text())
        .then(data => {
            weatherResults.innerHTML = data;
        })
        .catch(error => {
            console.error('Error fetching weather:', error);
            alert('An error occurred while fetching weather data.');
        });
}
