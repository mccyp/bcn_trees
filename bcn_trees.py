import pandas as pd 
import json
import pygsheets
import sys
import os
from flask import Flask, render_template, request, url_for, flash, redirect
import pandas as pd
import folium


app = Flask(__name__)

gc = pygsheets.authorize(client_secret='/home/k4y4k/credentials/code_secret.json')

@app.route('/')
def render_index():
    return render_template('index.html')



@app.route('/mapa', methods=(['POST']))
def render_the_map():
    content = request.form.get('content',type=int)
    if not content:
        flash('''Merci de saisir un nombre correspondant à un item !''')
    else:
        # Open the spreadsheet and the first sheet.
        sh = gc.open_by_key('1aCzOeWrq8BQFz-39dC07QQ8TOJeT5fNbNSCCh6jLLUY')
        wks = sh.sheet1
        df = pd.DataFrame(wks.get_all_values())
        print(df.iloc[0])
        cols = df.iloc[0]
        df.columns = cols
        del cols[0]
        df = df.drop(0)      
        def verdict(df, x):
            y = int(x)-1
            row = df.iloc[y]
            print('''
                    __,__
           .--.  .-"     "-.  .--.
          / .. \/  .-. .-.  \/ .. \\
         | |  '|  /   Y   \  |'  | |
         | \   \  \ 0 | 0 /  /   / |
          \ '- ,\.-"`` ``"-./, -' /
           `'-' /_   ^ ^   _\ '-'`
               |  \._   _./  |
               \   \ `~` /   /
                '._ '-=-' _.'
                   '~---~ ''')
            print('\n||||||||| ITEM N°' + row[0] + ' ||||||||| ')
            for col in cols:
                print(col)
                if( (len(str(col)) > 3) & (len(row[col]) > 2) ):   
                    print(col)
                    print('   -> ' + row[col])

        result = verdict(df, sys.argv[1])
        print(result)




