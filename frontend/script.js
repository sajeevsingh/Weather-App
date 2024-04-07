document.getElementById('weather-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const city = document.getElementById('city').value.trim();
    const state = document.getElementById('state').value.trim();

    try {
        const response = await fetch('/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city, state })
        });

        if (!response.ok) {
            throw new Error('City not found');
        }

        const data = await response.json();
        const weatherInfo = `The weather in ${data.city} is ${data.weather}. The temperature is ${data.temp}°F, feels like ${data.feels_like}°F.`;
        document.getElementById('weather-info').textContent = weatherInfo;
    } catch (error) {
        document.getElementById('weather-info').textContent = error.message;
    }
});