# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:59:43 2019

@author: Manish
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:15:51 2019

@author: Manish
"""
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from flask import request
from datetime import datetime
from flask_cors import CORS, cross_origin 
import sys
import os
import datetime
import calendar
import pickle
from flask import render_template, make_response
import datetime
import time
from dateutil import relativedelta
from flask import Flask, session, jsonify, request
import os
import traceback
import json
import requests

import requests

# Your API definition
app = Flask(__name__)
#for localhost
cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})

@app.route('/chat', methods=['POST','GET'])
@cross_origin(origin='localhost')

def chat():
    try:
        url = "http://localhost:5005/webhooks/rest/webhook/"
        headers = {'content-type': 'application/json'}
    
        #payload = "{ \"message\": \" i want to do engineering\"}"
        json_input = request.json
        inp_msg  = json_input["message"]
        print("1",inp_msg)
    
        in_json = {"message" : inp_msg}
        #return_list_of_dicts.append(out_dict)
            #out_json = json.dumps(out_dict,ensure_ascii= False)
        in_json = json.dumps(in_json,ensure_ascii= False)
        #print("2", in_json)
        response = requests.request("POST", url, data=in_json, headers=headers)
        #print(response)
        #print("3",response.status_code)
        #print("4",response.text)
        print("5",response.json())     
        
    
        return jsonify(response.json())





    except:
        return jsonify({'trace': traceback.format_exc()})

 


if __name__ == '__main__':
    app.run()
