
import numpy as np
import os
import librosa
import librosa.display

import warnings
import keras

warnings.filterwarnings('ignore')




def extract_mfcc(filename):
    y, sr = librosa.load(filename, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc



#print(test_file.shape)
model = keras.models.load_model('audio_chat_emo_model.h5')
name_lab = ['angry','disgust','fear','happy','neutral','ps', 'sad', 'angry']


# file_parth = 'test_data/'
# test_data = os.listdir(file_parth)

def audio_imo_DDN(file_parth,detels = False):


    test_file = extract_mfcc(file_parth)

    data = test_file.reshape(1, 40, 1)
    predictions = model.predict(data)
    accu = np.max(predictions)
    # print('accuresy - ', round(accu * 100, 2), ' %')
    # print('predict behavior - ',name_lab[np.argmax(predictions)])

    if detels:
        print('predict behavior - ',name_lab[np.argmax(predictions)], '   accuressy - ',accu)

    return name_lab[np.argmax(predictions)]



#print(audio_imo_DDN('human_voice.wav',detels = False))