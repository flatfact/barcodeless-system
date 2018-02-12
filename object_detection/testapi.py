#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:37:33 2018

@author: porames
"""

from flask import Flask,request
app = Flask(__name__)
 
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print(content["hey"])
    return "test"
 
app.run(host='0.0.0.0', port= 8090)