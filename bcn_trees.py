import pandas as pd 
import json
import pygsheets
import sys
import os
from flask import Flask, render_template, request, url_for, flash, redirect
import pandas as pd
import folium


app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')






