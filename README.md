# Voice-Based Weather App

This project is a voice-based weather application built with Flask, SpeechRecognition, and OpenWeatherMap API. It allows users to retrieve weather information for a specific city and state using voice commands.

## Features

- Speech recognition for inputting city and state information
- Real-time weather data retrieval from OpenWeatherMap API
- Conversion of temperature from Kelvin to Fahrenheit
- User-friendly interface for easy interaction

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sajeevsingh/Weather-App.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `'YOUR_API_KEY'` in `app.py` with your actual API key.

4. Run the Flask app:

    ```bash
    python app.py
    ```

## Usage

1. Open the application in your web browser.
2. Speak the name of the city you want to get weather information for when prompted.
3. Speak the state abbreviation when prompted.
4. The application will display the weather information on the webpage.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request


