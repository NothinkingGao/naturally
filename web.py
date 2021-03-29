#!/usr/bin/env python
# coding: utf-8 
# Gao Ming Ming Create At 2021-03-25 16:11:19
# Description:some description


from flask import Flask, request, redirect, abort, url_for, session, jsonify, g, render_template
import json

app=Flask(__name__)

cache = list()

@app.route('/')
def index():
    return json.dumps(cache)

@app.route('/template')
def template():
    return render_template('template.html', **locals())

@app.route('/add')
def add():
    cache.append(request.args)
    return "success"
    

if __name__=='__main__':
    app.run(threaded=True,debug=True)
