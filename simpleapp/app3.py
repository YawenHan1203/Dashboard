# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                go.Scatter(
                    x=np.arange(-10,10,1),
                    y=np.square(np.arange(-10,10,1)),
                    mode='markers',
                    marker={'size': 15, 'color':'red'}
                ) 
            ],
            'layout': go.Layout(
                title= 'y=x^2',
                xaxis={'title': 'x'},
                yaxis={'title': 'y'},
                
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)