# mlnd_capstone

Trying to implement an LSTM for sales prediction as part of my capstone project.
I am not going to use the sales data only but also other features such as day of week, holiday or not etc.
Seeing on the keras documentation here tried to create a pseudocode on how the actual structure will look like as the documentation for keras is not the most detailed/explanatory out there would like some insightson my understanding.

code is created based in https://keras.io/getting-started/functional-api-guide/

The sample is for text prediction and not numerical so some changes have been made where thought to be necessary.

## I am mostly concerned about:

The overall structure
The arguments in: lstm_out = LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 2)) and
The arguments in: auxiliary_input = Input(shape=(9,), name='aux_input'))
The way I am compiling and fitting the model

the whole pseudocode is in pseudocode.py


Would really appreciate some feedback promptly.
