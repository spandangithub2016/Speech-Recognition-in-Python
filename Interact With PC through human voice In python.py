#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import webbrowser
import os

flag = True

while flag:

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    direction = r.recognize_google(audio)
    print(direction)

    if str(direction) == "open my Facebook":

        new = 2 # open in a new tab, if possible
        # open facebook
        url = "https://www.facebook.com/spandanmajumderjblss?lst=100003142359755%3A100003142359755%3A1500301138"
        webbrowser.open(url,new=new)
    if str(direction) == "hi Max":
        
        print("Hi Bro")
    elif str(direction) == "play me a song":
        print("Starting Song")
        os.startfile('C:\Users\Spandan Majumder\Desktop\Amijeketomar.mp3')
    elif str(direction) == "open Notepad":
        print("Starting notepad")
        os.startfile('notepad.exe')
    elif str(direction) == "close the Notepad":
        print("closing notepad")
        os.system("taskkill /f /im notepad.exe")
        Flag = False
    elif str(direction) == "bye Max":
        Flag = False
    else:
        print("Please say again....")


# Linux
# chrome_path = '/usr/bin/google-chrome %s'
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'








### recognize speech using Google Speech Recognition
##try:
##    # for testing purposes, we're just using the default API key
##    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
##    # instead of `r.recognize_google(audio)`
##    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
##except sr.UnknownValueError:
##    print("Google Speech Recognition could not understand audio")
##except sr.RequestError as e:
##    print("Could not request results from Google Speech Recognition service; {0}".format(e))
