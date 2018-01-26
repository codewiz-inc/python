import speech_recognition as sr
from time import ctime
import time
import webbrowser as wb
import os
import psutil
import pyaudio
from gtts import gTTS

chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print('done!')

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def assistant(data):
    if "hi" in data:
        speak("Hello! pleasure to speak to you")

    if "national bird" in data:
        bird="Peacock"
        print(bird)
        speak(bird)

    if "national tree" in data:
        tree="banyan"
        print(tree)
        speak(tree)

    if "national Fruit" in data:
        fru="Mango"
        print(fru)
        speak(fru)

    if "motto" in data:
        m="satyameva Jeyate "
        print(m)
        speak(m)

    if "national animal" in data:
        ani = "tiger"
        print(ani)
        speak(ani)

    if "national flower" in data:
        flo = "Lotus"
        print(flo)
        speak(flo)

    if "number of states" in data:
        a= "29"
        print(a)
        speak(a)


    if "capital city" in data:
        p="Delhi"
        print(p)
        speak(p)

    if  "colours in national flag" in data :
        colors = "three colours! they are saffron,white and green with blue chakra inside it"
        print(colors)
        speak(colors)


    if "play national anthem" in data:
        print("playing")
        wb.get(chrome_path).open("https://youtu.be/r3TtgYuaVFk")


    if "search me about" in data:
        data = data.split(" ")
        search = data[3:]
        print(search)
        searchstr = '+'.join(search)
        print(searchstr)
        speak("searching,please wait"+searchstr)
        wb.get(chrome_path).open("https://www.google.co.in/search?q="+ searchstr)




time.sleep(1)
speak("Hi Hari, what's up?")
while 1:
    data = recordAudio()
    assistant(data)
