from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

seq = Sequential()
seq.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
seq.add(Dropout(0.2))

seq.add(LSTM(units = 50, return_sequences = True))
seq.add(Dropout(0.2))

seq.add(LSTM(units = 50, return_sequences = True))
seq.add(Dropout(0.2))

seq.add(LSTM(units = 50))
seq.add(Dropout(0.2))

seq.add(Dense(units = 1))

seq.compile(optimizer = 'adam', loss = 'mean_squared_error')

seq.fit(X_train, y_train, epochs = 100, batch_size = 32)
