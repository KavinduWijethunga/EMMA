from predict_audio_imotion import audio_imo_DDN
import os


file_parth = 'test_data/OAF_bite_disgust.wav'
# test_data = os.listdir(file_parth)





stat = audio_imo_DDN(file_parth,detels = False)

print(stat)





