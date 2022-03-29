# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:22:22 2022

@author: 703311085
"""

from flask import Flask, request, jsonify

import pandas as pd
import pickle
import logging
import os

with open('ml-model.pkl', 'rb') as f:
    MODEL = pickle.load(f)

FEATURES_MASK = ['age', 'balance', 'duration', 'campaign', 'job_blue-collar',
       'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
       'job_self-employed', 'job_services', 'job_student', 'job_technician',
       'job_unemployed', 'job_unknown', 'marital_married', 'marital_single',
       'education_secondary', 'education_tertiary', 'education_unknown',
       'contact_telephone', 'contact_unknown', 'poutcome_other',
       'poutcome_success']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server_check():
    return "I'M ALIVE!"

@app.route('/predict', methods=['POST'])
def predictor():
    content = request.json

    try:
        features = pd.DataFrame([content])
        features = features[FEATURES_MASK]
    except:
        logging.exception("The JSON file was broke.")
        return jsonify(status='error', predict=-1)

    pred = MODEL.predict(features)[0]

    return jsonify(status='ok', predict=pred)

if __name__=='__main__':
    app.run( debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)) )