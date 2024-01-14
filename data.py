import pandas as pd
import numpy as np

from constants import ccaa

#Define a dataframe generation function from a random seed
def generate_random_seed(s, l):
    
    # Define a random normal distribution generation function
    def generate_filtered_random_dist(mean: float, std: float, column: str, condition:str):
        dist = np.random.normal(
            loc = mean,
            scale = std,
            size = len(df[df[column] == condition]))
    
        return dist
    
    # Set a random seed
    seed = s
    np.random.seed(seed)

    # Generate an empty DataFrame and set its size
    df = pd.DataFrame()
    df_size = l

    # Add a gender column
    p_male = np.random.randint(47, 52)/100
    p_female = 1 - p_male

    df['gender'] = np.random.choice(
        a = ['male', 'female'],
        size = df_size,
        p = [p_male, p_female])

    # Add height and weight columns
    for item in df['gender'].unique():
        if item == 'male':
            height_mean = np.random.randint(174, 178)
            weight_mean = np.random.randint(73, 77)
        else:
            height_mean = np.random.randint(164, 168)
            weight_mean = np.random.randint(53, 57)
            
        df.loc[df['gender'] == item, 'height'] = generate_filtered_random_dist(
            mean = height_mean,
            std = 4,
            column = 'gender',
            condition = item)
        
        df.loc[df['gender'] == item, 'weight'] = generate_filtered_random_dist(
            mean = weight_mean,
            std = 5,
            column = 'gender',
            condition = item)

    # Add studies column
    p_primary = np.random.randint(50, 60)/100
    p_secondary = np.random.randint(25, 35)/100
    p_tertiary = 1 - p_primary - p_secondary

    df['studies'] = np.random.choice(
        a = ['primary', 'secondary', 'tertiary'],
        size = len(df),
        p = [p_primary, p_secondary, p_tertiary])

    # Generate a dictionary with studies-income mean and std pairs
    income_studies_pairs = {
        'primary':[np.random.randint(17,22)*1000, 6000],
        'secondary':[np.random.randint(23,28)*1000, 7500],
        'tertiary':[np.random.randint(47,52)*1000, 10000]}

    # Add income column
    for item in income_studies_pairs.keys():
        df.loc[df['studies'] == item, 'income'] = np.random.normal(
            loc = income_studies_pairs[item][0],
            scale = income_studies_pairs[item][1],
            size = len(df[df['studies'] == item]))
        
    df.loc[df['income'] < 500, 'income'] = np.median(df['income'])

    df['income'] = df['income'].round(2)

    # Add income categorical
    for item in df['income']:
        if item > 60000:
            df.loc[df['income'] == item, 'income_cat'] = '> 60 000'
        elif 40000 < item < 60000:
            df.loc[df['income'] == item, 'income_cat'] = '40 000 - 60 000'
        else:
            df.loc[df['income'] == item, 'income_cat'] = '< 40 000'

    # Add CCAA column
    df['ccaa'] = np.random.choice(
        a = ccaa,
        size = len(df))

    # Add an ordinal income/studies column
    df['inc_rank'] = df.sort_values(by = ['studies', 'income'], ascending = False)\
        .groupby('studies').cumcount() + 1

    # Add age column
    df.loc[df['income'] > np.quantile(df['income'], .80), 'age'] = \
        np.random.normal(
            loc = 50,
            scale = 6,
            size = len(df[df['income'] > np.quantile(df['income'], .80)]))
        
    df.loc[df['age'].isnull(), 'age'] = np.random.normal(
            loc = 40,
            scale = 6,
            size = len(df[df['age'].isnull()]))

    df['age'] = df['age'].astype(int)
    
    return df