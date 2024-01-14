from dash import dcc, html
import dash_bootstrap_components as dbc

# General data tab
home_tab = dbc.Container([
    dbc.Row([
        dbc.Col(children = [
            dbc.Col([
                html.P('Length of data'),
                html.P(id = 'p_len', style = {'font-size':'50px'})],
                    width = 3,
                    style = {'text-align':'center',
                             'align-items':'center'}),
            dbc.Col([
                html.Ul(children = [
                    html.Li(id = 'li_gender_count',
                            style = {'margin-bottom':'5%'}),
                    html.Li(id = 'li_mean_height'),
                    html.Li(id = 'li_mean_weight'),
                    html.Li('Educational level:',
                            style = {'margin-top':'5%'}),
                    html.Ul([
                        html.Li(id = 'li_primary_count'),
                        html.Li(id = 'li_secondary_count'),
                        html.Li(id = 'li_tertiary_count')],
                            style = {'margin-top':'0px',
                                     'border-left':'2px solid rgb(22, 48, 32)',
                                     'margin-bottom':'5%'}),
                    html.Li(id = 'li_mean_income'),
                    html.Li(id = 'li_mean_age')])],
                    width = 3,
                    style = {'padding':'none'})], 
                width = 6,
                style = {'border-right':'2px solid rgb(22, 48, 32)'}),
        dbc.Col(className = 'col_home_buttons', children = [
            dcc.Download(id = 'download'),
            dbc.Row(children = [
                dcc.Input(id = 'input_length', placeholder = 'Select length of data')],
                    justify = 'center', style = {'color': 'red',
                                                 'margin-top': '2%',
                                                 'align-items': 'center',
                                                 'justify-content': 'center'}),
            dbc.Row(children = [
                html.Button('Regenerate data', id = 'button_regenerate',
                            className = 'button_home')],
                    justify = 'center'),
            dbc.Row(
                html.Button('Download data', id = 'button_download',
                            className = 'button_home'),
                justify = 'center')], width = 6,
                style = {'display':'inline-block',
                         'align-contents':'center'})])])

# Biometrics tab. Includes weight/height scatter plot, gender bar plot,
# and a gender/age histogram
biometrics_tab = dbc.Container([
    dbc.Row([
            dbc.Col(dcc.Graph(id = 'bio_bar'), width = 6),
            dbc.Col(dcc.Graph(id = 'bio_scatter'), width = 6)]),
    dbc.Row(dcc.Graph(id = 'age_gender_hist'))])

#Socioeconomic tab. Includes x dropdown, an income histogram and a bar chart
# that display mean income by ccaa and gender
socioec_tab = dbc.Container([
    dbc.Row(align = 'center', children = [
        html.Button('Gender', id = 'button_gender', className = 'gender_button',
                    style = {'width':'80px'}),
        html.Button('Studies', id = 'button_studies', style = {'width':'80px'})]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'se_income_hist'), width = 6),
        dbc.Col(
            dcc.Graph(id = 'income_studies_bar'), width = 6)])])
