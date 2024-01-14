import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

def generate_scatter(data: pd.DataFrame, x:str, y:str, sub_x:str):
    fig = px.scatter(
        data_frame = data,
        x = x,
        y = y,
        color = sub_x,
        color_discrete_sequence = px.colors.qualitative.Dark2)
    
    x_values = data[x]
    y_values = data[y]
    X = sm.add_constant(x_values)
    model = sm.OLS(y_values, X).fit()

    trendline = go.Scatter(
        x = x_values,
        y = model.predict(X),
        mode = 'lines',
        line = dict(color = 'rgba(22, 48, 32,.5)'),
        name = 'Trendline',
        showlegend = False)

    fig.add_trace(trendline)
    
    correlation_coefficient = round(data[x].corr(data[y]), 2)
    correlation_text = f'pearson (r) = {correlation_coefficient}'
    
    annotation = go.layout.Annotation(
        text=correlation_text,
        align='left',
        showarrow=False,
        xref='paper',
        yref='paper',
        x=0.05,
        y=0.9,
        font = dict(family='sans-serif', size=18, color='rgb(22, 48, 32)'))
    
    fig.add_annotation(annotation)
    
    fig.update_layout(
        title = f'{y.title()}/{x} by {sub_x}',
        font = dict(family = 'sans-serif', color = 'rgb(22, 48, 32)'),
        plot_bgcolor='rgb(238, 240, 229)',
        paper_bgcolor='rgb(238, 240, 229)',
        title_font = dict(size = 18),
        xaxis_title = None,
        yaxis_title = None,
        showlegend = False,
        margin=dict(pad=10))
    
    return fig

def generate_bar(data:pd.DataFrame, x:str, y:str, sub_x:str = None):
    fig = px.bar(
        data_frame = data,
        x = x,
        y = y,
        color = sub_x,
        barmode = 'group',
        color_discrete_sequence = px.colors.qualitative.Dark2,
        hover_data = sub_x)
    
    fig.update_layout(
        title = f'{y.title()} by {x} (mean)',
        font = dict(family = 'sans-serif', color = 'rgb(22, 48, 32)'),
        plot_bgcolor='rgb(238, 240, 229)',
        paper_bgcolor='rgb(238, 240, 229)',
        title_font = dict(size = 18),
        xaxis_title = None,
        yaxis_title = None,
        margin = dict(pad = 10),
        showlegend = False)
    
    return fig

def generate_hist(data:pd.DataFrame, x:str, sub_x:str):
    fig = px.histogram(
        data_frame = data,
        x = x,
        color = sub_x,
        color_discrete_sequence = px.colors.qualitative.Dark2,
        opacity = .5)
    
    fig.update_layout(
        title = f'{x.title()} distribution',
        font = dict(family = 'sans-serif', color = 'rgb(22, 48, 32)'),
        plot_bgcolor='rgb(238, 240, 229)',
        paper_bgcolor='rgb(238, 240, 229)',
        title_font = dict(size = 18),
        xaxis_title = None,
        yaxis_title = None,
        margin = dict(pad = 10),
        showlegend = False)
    
    return fig