# My goal is to gain a better understanding of the frontier models, so I'll use Gemini

import speech_recognition as sr
import datetime
import os
import logging
import google.generativeai as gai
import streamlit as st
from gtts import gTTS

def greet():
    now = datetime.datetime.now()
    # greets the user
    hour = now.hour
    minute = now.minute
    second = now.second
    period = "AM" if hour < 12 else "PM"# store the if else in a variable
    hour %= 12
    hour = 12 if hour == 0 else hour # if hour is 0, set it to 12

    if period == "AM" and hour <= 12:
        st.write(f"Good Morning! \n It is {hour}:{minute}:{second} {period}")
    elif period == "PM" and hour <= 6:
        st.write(f"Good Afternoon! \n It is {hour}:{minute}:{second} {period}")
    else:
        st.write(f"Good Evening! \n It is {hour}:{minute}:{second} {period}")

    st.write("I am your assistant. How may I help you?")
    logging.info("Greeted the user")
    logging.info("Greeted the user")

LOG_DIR = 'logs' #optional log directory
LOG_FILE_NAME = 'app.log'

os.makedirs(LOG_DIR, exist_ok=True)
# mkdir is used to create a directory
# os.makedirs is used to create a directory and all parent directories
# exist_ok is used to prevent an error if the directory already exists

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
# join the path of the directory and the file name

logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(message)s')
# basic configuration for the logger 
# level is the info, and format is the time and the message

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
        query = r.recognize_google(audio, language='en') # recognize_google is used to convert the audio to text
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
    gai.configure(api_key='')
    # replace the above with your own key
    model = gai.GenerativeModel('gemini-1.5-flash')
    # cheap model
    response = model.generate_content(input)
    # use input to generate content
    results = response.text
    return results

def main():
    st.title("AI Voice Assistant with Gemini")

    greet()

    if st.button("Speak"):
        with st.spinner("Listening..."):
            text = take_command()
            # get the text from the user
            response = gemini_model(text) # calls take command first since its inside
            # get the response from the model
            # display the response
            text_to_speech(response)
            # convert the response to speech in mp3

            audio_file = open("test_speech.mp3", "rb")
            audio_bytes = audio_file.read()

            st.text_area(label="AI Response", value=response, height=200)
            st.audio(audio_bytes, format="audio/mp3", start_time=0, autoplay=True)
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute
            second = now.second
            period = "AM" if hour < 12 else "PM"
            hour %= 12
            hour = 12 if hour == 0 else hour

            st.download_button(label="Download Audio", data=audio_bytes, file_name=f"{hour}:{minute}:{second} .mp3", mime="audio/mp3")
    #streamlit run main.py
    # alternative to gradio

main()

'''In Summary:

I created a voice assistant using the speech_recognition library to recognize the users voice input.
1. I used the Google Text-to-Speech (gTTS) library to convert text to speech.
2. I used the GenerativeAI library to generate responses to the user's queries.
3. I used the Streamlit library to create a web application for the voice assistant.
4. I used the logging library to log information about the voice assistant.
5. I used the datetime library to get the current time and date.'''
