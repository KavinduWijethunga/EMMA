import speech_recognition
import pyttsx3
from gtts import gTTS
import os
from playsound import playsound
import threading
import time
from chat_api_level import chat_me




def audio_to_text():

    recognizer = speech_recognition.Recognizer()
    while True:
        try:

            #print('warking.............')

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                global user_say

                try:
                    text = recognizer.recognize_google(audio)
                    text = text.lower()
                    print(f"Recognized {text}")
                    user_say = str(text)
                except:
                    pass
                    print('i cant hear you properly tell again plz  ')
                    user_say = str('i cant hear you properly tell again plz  ')

                text_to_audio(user_say)

        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            continue



def audio_recognzr():
    pass




def text_to_audio(user_say):

    ########## pip install playsound==1.2.2 ####### but now work
    # letast verstion not work #######

    #mytext = 'Welcome to geeksforgeeks!'

    bot_say = chat_me(user_say)

    mytext = bot_say

    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    #time.sleep(0.1)
    playsound('welcome.mp3')
    #time.sleep(0.1)
    os.remove('welcome.mp3')



print('system_start ....')

audio_to_text()



