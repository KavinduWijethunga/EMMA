
from gtts import gTTS
import os
from playsound import playsound


########## pip install playsound==1.2.2 #######
# letast verstion not work #######

mytext = 'Welcome to geeksforgeeks!'


language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")
playsound('welcome.mp3')





