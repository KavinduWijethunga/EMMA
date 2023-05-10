import pandas as pd
import numpy as np
import os
#import seaborn as sns
import matplotlib.pyplot as plt
import librosa
import librosa.display
#from IPython.display import Audio
import warnings
warnings.filterwarnings('ignore')


paths = []
labels = []
for dirname, _, filenames in os.walk('dataset'):
    for filename in filenames:
        paths.append(os.path.join(dirname, filename))
        label = filename.split('_')[-1]
        label = label.split('.')[0]
        labels.append(label.lower())
    if len(paths) == 25596:
        break
print('Dataset is Loaded')

print(len(paths))

print(labels[:5])

## Create a dataframe
df = pd.DataFrame()
df['speech'] = paths
df['label'] = labels
df.head()

df['label'].value_counts()

#sns.countplot(df['label'])


def waveplot(data, sr, emotion):
    plt.figure(figsize=(10, 4))
    plt.title(emotion, size=20)
    librosa.display.waveplot(data, sr=sr)
    plt.show()


def spectogram(data, sr, emotion):
    x = librosa.stft(data)
    xdb = librosa.amplitude_to_db(abs(x))
    plt.figure(figsize=(11, 4))
    plt.title(emotion, size=20)
    librosa.display.specshow(xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()


# emotion = 'fear'
# path = np.array(df['speech'][df['label']==emotion])[0]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
# emotion = 'angry'
# path = np.array(df['speech'][df['label']==emotion])[1]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
#
# emotion = 'disgust'
# path = np.array(df['speech'][df['label']==emotion])[0]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
# emotion = 'neutral'
# path = np.array(df['speech'][df['label']==emotion])[0]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
# emotion = 'sad'
# path = np.array(df['speech'][df['label']==emotion])[0]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
# emotion = 'ps'
# path = np.array(df['speech'][df['label']==emotion])[0]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
#
# emotion = 'happy'
# path = np.array(df['speech'][df['label']==emotion])[0]
# data, sampling_rate = librosa.load(path)
# waveplot(data, sampling_rate, emotion)
# spectogram(data, sampling_rate, emotion)
# Audio(path)
#
#
#
#
def extract_mfcc(filename):
    y, sr = librosa.load(filename, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc
#
#
# extract_mfcc(df['speech'][0])
#

X_mfcc = df['speech'].apply(lambda x: extract_mfcc(x))
#
print(X_mfcc)


X = [x for x in X_mfcc]
X = np.array(X)
# X.shape
#
X = np.expand_dims(X, -1)
# X.shape
#
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
y = enc.fit_transform(df[['label']])
#
#
y = y.toarray()
#
# y.shape

#import keras LSTM neural network
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

model = Sequential([
    LSTM(123, return_sequences=False, input_shape=(40,1)),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(7, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Train the model

history = model.fit(X, y, validation_split=0.2, epochs=70, batch_size=125, shuffle=True)


epochs = list(range(70))
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.plot(epochs, acc, label='train accuracy')
plt.plot(epochs, val_acc, label='val accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()



loss = history.history['loss']
val_loss = history.history['val_loss']

plt.plot(epochs, loss, label='train loss')
plt.plot(epochs, val_loss, label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

#save the model
model.save("audio_chat_emo_model_new_dataset.h5")
















