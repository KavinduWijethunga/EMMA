

import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from matplotlib import pyplot as plt

#Load dataset
with open('intents.json') as file:
    data = json.load(file)



#split labels and sentences
training_sentences = []
training_labels = []
labels = []
responses = []

#added training patterns
for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])




#added lable encoder
num_classes = len(labels)
lbl_encoder = LabelEncoder()
lbl_encoder.fit(training_labels)
training_labels = lbl_encoder.transform(training_labels)

##added max length
vocab_size = 1000
embedding_dim = 16
max_len = 20
oov_token = "<OOV>"

# adding out of vocabulary token
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)



########################## model #####################################
#model initializing
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(GlobalAveragePooling1D())

decoder_lstm = tf.keras.layers.LSTM( 10 , return_state=True , return_sequences=True )
decoder_lstm = tf.keras.layers.LSTM( 5 , return_state=True , return_sequences=True )

#added dense layers
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

print('num_classes - ',num_classes)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

#initialize no of epoches
epochs = 300
history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)


acc = history.history['accuracy']
epochs = list(range(epochs))
plt.plot(epochs, acc, label='train accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()



loss = history.history['loss']

plt.plot(epochs, loss, label='train loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()





# saving model
model.save("chat_model")

import pickle

# saving tokenizer
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# saving label encoder
with open('label_encoder.pickle', 'wb') as ecn_file:
    pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)



print('model traind complited.')












