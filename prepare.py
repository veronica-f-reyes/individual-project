#!/usr/bin/env python
# coding: utf-8

# #### Individual Class Project
# 
# ## Predicting Major League Baseball Game Outcomes
# ***
# ### Prepare Major League Baseball Data from baseball-reference.com
# 
# - All data is acquired from batting game logs for all 30 Major League Baseball teams for the year 2021
# - All batting logs were combined into one .csv file
# - Data source is baseball-reference.com
# 
# ## Prepare
# 
# ### Clean up and prepare data obtained to use for exploration and modeling
# 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Container
import os
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats


def prepare_data():

    import warnings
    warnings.filterwarnings('ignore')

    import pandas as pd
    import numpy as np

    import acquire

    filename = "baseball.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        
        #Acquire baseball batting data using function in acquire.py
        df = acquire.get_batting_log_data()
        
        # Create new column to capture that game was played away, not at home stadium
        df['is_away'] = np.where(df['Unnamed: 4']== '@', 1, 0)
        
        
        #Renaming columns for easier readability
        df = df.rename(columns={"PA": "plate_app", "AB": "at_bats", "R": "runs_scored",
                    "H": "hits", "2B": "doubles", "3B": "triples", "BB": "bases_on_balls", 
                    "IBB": "intentional_bb", "SO": "strikeouts","HBP": "hit_by_pitch", 
                    "SH": "sac_hits", "SF": "sac_flies","ROE": "reached_on_error", "GDP": "double_plays",
                    "SB": "stolen_bases","CS": "caught_stealing", "BA": "batting_avg", "LOB": "left_on_base",
                    "#": "num_players_used", "Thr": "handedness_opp_pitcher"}, errors="raise")
        
        #Feature Engineering: Create new column with result, is_win, where 1 is a win and 0 is a loss for every game
        df['is_win'] = np.where(df.Rslt.str.startswith('W'), 1, 0)
        
        #Feature Engineering: Create new columns to filter by teams that made the playoffs in 2021, a.k.a. - most winning teams
        df['made_playoffs'] = np.where((df['Team'].str.contains('Houston Astros'))|
                               (df['Team'].str.contains('Chicago White Sox'))|
                               (df['Team'].str.contains('Boston Red Sox'))|
                               (df['Team'].str.contains('Atlanta Braves'))|
                               (df['Team'].str.contains('Milwaukee Brewers'))|
                               (df['Team'].str.contains('L.A. Dodgers'))|
                               (df['Team'].str.contains('S.F. Giants'))|
                               (df['Team'].str.contains('N.Y. Yankees'))|
                               (df['Team'].str.contains('St. Louis Cardinals'))
                               , 1, 0)
        
        # Drop unnecessary columns
        df = df.drop(columns=['Rk', 'Gtm', 'Unnamed: 4'])

        # create dummies dataframe using .get_dummies(column_names,not dropping any of the dummy columns)
        categorical_features = ['Team','handedness_opp_pitcher']

        dummy_df = pd.get_dummies(df, columns=categorical_features, drop_first=False)
  
        # join original df with dummies df using .concat([original_df,dummy_df])
        #df = pd.concat([df, dummy_df], axis=1)

        df.to_csv(r'baseball.csv', index=False)

        return df


# ### Takeaways:
# 
# - Created 'is_away' column to capture that the game was played away, not at home stadium
# - Renamed columns for easier readability
# - Created 'is_win' column to capture the result of the game, win or loss
# - Created 'made_playoffs' to capture whether the team made it to the playoffs
# - Dropped unnecessary columns, "Rk", "Gtm", "Unnamed: 4" and  because they were used on the website to show the count of the columns in the table, the game number of the season, and the "@" to indicate away game which a new column was created to capture.  
# - Created function, prepare_data(), to clean up and prepare all data acquired as described above
# - Created dummy variables for categorical features



def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test

#Plots a normalized value count as a percent using catplot
def category_percentages_by_another_category_col(df, category_a, category_b):
    """
    Produces a .catplot with a normalized value count
    """
    (df.groupby(category_b)[category_a].value_counts(normalize=True)
    .rename('percent')
    .reset_index()
    .pipe((sns.catplot, 'data'), x=category_a, y='percent', col=category_b, kind='bar', ))