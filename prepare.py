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



def prepare_data():
    
    import warnings
    warnings.filterwarnings('ignore')

    import pandas as pd
    import numpy as np

    import acquire
    
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
    
    #Create new column with result, is_win, where 1 is a win and 0 is a loss for every game
    df['is_win'] = np.where(df.Rslt.str.startswith('W'), 1, 0)
    
    
    # Drop unnecessary columns
    df = df.drop(columns=['Rk', 'Gtm', 'Unnamed: 4'])
    
    
    return df


# ### Takeaways:
# 
# - Created 'is_away' column to capture that the game was played away, not at home stadium
# - Renamed columns for easier readability
# - Created 'is_win' column to capture the result of the game, win or loss
# - Dropped unnecessary columns, "Rk", "Gtm", "Unnamed: 4" and  because they were used on the website to show the count of the columns in the table, the game number of the season, and the "@" to indicate away game which a new column was created to capture.  
# - Created function, prepare_data(), to clean up and prepare all data acquired as described above
