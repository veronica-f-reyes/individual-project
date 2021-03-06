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
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score


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
                                (df['Team'].str.contains('Tampa Bay Rays'))|
                               (df['Team'].str.contains('St. Louis Cardinals'))
                               , 1, 0)

        #Feature Engineering: Create rolling averages per team using the last 3 games to use for modeling
        df['roll_plate_app'] = df.groupby('Team')['plate_app'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_at_bats'] = df.groupby('Team')['at_bats'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_runs_scored'] = df.groupby('Team')['runs_scored'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_hits'] = df.groupby('Team')['hits'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_doubles'] = df.groupby('Team')['doubles'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_triples'] = df.groupby('Team')['triples'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_HR'] = df.groupby('Team')['HR'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_RBI']= df.groupby('Team')['RBI'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_bases_on_balls']= df.groupby('Team')['bases_on_balls'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_intentional_bb']= df.groupby('Team')['intentional_bb'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_strikeouts']= df.groupby('Team')['strikeouts'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_hit_by_pitch']= df.groupby('Team')['hit_by_pitch'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_sac_hits']= df.groupby('Team')['sac_hits'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_sac_flies']= df.groupby('Team')['sac_flies'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_reached_on_error']= df.groupby('Team')['reached_on_error'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_double_plays']= df.groupby('Team')['double_plays'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_stolen_bases']= df.groupby('Team')['stolen_bases'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_caught_stealing']= df.groupby('Team')['caught_stealing'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_batting_avg']= df.groupby('Team')['batting_avg'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_OBP']= df.groupby('Team')['OBP'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_SLG']= df.groupby('Team')['SLG'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_OPS']= df.groupby('Team')['OPS'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_left_on_base']= df.groupby('Team')['left_on_base'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_num_players_used']= df.groupby('Team')['num_players_used'].transform(lambda x: x.rolling(3, 1).mean())
        df['roll_is_win'] = df.groupby('Team')['is_win'].transform(lambda x: x.rolling(3, 1).mean())                       
        
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


def make_metric_df(y, y_pred, model_name, metric_df):
    if metric_df.size ==0:
        metric_df = pd.DataFrame(data=[
            {
            'model': model_name, 
            'RMSE_validate': mean_squared_error(
                y,
                y_pred) ** .5,
            'r^2_validate': explained_variance_score(
                y,
                y_pred)
            }])
        return metric_df
    else:
        return metric_df.append(
        {
            'model': model_name, 
            'RMSE_validate': mean_squared_error(
                y,
                y_pred) ** .5,
            'r^2_validate': explained_variance_score(
                y,
                y_pred)
        }, ignore_index=True)

def was_hypothesis_rejected(alpha, null_hyp, p):

    if p < alpha:
        print("We reject the hypothesis that", null_hyp)
    else:
        print("We fail to reject the null hypothesis")
    
    return
            