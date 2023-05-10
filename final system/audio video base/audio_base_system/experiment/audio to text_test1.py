import speech_recognition
import pyttsx3
from gtts import gTTS
import os
from playsound import playsound
import threading
import time





def audio_to_text(para):

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


def text_to_audio(para):





    ########## pip install playsound==1.2.2 ####### but now work
    # letast verstion not work #######

    #mytext = 'Welcome to geeksforgeeks!'

    mytext = para

    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    #time.sleep(0.1)
    playsound('welcome.mp3')
    #time.sleep(0.1)
    os.remove('welcome.mp3')






t1 = threading.Thread(target=audio_to_text, args=(10,))
#t2 = threading.Thread(target=text_to_audio, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
#t2.start()
