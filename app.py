#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
######
import json
import time
from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Hello World!"



def evaluate_credit(loanamount,age,income):
    score = (50 * income)/(loanamount*age)
    if age<18:
        result = 'not_approve'
    elif score < 0.5:
        result = 'not_approve'
    else:
        result = 'approve'
    return result


class credit_analysis(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('loanamount', type=int)
        parser.add_argument('age', type=int)
        parser.add_argument('income', type=int)
        dictp = parser.parse_args()
        kw = dictp['loanamount']
        ag = dictp['age']
        ic = dictp['income']
        res = evaluate_credit(kw,ag,ic)
        res = {"result":res}
        return res


api.add_resource(credit_analysis, '/credit_analysis',endpoint='credit_analysis')
if __name__ == '__main__':
    app.run(threaded=True)
