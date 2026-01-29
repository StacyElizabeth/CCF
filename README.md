# CCF
credit card fraud detection
# Credit Card Fraud Detection

This project implements a Machine Learning model to detect fraudulent credit card transactions using Logistic Regression.

## Dataset Information
The project uses a dataset of credit card transactions (`creditcard.csv`). 
- **Legit Transactions**: 284,315
- **Fraudulent Transactions**: 492

The data is highly unbalanced, which is handled in the analysis by comparing the mean values of features for both classes.

## Model Performance
The model is built using `scikit-learn`'s `LogisticRegression`. 
- **Accuracy on Test Data**: ~91.37%

## How to Run
1. Clone this repository.
2. Ensure you have `creditcard.csv` in the root directory.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the Jupyter Notebook `CredFrad (1).ipynb`.
