# Predicting Major League Baseball (MLB) Outcomes
***
![baseball_stadium](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOfGMVLGclDKdofCZqf_jD6Dq6dUnPK0Rsmw&usqp=CAU)

## Executive Summary

### Overview:

Professional baseball in the US, or Major League Baseball, is comprised of 30 teams that play 162 baseball games every year. Official game statistics are kept for every game and have been kept since the mid-1800s. With so much data and statistics, fans and team managers have the opportunity to look back and better understand the game. The understanding and analysis of baseball data can help differentiate the performance of a better performing baseball player or a better performing baseball club.

As a long time fan of baseball having grown up with a family of baseball players and fans, I chose to use MLB data for my individual project.

In this project, I seek to better understand the game of baseball and to forecast MLB game outcomes by creating machine learning models. I will create a classification model that will try to predict whether a team will win or lose a game and a linear regresssion model that will try to predict the number of runs in a game using hitting data for games that were already played. I also seek to determine what drivers are indicators of a win and scoring.


### Project Goals

- Use MLB baseball hitting data for all 30 teams for the 2021 season
- Find drivers for team wins using baseball data. 
- Create a machine learning classification model that predicts team wins
- Find drivers of runs scored
- Create a regression model to predict the number of runs scored in a baseball game


### Project Deliverables

- A final report notebook


### Project Context

- I will be using the baseball team hitting game logs data for all 30 MLB team datasets from baseball-reference.com.

- The target variable for this assessment is going to be the feature `is_win` for the classification model and `runs_scored` for the linear regression model.

### DATA DICTIONARY

----------------

|Target|Datatype|Definition|
|:-------|:--------|:----------|
| is_win                  |4858 non-nul:   int64 | indicator 0 or 1 for result of game; 0 is a loss, 1 is a win| |              |
| runs_scored| 4858 non-nul:   int64|  number of runs scored in a game|   |


|Feature|Datatype|Definition|
|:-------|:--------|:----------| 
|Team|                   4858 non-null   object |Name of Major League Baseball Team|
|Date |                   4858 non-null   object | Date the baseball game was played|
|Opp  |                   4858 non-null   object | Name of the opposing team|
|Rslt  |                  4858 non-null   object | Result with score of the game|
|plate_app   |            4858 non-null   int64  | Number of plate appearance|
|at_bats|                 4858 non-null   int64  | Number of at bats|
|runs_scored |            4858 non-null   int64  | Number of runs scored|
|hits      |              4858 non-null   int64  | Number of hits|
|doubles   |              4858 non-null   int64  |Number of doubles|
|triples |                4858 non-null   int64  |Number of triples|
|HR     |                 4858 non-null   int64  |Number of home runs|
|RBI   |                  4858 non-null   int64  |Runs batted in|
|bases_on_balls |         4858 non-null   int64  |Bases on balls; walks|
|intentional_bb |         4858 non-null   int64  |Intentional walks|
|strikeouts    |          4858 non-null   int64  |Number of strikeouts|
|hit_by_pitch  |          4858 non-null   int64  |Number of times hit by pitch|
|sac_hits |               4858 non-null   int64  |Sacrifice hits|
|sac_flies  |             4858 non-null   int64  |Sacrifice fly balls|
|reached_on_error|        4858 non-null   int64  |Bases reached on error|
|double_plays |           4858 non-null   int64  |Number of double plays|
|stolen_bases |           4858 non-null   int64  |Number of stolen bases|
|caught_stealing |        4858 non-null   int64  |Number of times caught stealing a base|
|batting_avg   |          4858 non-null   float64|Batting average|
|OBP      |               4858 non-null   float64|On base percentage|
|SLG   |                  4858 non-null   float64|Slugging percentage; (Hits+(2*Doubles)+(3*Triples)+(4*Homeruns)/Number of at bats|
|OPS   |                  4858 non-null   float64|OBP + SLG|
|left_on_base |           4858 non-null   int64  |Number of players left on base|
|num_players_used  |      4858 non-null   int64  |Number of players used in a game|
|handedness_opp_pitcher | 4858 non-null   object |Opposing pitcher handedness, left or right|
|Opp. Starter (GmeSc) |   4858 non-null   object |Name of opposing pitcher|
|is_away      |           4858 non-null   int64  |Indicator whether game was away; 0 was not away, 1 was away|
|is_win    |              4858 non-null   int64  |Indicator whether game was won; 0 was lost, 1 was won|
|made_playoffs |          4858 non-null   int64 |Indicator whether team made playoffs; 0 not made playoffs, 1 did make playoffs|

# DATA SCIENCE PIPELINE
***
 

## PLAN:
***
#### PLAN -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

See my Trello board here --> https://trello.com/b/D3fCAVA7/baseball-project

Working through the data science pipeline, I will acquire data from baseball-reference.com.  I will download all 30 MLB teams' baseball hitting game logs and combine them into one .csv file. I will prepare the data using a prepare.py file which will get rid of unneeded columns,rename columns,  and create new columns to capture rolling averages and encode columns. Then I will explore the data by looking for possible relationships between features and look at how they are distributed by creating plots and looking at the data. Next I will create models using Decision Tree, Random Forest and K - Nearest Neighbors Classifiers. I will then compare the models that were run on training data to validate data before running our model on the test data to get the final accuracy. I will then create linear regression models using Linear Regressor, Tweedie Regressor, Lasso Lars Regressors, and Polynomial Linear Regressors, evaluate model performance and then run the best model on out of sample data.  I will then create and turn in a final Jupyter Notebook with the code of this entire process.

## ACQUIRE: 
***
####  Plan -> ACQUIRE -> Prepare -> Explore -> Model & Evaluate -> Deliver

### Obtain Major League Baseball Data from baseball-reference.com

- All data is acquired from batting game logs for all 30 Major League Baseball teams for the year 2021
- Baseball data was exported into an Excel file from the website for each baseball team
- All batting logs were then combined into one .csv file
- Data source is baseball-reference.com
- Acquired 4858 rows of data

## PREPARE:
***
#### Plan -> Acquire -> PREPARE -> Explore -> Model & Evaluate -> Deliver

I prepped and cleaned the data acquired from baseball-reference.com. I then used functions in prepare.py to accomplish the following:

- Create 3 game rolling average columns for all hitting stats for use in predictive modeling
- Create 'is_away' column to capture that the game was played away, not at home stadium
Renamed columns for easier readability
- Create 'is_win' column to capture the result of the game, win or loss
- Create 'made_playoffs' to capture whether the team made it to the playoffs
- Dropp unnecessary columns, "Rk", "Gtm", "Unnamed: 4" and because they were used on the website to show the count of the columns in the table, the game number of the season, and the "@" to indicate away game which a new column was created to capture.
- Create function, prepare_data(), to clean up and prepare all data acquired as described above
- Create dummy variables for categorical features


## EXPLORE:
***
#### Plan -> Acquire -> Prepare -> EXPLORE -> Model & Evaluate -> Deliver
I visualized combinations of variables to compare relationships and check for independence or correlation between variables.

For the classification model predicting whether the team won, I ran statistical tests for independence for the following questions:

### Hypothesis 1: Is winning related to number of runs scored?  

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0): There is no difference between number of runs scored in a winning game and the overall average.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a) : There is a difference between number of runs scored in a winning game  and the overall average.

`FINDING`: We reject the hypothesis that winning is not related to number of runs scored

### Hypothesis 2: Does number of hits differ by winning teams?  

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no difference between number of hits by winning teams and the overall average.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a difference between number of hits by winning teams and the overall average.

`FINDING`: We reject the hypothesis that winning is not related to number of hits in a game

### Hypothesis  3: Does number of homeruns differ by winning teams?  

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no difference between number of homeruns by winning teams and the overall average.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a) : There is a difference between number of homeruns by winning teams and the overall average.

`FINDING`: We reject the hypothesis that winning is not related to number of homeruns in a game

### Hypothesis 4: Is winning related to the number of runs batted in (RBI)?  

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no difference between number of runs batted in in a winning game and the overall average.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a difference between number of runs batted in in a winning game  and the overall average.

`FINDING`: We reject the hypothesis that winning is not related to number of runs batted in a game

### Hypothesis 5: Is winning related to the number of total appearances at the plate by a player in the game? 

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no relationship between winning and the number of plate appearances.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a relationship between winning and the number of plate appearances.

`FINDING`: We reject the hypothesis that winning is not related to number of total plate appearances in a game

### Hypothesis 6: Is winning related to the number of doubles that were hit in the game?

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no relationship between winning and the number of doubles in a game.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a relationship between winning and the number of doubles in a game.

`FINDING`: We reject the hypothesis that winning is not related to number of doubles hit in a game

### Hypothesis 7: Is winning related to the number of bases that were obtained by being walked by the pitcher? 

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no relationship between winning and the number of walks in a game.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a relationship between winning and the number of walks in a game.

`FINDING`: We reject the hypothesis that winning is not related to number of walks in a game

### Hypothesis  8: Is winning related to whether the team is playing away?  

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_0) : There is no relationship between winning and a team playing away.

![equation](https://latex.codecogs.com/gif.latex?%5Cinline%20H_a): There is a relationship between winning and a team playing away.

`FINDING`: We reject the hypothesis that winning is independent of whether a team is playing away


For the linear regression models predicting the number of runs scored, I ran statistical tests for independence.

## MODEL:
***
#### Plan -> Acquire -> Prepare -> Explore -> MODEL -> Deliver

The goal is to develop a classification and regression model that performs better than the baseline.

#### For the classification model predicting whether a team would win or lose, I chose the Random Forest model because of its highest accuracy in both train and validate with low overfitting.

- Random Forest Model had an accuracy of 58% using out of sample data
- This was higher than the baseline accuracy of 50%

- Features used for this model included 3 game rolling averages for:
    - `'roll_runs_scored'` - runs scored
    - `'roll_RBI'` - RBI
    - `'roll_hits'` - hits per game
    - `'roll_HR'` - homeruns
    - `'roll_plate_app'` - total plate appearances
    - `'roll_doubles'` - doubles
    - `'roll_bases_on_balls'` - walks or bases on balls
    
#### For linear regression model predicting number of runs, I chose the Ordinary Least Squares Linear Regression model due to its lowest RMSE and highest explained variance, $R^2$

- The Linear Regression model performed well on out of sample (test) data beating the baseline with an explained variance score, $R^2$, of 17% and came up with the lowest RMSE of 2.76.
- Features used for this model include rolling averages for the following baseball hitting stats:
    - `'roll_RBI'` - runs batted in; a stat indicating that a baseball player got a hit that resulted in a run being scored. 
    - `'roll_OBP'` - on base percentage; a stat capturing the percentage a number times a player gets on base
    - `'roll_SLG'` - slugging percentage; a stat capturing the hitting 'power' of a baseball player by giving more weight to more base earned hits; Total Bases/At Bats or (1B + 2*2B + 3*3B + 4*HR)/AB
    - `'roll_OPS'` - a combination of OBP and SLP to measure a baseball players ability to get on base and hit the ball; On-Base + Slugging Percentages
    - `'roll_batting_avg'` - the average number of times a baseball player hit the ball and got on base; Hits/At Bats

## DELIVER:
***
#### Plan -> Acquire -> Prepare -> Explore -> Model -> DELIVER
- The final product will be a Github repository containing your work with any .py files required to acquire and prepare the data and a clearly labeled final Jupyter Notebook that walks through the pipeline.


## HOW TO RECREATE THIS PROJECT:
***

To recreate this project you will need the following files from this repository:

- README.md
- acquire.py
- prepare.py
- Final_Baseball_Project_Notebook.ipynb
- baseball.csv 

### Instructions:

- Read the README.md
- Download the acquire.py, prepare.py, baseball.csv and Final_Baseball_Project_Notebook.ipynb files into your working directory, or clone this repository
- Run the Final_Baseball_Project_Notebook.ipynb