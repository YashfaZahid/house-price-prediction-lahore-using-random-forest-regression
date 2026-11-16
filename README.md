# Lahore house prices

A Random Forest regression notebook for Lahore residential listings. The dataset is `houseDataset2024.csv`. The training workflow is `Copy_of_House_Price_Prediction.ipynb`.

## What is in this repository

- Listings with location, area, bedrooms, bathrooms, and price
- Cleaning: nulls, duplicates, and outlier handling
- One-hot encoding of location
- A Random Forest regressor, with train and test R² printed in the notebook

This repository is the model study. It does not include a Flask app or a frontend. An earlier note described a web form. Those files are not here. Run the notebook to reproduce the fit.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas numpy scikit-learn matplotlib jupyter
jupyter notebook Copy_of_House_Price_Prediction.ipynb
```

## Limits

The score is on this Kaggle-style Lahore extract, with the split and filters in the notebook. It is not a valuation and it will not transfer cleanly to another city or another year without new data.
