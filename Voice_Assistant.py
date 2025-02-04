import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time 

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Did not understand")

def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
   
    if "hey peter" in sptext().lower():
        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "My name is Peter"
                speechtxt(name)

            elif "old are you" in data1:
                age = "I am two years old"
                speechtxt(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I:%M %p")
                speechtxt(f"The time is {time}")

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                speechtxt(joke_1)

            elif "song" in data1:
                add = r"C:\Users\Admin\Desktop\song"
                listsongs = os.listdir(add)
                print(listsongs)
                os.startfile(os.path.join(add, listsongs[0]))

            elif "exit" in data1:
                speechtxt("Thank you")
                break

            time.sleep(10)


    else:
        print("thanks")
