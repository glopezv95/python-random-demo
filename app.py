import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from tabs import home_tab, biometrics_tab, socioec_tab
from callbacks import register_callbacks
from constants import ccaa

app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1(children = 'Random Demographic Analysis'),
    dcc.Dropdown(id = 'dd_ccaa',
                 options = ccaa,
                 className = 'custom-dd',
                 placeholder = 'Select CCAA'),
    dbc.Tabs(
        [dbc.Tab(home_tab, label = 'Home'),
         dbc.Tab(biometrics_tab, label = 'Biometrics'),
         dbc.Tab(socioec_tab, label = 'Socioeconomics')]
        )])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug = True)