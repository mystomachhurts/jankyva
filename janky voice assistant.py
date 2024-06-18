import pyttsx3
import speech_recognition as sr
import time
import os
import webbrowser
import pygame
from googlesearch import search

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for activation keyword
def listen_for_activation():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening for activation...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)  

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            if "YO" in query.upper():
                speak("Hey there! How can I help you?")
                return True  
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you try again?")
        except sr.RequestError:
            speak("I'm having trouble with my speech recognition. Please try again.")
    return False

# Function to listen for user commands
def listen_for_commands():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening for commands...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)  

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
        except sr.RequestError:
            speak("I'm having trouble with my speech recognition. Please try again.")

# Function to play a song
def play_song(song_path):
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to perform Google search and get the top search result
def google_search(query):
    try:
        search_results = list(search(query, num=1, stop=1))
        return search_results[0]
    except Exception as e:
        print("An error occurred during Google search:", e)
        return None

# Main function for virtual assistant
def virtual_assistant():
    print("Virtual Assistant activated...")
    while not listen_for_activation():
        pass
    
    while True:
        query = listen_for_commands()
        if "exit" in query:
            speak("Goodbye!")
            break
        elif "play that shi" in query:
            speak("Playing the requested song.")
            # Placeholder: Replace the path with the actual path to your song file
            play_song(r"C:\Users\lilha\Desktop\Creek (feat. Osamason).mp3")
        else:
            speak("Let me search that for you.")
            search_result = google_search(query)
            if search_result:
                speak("Here's what I found on Google:")
                speak(search_result)
            else:
                speak("Sorry, I couldn't find any relevant information.")

# Entry point of the script
if __name__ == "__main__":
    virtual_assistant()
