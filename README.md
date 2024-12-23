##  Car Dheko - Used Car Price Prediction

### Overview
This project aims to predict the price of a used car based on various features such as make, model, year, mileage, and more. The model utilizes machine learning algorithms to make predictions on used car prices, providing an accurate estimate based on the provided input.

## Table of content 

- Project description 
- Tech stacks 
- Dataset inspection 
- EDA(Exploratory data analysis)
- Data preprocessing 
- Models
- Model evaluation
- Pickling
- Installation 

### Project description
The goal of this project is to build a machine learning model capable of predicting the price of used cars based on multiple features. This could help car dealerships, buyers, or sellers get an estimate of a car's worth in the used car market.

### Tech stacks
- Python
- Pandas
- Streamlit
- Sklearn machine learning models
- Matplotlib/Seaborn
- Html/Css
- Pipline

### Dataset inspection 
Upon initial review, the data appears to have missing values in the dictionary type, and it is in JSON format.
Ast module in Python is used to extract dictionary literal from the JSON format.

### EDA(Exploratory data analysis)
EDA(Exploratory data analysis) has been performed to find correlations, trend patterns and data distribution.

### Data preprocessing
- One-Hot encoding - Convert categorical value into a numerical value
- IQR(inter qurantile range) - Remove outliers
- StandardScaler - Scaling data with mean of 0 and deviation of 1 

### Models
- Linear Regression 
- Decision Trees 
- Random Forests 
- Gradient Boosting
- Lasso(L1)
- Ridge(L2)

#### Hyperparametric tunning
Hyperparameter tuning was performed to enhance the model's performance and improve prediction accuracy. The *RandomizedSearchCV* function from Scikit-learn was used for this hyperparameter optimization.

### Model evaluation
- R-squared (R2)
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

### Pickling
Pickling, also known as saving data in binary format, involves storing the selected model as a pickle file, making it easily accessible and usable by anyone.






## Run Locally

Clone the project

```bash
  git clone https://github.com/Ukeshvaran/car_dekho_project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install requirements.txt
```
unpickling
```bash
  with open('Pipeline.pkl','rb') as file:
    loaded=pickle.load(file)
```
prediction
```bash
  loaded.predict(data)
```

## App Screenshots

![](https://github.com/Ukeshvaran/car_dekho_project/blob/fb00b864c669e5a72bbe30c1cb34d05f5d817952/car_dheko_1.png)

![](https://github.com/Ukeshvaran/car_dekho_project/blob/fb00b864c669e5a72bbe30c1cb34d05f5d817952/car_dheko_2.png)

![](https://github.com/Ukeshvaran/car_dekho_project/blob/fb00b864c669e5a72bbe30c1cb34d05f5d817952/car_dheko_3.png)