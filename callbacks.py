import dash
from dash import callback_context as ctx
from dash.dependencies import Input, Output
import io
import base64

from data import generate_random_seed
from graphs import generate_bar, generate_scatter, generate_hist
from constants import seed, l

def register_callbacks(a):

    @a.callback(
        [Output('bio_scatter', 'figure'),
        Output('bio_bar', 'figure'),
        Output('age_gender_hist', 'figure'),
        Output('se_income_hist', 'figure'),
        Output('income_studies_bar', 'figure'),
        Output('li_gender_count', 'children'),
        Output('li_mean_height','children'),
        Output('li_mean_weight', 'children'),
        Output('li_primary_count', 'children'),
        Output('li_secondary_count', 'children'),
        Output('li_tertiary_count', 'children'),
        Output('li_mean_income', 'children'),
        Output('li_mean_age', 'children'),
        Output('p_len', 'children')],
        [Input('dd_ccaa', 'value'),
        Input('button_gender', 'n_clicks'),
        Input('button_studies', 'n_clicks'),
        Input('button_regenerate', 'n_clicks'),
        Input('input_length', 'value')])

    def upgrade_output(value, gender, studies, regenerate, lth):
        if lth:
            global l
            l = int(lth)
            
        if ctx.triggered_id == 'button_regenerate':
            global seed
            seed += 1
            
        if value is not None:
            dff = generate_random_seed(seed, l)
            dff = dff[dff['ccaa'] == value]
        
        else:
            dff = generate_random_seed(seed, l)
        
        if value:
            dff = dff[dff['ccaa'] == value]
                
        fig_2 = generate_bar(
            data = dff.groupby(['ccaa', 'gender'])['age'].agg('mean').reset_index(),
            x = 'ccaa',
            y = 'age',
            sub_x = 'gender')
        
        fig_5 = generate_bar(
            data = dff.groupby(['ccaa', 'gender'])['income'].agg('mean').reset_index(),
            x = 'ccaa',
            y = 'income',
            sub_x = 'gender')
            
        fig_1 = generate_scatter(
            data = dff,
            x = 'height',
            y = 'weight',
            sub_x = 'gender')
        
        fig_3 = generate_hist(
            data = dff,
            x = 'age',
            sub_x = 'gender')
        
        fig_4 = generate_hist(
                data = dff,
                x = 'income',
                sub_x = 'gender')
        
        female = len(dff[dff['gender'] == 'female'])
        male = len(dff[dff['gender'] == 'male'])
        height = dff['height'].mean()
        weight = dff['weight'].mean()
        primary = len(dff[dff['studies'] == 'primary'])
        secondary = len(dff[dff['studies'] == 'secondary'])
        tertiary = len(dff[dff['studies'] == 'tertiary'])
        income = weight = dff['income'].mean()
        age = weight = dff['age'].mean()
        length = len(dff)
        
        if ctx.triggered_id == 'button_gender':
            fig_4 = generate_hist(
                data = dff,
                x = 'income',
                sub_x = 'gender')
            
        if ctx.triggered_id == 'button_studies':
            fig_4 = generate_hist(
                data = dff,
                x = 'income',
                sub_x = 'studies')
        
        return fig_1, fig_2, fig_3, fig_4, fig_5,\
            f'{female} females, {male} males', f'Mean height: {round(height, 2)} cm',\
            f'Mean weight: {round(weight, 2)} kg', f'Primary studies: {primary}',\
            f'Secondary studies: {secondary}',f'Tertiary studies: {tertiary}',\
            f'Mean income: {round(income, 2)} €', f'Mean age: {round(age, 2)} years',\
            length

    @a.callback(
        Output('download', 'data'),
        [Input('button_download', 'n_clicks'),
         Input('dd_ccaa', 'value')])
    
    def download_data(click, value):
        if ctx.triggered_id == 'button_download':
            dff = generate_random_seed(seed, l)
            csv_string = dff.to_csv(index=False, encoding='utf-8')
            
            return dict(content = csv_string, filename = 'data.csv')
        
        else:
            return dash.no_update