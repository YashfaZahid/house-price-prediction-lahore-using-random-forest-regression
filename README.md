# **House Price Prediction using Random Forest**

This is a machine learning web application that predicts house prices based on features like location, number of bedrooms, bathrooms, and area. The model is trained using a **Random Forest Regressor** and deployed with a **Flask** backend and a simple **HTML/CSS/JavaScript** frontend.

---

## **Technologies Used**

- **Python** – for data processing and model training
- **Pandas** – for data manipulation and cleaning
- **NumPy** – for numerical operations
- **Matplotlib** – for data visualization
- **Scikit-learn** – for machine learning (Random Forest Regression)
- **Pickle** – for model serialization
- **Flask** – for backend API/server
- **HTML, CSS, JavaScript** – for frontend interface

---

## **Dataset**

- Sourced from **Kaggle**
- Contains real estate listings with features such as:
  - Location (city, address)
  - Area in square feet
  - Bedrooms and bathrooms
  - Price and price per square foot

---

## **Features**

- Cleaned dataset (removed nulls, duplicates, and outliers)
- Converted categorical columns using one-hot encoding
- Correlation heatmap and statistical filtering to handle outliers
- Trained using **Random Forest Regressor** with optimized parameters
- Performance evaluated using **R² score** for both training and test sets
- Frontend allows user to input house details and get an instant price estimate

---

## **How It Works**

1. User fills out a form with property details.
2. Flask backend receives input and loads the trained model.
3. Model processes the input and returns a price prediction.
4. Frontend displays the predicted house price.
