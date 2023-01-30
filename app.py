from dash import Dash, html, dcc
import datetime
from dash.dependencies import Input, Output

app = Dash(__name__)

from dash import html

@app.callback(Output('my_output', 'children'),
              Input('interval_component', 'n_intervals'))

def update_output_div(input_value):
    return f'Updated time snapshot is: {getStrTime()}'


def serve_layout():
    return html.Div([

        html.Div([
            html.H4('CURRENT TIME (LIVE UPDATES)'),
            ]),

        html.Div(id='my_output'),


        html.Div([
            dcc.Interval(id='interval_component', interval=1000 * 1, n_intervals=0)
        ])

    ])

def getStrTime():
    return str(datetime.datetime.now())

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)