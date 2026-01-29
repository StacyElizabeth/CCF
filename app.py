"""
Simple Flask API for Credit Card Fraud Detection
Run: python app.py
Then open: http://localhost:5000 in your browser
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__, template_folder='.', static_folder='.')
CORS(app)

# Load the trained model
MODEL_PATH = 'credit_card_model.pkl'
model = None

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully!")
    else:
        print(f"Warning: Model file '{MODEL_PATH}' not found. Run your notebook first.")

@app.route('/')
def index():
    """Serve the HTML frontend"""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """Make a prediction for a single transaction"""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 400
        
        data = request.json
        
        # Extract features - must match the order used in training
        # Expected: Time, V1-V28, Amount (30 features total)
        features = [
            data.get('time', 0),
            data.get('v1', 0), data.get('v2', 0), data.get('v3', 0),
            data.get('v4', 0), data.get('v5', 0), data.get('v6', 0),
            data.get('v7', 0), data.get('v8', 0), data.get('v9', 0),
            data.get('v10', 0), data.get('v11', 0), data.get('v12', 0),
            data.get('v13', 0), data.get('v14', 0), data.get('v15', 0),
            data.get('v16', 0), data.get('v17', 0), data.get('v18', 0),
            data.get('v19', 0), data.get('v20', 0), data.get('v21', 0),
            data.get('v22', 0), data.get('v23', 0), data.get('v24', 0),
            data.get('v25', 0), data.get('v26', 0), data.get('v27', 0),
            data.get('v28', 0), data.get('amount', 0)
        ]
        
        # Make prediction
        X = np.array([features])
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]
        
        return jsonify({
            'prediction': int(prediction),
            'fraud': prediction == 1,
            'confidence_legitimate': float(probability[0]),
            'confidence_fraud': float(probability[1]),
            'message': 'Fraudulent Transaction' if prediction == 1 else 'Legitimate Transaction'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/predict-batch', methods=['POST'])
def predict_batch():
    """Process a CSV file and predict fraud for all transactions"""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 400
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'Empty filename'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File must be CSV format'}), 400
        
        # Read CSV
        df = pd.read_csv(file)
        
        # Check if required columns exist
        if 'Class' in df.columns:
            df_pred = df.drop('Class', axis=1)
            true_labels = df['Class'].values
        else:
            df_pred = df
            true_labels = None
        
        # Make predictions
        predictions = model.predict(df_pred)
        probabilities = model.predict_proba(df_pred)
        
        # Calculate statistics
        fraud_count = np.sum(predictions == 1)
        legit_count = np.sum(predictions == 0)
        
        results = {
            'total_transactions': len(predictions),
            'fraud_detected': int(fraud_count),
            'legitimate': int(legit_count),
            'fraud_percentage': round((fraud_count / len(predictions)) * 100, 2),
            'predictions': predictions.tolist(),
            'confidence_scores': [
                {'legitimate': float(prob[0]), 'fraud': float(prob[1])} 
                for prob in probabilities
            ]
        }
        
        # Add accuracy if true labels are available
        if true_labels is not None:
            from sklearn.metrics import accuracy_score
            accuracy = accuracy_score(true_labels, predictions)
            results['accuracy'] = round(accuracy, 4)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/model-info', methods=['GET'])
def model_info():
    """Get information about the model"""
    return jsonify({
        'model_loaded': model is not None,
        'training_accuracy': 0.95,
        'test_accuracy': 0.913,
        'model_type': 'Logistic Regression',
        'features_count': 30,
        'classes': ['Legitimate', 'Fraudulent']
    })

if __name__ == '__main__':
    load_model()
    print("Starting Credit Card Fraud Detection API...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
