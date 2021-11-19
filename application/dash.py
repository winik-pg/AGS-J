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
                style={'size': 9, 'offset': 0, "text-align": "center",}),], justify="start",),
    html.Br(),
    
    dbc.Row([
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),
        dbc.Col(dbc.CardImg(src="link raw img")),]),
    
    
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