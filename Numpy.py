import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential

# Define a dataset of simple mathematical expressions
expressions = ['2 + 2', '3 * 4', '10 - 5', '6 / 2']

# Create a vocabulary of characters
chars = set('0123456789 +-*/')
char_to_index = {char: index for index, char in enumerate(chars)}
index_to_char = {index: char for index, char in enumerate(chars)}

# Encode expressions into numerical sequences
max_len = max([len(expr) for expr in expressions])
X = np.zeros((len(expressions), max_len, len(chars)), dtype=np.bool)
y = np.zeros((len(expressions), max_len, len(chars)), dtype=np.bool)
for i, expr in enumerate(expressions):
    for t, char in enumerate(expr):
        X[i, t, char_to_index[char]] = 1
        if t < len(expr) - 1:
            y[i, t + 1, char_to_index[expr[t + 1]]] = 1

# Build a simple sequence-to-sequence model
model = Sequential()
model.add(LSTM(128, input_shape=(max_len, len(chars)), return_sequences=True))
model.add(Dense(len(chars), activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(X, y, batch_size=2, epochs=5000, verbose=2)

# Generate code using the trained model
start_expr = '2 +'
generated_expr = start_expr
for _ in range(10):  # Generate 10 characters
    x_pred = np.zeros((1, len(generated_expr), len(chars)))
    for t, char in enumerate(generated_expr):
        x_pred[0, t, char_to_index[char]] = 1
    preds = model.predict(x_pred, verbose=0)[0]
    next_char_index = np.argmax(preds[len(generated_expr) - 1])
    next_char = index_to_char[next_char_index]
    generated_expr += next_char

print("Generated Expression:", generated_expr)
