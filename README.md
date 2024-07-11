
# Medical Insurance Cost Prediction

## 🚀 Technologies
The following tools were used in this project:

Python

Pandas

Matplotlib

Seaborn

SciKit-Learn

Flask


## Project description


The purpose of this project is to determine the contributing factors and predict health insurance cost by performing exploratory data analysis and predictive modeling on the Health Insurance dataset. This project makes use of Numpy, Pandas, Sci-kit learn, and EDA Techniques for data visualization.

Overview:
• Seek insight from the dataset with Exploratory Data Analysis
• Performed Data Processing, Data Engineering and Feature Transformation to prepare data before modeling
• Built a model to predict Insurance Cost based on the features
• Evaluated the model using various Performance Metrics like RMSE, R2, Testing Accuracy, Training Accuracy and MAE

## About Dataset

Data source : https://www.kaggle.com/mirichoi0218/insurance

1. age: age of primary beneficiary
2. sex: insurance contractor gender, female, male
3. bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
4. children: Number of children covered by health insurance / Number of dependents
5. smoker: Smoking
6. region: the beneficiary's residential area in the US,       northeast, southeast, southwest, northwest
7. charges: Individual medical costs billed by health insurance

# Data Preprocessing

Check missing value - there are none

Check duplicate value - there are 1 duplicate and is removed

Feature transformation:
A) Mapping sex, region, & smoker attributes

Steps while training the model:
A) Target & features 

B) Splitting train & test data

C) Modeling using Linear Regression,Lasso, Ridge , Random 
Forest, Decision Tree, XGboost and Adaboost . 

D) Find the best algorithm i.e RandomForestRegressor 

E) Tuned the random Forest Regressor algorithm




## 🏁 How to start 
#### Clone this project
git clone https://github.com/Ujjwal6710/Medical-Cost-Prediction-Using-Regression.git

## Machine Learing Algorithms Comparison - 
|  Model Name |  R² Score |   
|---|---|
| Random Forest Regressor  | 0.854684  |   
| XGBRegressor  | 0.847914  |   
|  AdaBoost Regressor | 0.829981  |   
|  Linear Regression |  0.779735 |   
|  Lasso|	0.779713|
|Ridge|	0.779259|
|Decision Tree|	0.752976|
|K-Neighbors Regressor|	0.130766  |

###  After hyperparameter tuning for random forest regressor using grid search we received R2-score of 0.8777 . 


