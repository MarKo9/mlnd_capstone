
# pseudo code for multy input, multy output LSTM

# built based on the sample from https://keras.io/getting-started/functional-api-guide/
# the sample is for text prediction and not numerical so some changes have been made
# where thought to be necessary
#as the documentation for keras is not the most detailed/explenatory out there would like some insights


## main input (sales_per_day, customer_per_day)

### Getting the inputs and the ouputs (lets say using ones day data to predict the next on a dataset with 1258 days total)
X_main_train = training_set[0:1257]
X_other_train = training_set[0:1257]
# the sales data only
y_train = training_set[1:1258]


### Adding the LSTM layer
##input_shape: must be apair of 2 elements 
##### None: means that model can expect any time step, 2: beacause 2 feature2
## the settings are what was using on the Sequential API but this sample is based on
## the Functional API so not sure if arguments are correct 
lstm_out = LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 2))
#Here we insert the auxiliary loss, allowing the LSTM and Embedding layer to be 
#trained smoothly even though the main loss will be much higher in the model.
auxiliary_output = Dense(1, activation='sigmoid', name='aux_output')(lstm_out)


# other input (day_or_week, holiday)
## not sure if this is correct but since I am having lets 9 features 
## (7 days per week + 2 (holiday boolean)),I using the above
auxiliary_input = Input(shape=(9,), name='aux_input')

## concatenate the 2 inputs
x = keras.layers.concatenate([lstm_out, auxiliary_input])



## We stack a deep densely-connected network on top
x = Dense(64, activation='relu')(x)
x = Dense(64, activation='relu')(x)
x = Dense(64, activation='relu')(x)

model = Model(inputs=[main_input, auxiliary_input], outputs=[main_output, auxiliary_output])

## change in the loss function from "binary_crossentropy" to "mean_squared_error" 
## not sure what is going on with the loss_weights settings and if this approach stands
# correct in my case
model.compile(optimizer='rmsprop',
              loss={'main_output': 'mean_squared_error', 'aux_output': 'mean_squared_error'},
              loss_weights={'main_output': 1., 'aux_output': 0.2})

# And trained it via:
## X_main_train, X_other_train are the 2d inputs from above
## y_train is the sales data
model.fit({'main_input': X_main_train, 'aux_input': X_other_train},
          {'main_output': y_train, 'aux_output': y_train},
          epochs=50, batch_size=32)



