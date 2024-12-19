# Project_4

Project Objective

  The purpose of this project is to create a model that accurately predicts the presence of cardiovascular disease. The information used to accomplish this includes age, systolic blood pressure, diastolic blood pressure, body mass index, and blood pressure category to help create an accurate prediction.

Data Source

  Cardiovascular Disease Dataset (Kaggle) https://www.kaggle.com/datasets/colewelkins/cardiovascular-disease
This dataset of about 7000 records provides a comprehensive analysis of factors predicting the presence or absence of cardiovascular disease based on various patient metrics. It includes demographic information, physical fitness, and health conditions that may contribute to cardiovascular strength. 

Technical Stack

  Languages: Python
  Libraries : 
      Visualization : Pyplot
      Data Handling : Pandas
  Database: SQL

SQL Database & Flask

  The dataset for this analysis was sourced from Kaggle and downloaded in CSV format. To manage the data, a database named "project4" was set up in pgAdmin. An app.py was created with Flask to generate the backend datasource for the project. Flask_sqlalchemy was used to query the SQL database.

Correlation Matrix

  We ended up running a quick correlation matrix to determine what features contribute to cardiovascular disease.  We used this information to help eliminate variables such as height, gender, glucose levels, smoking status, alcohol intake, and physical activity.

Random Forest Classification Model

  Choose this model because it is good with High-dimensional data and resistant to outliers.
Parameters I attempted to utilize to increase accuracy:
      Number of trees
      Max depth of each decision tree
      Min number of samples to split
      Min number of samples required to be in a leaf node
GridSearchCV was used to run multiple of these parameters at once to find best model.
Model accuracy: 0.7229

XGBClassifier Model

  Choose this model second because it offered Hyperparameter tuning. Downside to this model is it can be over complex.  Could have contributed to lower accuracy compared to the RFC.
  The additional parameters included:
        Learning rate
        Subsample
        Column Sample by Tree
  GridSearchCV was used to run multiple of these parameters at once to find best model.
  Model Accuracy: 0.7215

Neural Network

   I set up a Tensorflow Keras Neural Network.  For my data, I used cardio as the target, and height, weight, active, gluc, gender, alco, and smoke due to low correlation with the cardio data.  My model has 9 iput dimensions,two hidden relu layers, with 64 neurons each, and a sigmoid output.  There are 50 epochs.  My model accuracy was 0.73369 and loss was 0.13926

Logistics Regression

The second model that I used was a Logistics Regression model.  The solver I used was ‘lbfgs’, with max iterations at 1000, and a random state of 78.  The accuracy scored out at 0.72542

Tablea

  https://public.tableau.com/views/Proyect_Hyper_4/Dashboard2?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

Mock Data

Working with the cardiovascular dataset, Numpy was used to set a random seed for reproducibility. Mock data was generated after listing categorical data. Data was organized into a dataframe and saved into a csv file in order to test our model
