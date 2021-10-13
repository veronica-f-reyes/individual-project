# Can We Predict Major League Baseball Outcomes?
#### Finding drivers of winning baseball teams and using machine learning to predict whether an MLB team will win or not.
***
## Executive Summary:

## Project Planning:
#### PLAN -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

Working through the data science pipeline, I will acquire data using an acquire.py file which pulls data from the Telco churn database using SQL and joins 3 tables. I will prepare the data using a prepare.py file which will get rid of unneeded columns, encode string values to 0s and 1s and create dummies. Then I will explore the data by looking for possible relationships be Ien features and look at how they are distribute by creating plots and looking at the data. Next I will create models using Decision Tree, Random Forest and K - Nearest Neighbors Classifiers. I will then compare the models that were run on training data to validate data before running our model on the test data to get the final accuracy. I will then turn in the Jupyter Notebook with the code of this entire process.

## Project Objectives

Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation, findings, and key takeaways in a Jupyter Notebook report.
Create modules (acquire.py, prepare.py or wrangle.py) that make your process repeateable.
Construct a model to predict team wins using classification techniques.
Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.


### Business Goals

Find drivers for team wins using baseball data. Why do teams win?
Construct a ML classification model that accurately predicts team wins.
Document your process well enough to be presented or read like a report.

### Project Deliverables

A final report notebook
All necessary modules to make my project reproducible

### Project Context

I will be using the baseball team logging for batting and ptiching for all 30 MLB team datasets from baseball-reference.com.

The target variable for this assessment is going to be the feature Result.

### Data Dictionary

 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   Team                    4858 non-null   object 
 1   Date                    4858 non-null   object 
 2   Opp                     4858 non-null   object 
 3   Rslt                    4858 non-null   object 
 4   plate_app               4858 non-null   int64  
 5   at_bats                 4858 non-null   int64  
 6   runs_scored             4858 non-null   int64  
 7   hits                    4858 non-null   int64  
 8   doubles                 4858 non-null   int64  
 9   triples                 4858 non-null   int64  
 10  HR                      4858 non-null   int64  
 11  RBI                     4858 non-null   int64  
 12  bases_on_balls          4858 non-null   int64  
 13  intentional_bb          4858 non-null   int64  
 14  strikeouts              4858 non-null   int64  
 15  hit_by_pitch            4858 non-null   int64  
 16  sac_hits                4858 non-null   int64  
 17  sac_flies               4858 non-null   int64  
 18  reached_on_error        4858 non-null   int64  
 19  double_plays            4858 non-null   int64  
 20  stolen_bases            4858 non-null   int64  
 21  caught_stealing         4858 non-null   int64  
 22  batting_avg             4858 non-null   float64
 23  OBP                     4858 non-null   float64
 24  SLG                     4858 non-null   float64
 25  OPS                     4858 non-null   float64
 26  left_on_base            4858 non-null   int64  
 27  num_players_used        4858 non-null   int64  
 28  handedness_opp_pitcher  4858 non-null   object 
 29  Opp. Starter (GmeSc)    4858 non-null   object 
 30  is_away                 4858 non-null   int64  
 31  is_win                  4858 non-null   int64  
 32  made_playoffs           4858 non-null   int64 



## Acquire

### Obtain Major League Baseball Data from baseball-reference.com

- All data is acquired from batting game logs for all 30 Major League Baseball teams for the year 2021
- Baseball data was exported into an Excel file from the website for each baseball team
- All batting logs were then combined into one .csv file
- Data source is baseball-reference.com