# My goal is to gain a better understanding of the frontier models, so I'll use Gemini

import speech_recognition as sr
import datetime
import webbrowser
import os
import logging
import google.generativeai as gai
import pyaudio
import streamlit as st
from gtts import gTTS # this way is because of OOP, this is method

def greet():
    now = datetime.datetime.now()
    # greets the user
    hour = int(now.hour) # we convert the hour to an integer because it is a float
    if hour >= 0 and hour < 12:
        print("\033[1mGood Morning!\033[0m")
    elif hour >= 12 and hour < 18:
        print("\033[1mGood Afternoon!\033[0m")
    else:
        print("\033[1mGood Evening!\033[0m")
    print("I am your assistant. How may I help you?")
    # logging.info("Greeted the user")

# Application logger
# LOG_DIR = 'logs'
# LOG_FILE_NAME = 'app.log'

# os.makedirs(LOG_DIR, exist_ok=True)
# # mkdir is used to create a directory
# # os.makedirs is used to create a directory and all parent directories
# # exist_ok is used to prevent an error if the directory already exists

# log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
# # join the path of the directory and the file name

# logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(message)s')
# # basic configuration for the logger 
# # level is the info, and format is the time and the message

def take_command():
    # reckons the command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # use the microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
        #convert the audio to text
    except Exception as e:
        # logging.info(e) # log the error
        print("Say that again please...")
        return "None"
    return query # return the query as a string


def text_to_speech(text):
    # converts text to speech
    speech = gTTS(text=text, lang='en')
    speech.save("test_speech.mp3")
    os.system("start speech.mp3")
    # logging.info("Converted text to speech")
    #google tts

# greet()
# text_to_speech(take_command())

def gemini_model(input):
    gai.configure(api_key='AIzaSyCGPVB7IAbNjmr68IpdoBdkrumzulbHaZA')
    # replace the above with your own key
    model = gai.GenerativeModel('gemini-1.5-flash')
    # cheap model
    response = model.generate_content(input)
    # use input to generate content
    results = response.text
    return results

greet()
text = take_command()
response = gemini_model(text)
print(response)