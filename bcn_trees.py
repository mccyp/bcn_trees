# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


from flask import Flask, render_template, request, url_for, flash, redirect
import pandas as pd
import folium


app = Flask(__name__)



@app.route('/')
def render_index():
    return render_template('index.html')



@app.route('/mapa', methods=(['POST']))
def render_the_map():
    content = request.form['text']
    content = content.lower()
    if not content:
        flash('''Has d'entrar un titol!''')
    else:
        trees = pd.read_csv('arbres_bcn.csv')
        trees2 = trees.loc[trees['nom_cientific'].str.contains(content)]
        bcn = folium.Map(location = [41.390205, 2.154007], zoom_start = 13)
        for index, row in trees2.iterrows():
            folium.Marker(
                location=[row['latitud'], row['longitud']],
                popup = row['nom_cientific'] + '\n' + 'Planted on: ' + str(row['data_plantacio']),
                icon=folium.Icon(color="green", icon='fa-tree', prefix='fa')).add_to(bcn)
        return bcn._repr_html_()