import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os

####################################
# A P P
####################################
mytitle=' '
tabtitle='Aguascalientes'
sourceurl='https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published'

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
    html.Div([
        html.H5([dbc.Badge("inicio", 
                          href="link buttons",
                          color="light",
                          className="ml-1")]),],style={'textAlign': 'center',},),
    html.Br(),
    dbc.Row([
        dbc.Col(html.H6("Aguascalientes"),
                style={'size': 15, 'offset': 0, "text-align": "center",}),], justify="start",),
    html.Br(),
    
    dbc.Row([
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%201_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%202_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%203_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%204_r.png?raw=true")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%205_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%206_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%207_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%208_R.png?raw=true")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%209._rpng?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2010_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2011_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2012_r.png?raw=true")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2013_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2014_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2015_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2016_r.png?raw=true")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2017_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2018_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2019_r.png?raw=true")),
        dbc.Col(dbc.CardImg(src="https://github.com/winik-pg/AGS-J/blob/main/application/static/Aguascalientes_SEMANA%2020_r.png?raw=true")),]),
    
    
    html.Div([
        html.H5([dbc.Badge("inicio", 
                          href="link buttons",
                          color="light",
                          className="ml-1")]),],style={'textAlign': 'center',},),
    
    ],style={'width': '1800px', })

app.layout = html.Div([body],
                              style={'width': '1900px',
                                    "background-color": "white"})

#from application.dash import app
#from settings import config

if __name__ == "__main__":
    app.run_server()
