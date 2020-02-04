# Import libraries
import pickle
import numpy as np
from flask import Flask, jsonify, request
import random
import pandas as pd

app = Flask(__name__)

# curl -X POST -H'content-type:application/json' --data'{"id": 4325 }' http://127.0.0.1:5000/api

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Load a random data point from prediction dataset
pred_df = pd.read_csv('prediction_data.csv')

def get_random_():
    id_ = random.sample(set(pred_df.index),1)[0]
    data_ = pred_df.loc[id_]

    return(data_.to_dict())

@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
        #if no id is given generate random id
    if data['id']:
        data_ = pred_df.loc[data['id']]
        data_ = data_.to_dict()

    else:
        data_ = get_random_()

    #pop the name key from the dictionary in order to run the model
    name = data_.pop('name')
    data_.pop('Unnamed: 0')

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([np.array(list(data_.values()))])

    # Take the first value of prediction
    output = prediction[0]
    if output == 1:
        output = {'prediction made:': name + ' has blue eyes.'}
    else:
        output = {'prediction made:': name +  ' does not have blue eyes.'}

    return jsonify(output)


if __name__ == '__main__':
    try:
        app.run(port=8080, debug=True, host='0.0.0.0')

    except KeyboardInterrupt:
        LOG.info("Exit requested")
        worker.close()
