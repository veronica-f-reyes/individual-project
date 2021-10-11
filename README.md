# Can We Predict Major League Baseball Outcomes?
#### Finding drivers of winning baseball teams and using machine learning to predict whether an MLB team will win or not.
***
## Executive Summary:

## Project Planning:
#### PLAN -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

Working through the data science pipeline, I will acquire data using an acquire.py file which pulls data from the Telco churn database using SQL and joins 3 tables. I will prepare the data using a prepare.py file which will get rid of unneeded columns, encode string values to 0s and 1s and create dummies. Then I will explore the data by looking for possible relationships be Ien features and look at how they are distribute by creating plots and looking at the data. Next I will create models using Decision Tree, Random Forest and K - Nearest Neighbors Classifiers. I will then compare the models that Ire run on training data to validate data before running our model on the test data to get the final accuracy. I will then present the Jupyter Notebook with the code of this entire process to the class.

## Project Objectives

Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
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
