
import speech_recognition




recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
    audio = recognizer.listen(mic)
    print('ss')
    with open('speechhhhhhhhhhhhhhhhhhhhhh.wav', 'wb') as f:
        f.write(audio.get_wav_data())










