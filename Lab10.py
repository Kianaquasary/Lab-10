# Косарпур Киана - 344494 -  Вариант 4

import speech_recognition as sr
import pyttsx3
import requests
import random

r = sr.Recognizer()
engine = pyttsx3.init()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        command = r.recognize_google(audio)

        # recognizing commands
        if "dollar" in command:
            response = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub.json")
            rate = response.json()["USD"]
            engine.say(f"1 Russian Ruble is equal to {rate} US dollars")
        elif "euro" in command:
            response = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub.json")
            rate = response.json()["EUR"]
            engine.say(f"1 Russian Ruble is equal to {rate} euros")
        elif "save" in command:
            with open("rates.txt", "a") as f:
                response = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub.json")
                f.write(str(response.json()) + "\n")
            engine.say("Exchange rates saved to file")
        elif "amount" in command:
            response = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub.json")
            rate = response.json()["RUB"]
            engine.say(f"1 Russian Ruble is equal to {rate} Russian Rubles")
        elif "random" in command:
            response = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub.json")
            currencies = list(response.json().keys())
            random_currency = random.choice(currencies)
            rate = response.json()[random_currency]
            engine.say(f"1 Russian Ruble is equal to {rate} {random_currency}")
        else:
            engine.say("Command not recognized")

        engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("Sorry, I didn't catch that. Please try again.")
        engine.runAndWait()

    except requests.exceptions.RequestException:
        engine.say("Sorry, there was an error in the request. Please try again.")
        engine.runAndWait()
