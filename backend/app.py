from flask import Flask, render_template, request, jsonify
from urllib.parse import quote
import json
import pyttsx3
import speech_recognition as sr
from urllib.request import urlopen
import os

app = Flask(__name__)

# Set the path to the templates folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app.template_folder = template_dir

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_input(prompt, confirm=False):
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    r.energy_threshold = 4000
    r.pause_threshold = 0.8

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        speak(prompt)
        try:
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            text = r.recognize_google(audio, language='en-US')

            if confirm:
                speak(f"Did you say {text}? Please say yes or no.")
                print("Listening...")
                confirmation = r.listen(source, timeout=5, phrase_time_limit=5)
                confirmation_text = r.recognize_google(confirmation).lower()

                if "yes" in confirmation_text:
                    return text
                else:
                    speak("Let's try again.")
                    return None

            else:
                return text
        except sr.UnknownValueError:
            speak("Sorry I did not understand that. Please try again")
            return None
        except sr.RequestError as e:
            speak("Could not request results; please check your internet connection")
            return None
        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return None

def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit_temp = (9/5) * (kelvin_temp - 273.15) + 32
    return round(fahrenheit_temp)

def get_weather(city, state):
    encoded_city = quote(city)
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={encoded_city},{state},US&appid=7dc34849d7e8b6fbdcb3f12454c92e88"
    response = urlopen(complete_url)
    rawWeatherData = response.read().decode('utf-8')
    weatherData = json.loads(rawWeatherData)

    if weatherData["cod"] != "404":
        weather = weatherData["weather"][0]["description"]
        temp = weatherData["main"]["temp"]
        fahrenheit_temp = kelvin_to_fahrenheit(temp)
        feels_like = weatherData["main"]["feels_like"]
        fahrenheit_feels_like = kelvin_to_fahrenheit(feels_like)
        weather_info = f"The weather in {city} is {weather}. The temperature is {fahrenheit_temp} degrees, feels like {fahrenheit_feels_like}."
        return weather_info
    else:
        return "City not Found"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather_route():
    city = request.form['city']
    state = request.form['state']
    weather_info = get_weather(city, state)
    return jsonify({'weather_info': weather_info})

if __name__ == "__main__":
    app.run(debug=True)
