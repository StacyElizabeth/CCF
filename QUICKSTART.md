# 🚀 Credit Card Fraud Detection - Black Background Frontend

## What You Got

A complete, working fraud detection web application with:
- **Sleek black background UI** with cyan/blue accents
- **No complicated installations** - just Flask + standard libraries
- **Single transaction prediction** - input features and get instant results
- **Batch CSV processing** - analyze multiple transactions at once
- **Responsive design** - works on desktop and mobile
- **Flask backend** - integrates your trained Logistic Regression model

---

## 📋 Quick Setup (3 Simple Steps)

### Step 1: First, Generate Your Model
Make sure your Jupyter notebook has been run:
1. Open `CredFrad.ipynb` in VS Code
2. Run all cells (Ctrl+Alt+Enter or use Run All)
3. This creates `credit_card_model.pkl` which the app needs

### Step 2: Install Dependencies
Open PowerShell/Command Prompt in your `Credfrad` folder and run:
```bash
pip install -r requirements.txt
```

This installs:
- Flask (web server)
- Flask-CORS (for API requests)
- pandas (data handling)
- scikit-learn (ML library)
- numpy (numerical computing)

### Step 3: Run the Application
```bash
python app.py
```

Or simply double-click `run.bat` on Windows!

Then open your browser: **http://localhost:5000**

---

## 🎨 Features

### Single Transaction Analysis
- Input transaction features (Time, Amount, V1-V28)
- Get instant fraud prediction
- See confidence scores
- Color-coded results (Green = Legitimate, Red = Fraud)

### Batch CSV Processing
- Upload entire CSV files
- Process multiple transactions at once
- Get fraud rate statistics
- See accuracy metrics

### Model Information
- Training accuracy: **95%**
- Test accuracy: **91.3%**
- Model type: Logistic Regression
- Features: 30 (Time + V1-V28 + Amount)

---

## 📁 File Structure

```
Credfrad/
├── index.html                 # Beautiful black-themed frontend
├── app.py                     # Flask backend server (80 lines)
├── credit_card_model.pkl      # Your trained model
├── creditcard.csv             # Original dataset
├── CredFrad.ipynb            # Your analysis notebook
├── requirements.txt           # Python dependencies
├── run.bat                    # Windows quick start
└── README.md                  # Full documentation
```

---

## 🔗 API Endpoints

If you want to integrate with other apps:

```
POST /api/predict
{
  "time": 0,
  "amount": 100,
  "v1": -1.35, "v2": -0.07, "v3": 2.53,
  ...
}
Returns: { fraud: true/false, confidence_fraud: 0.95, confidence_legitimate: 0.05 }

POST /api/predict-batch
- Upload CSV file
Returns: { total_transactions, fraud_detected, fraud_percentage, accuracy }

GET /api/model-info
Returns: Model statistics and configuration
```

---

## ⚡ Quick Testing

### Test Single Prediction:
1. Open the app in browser
2. Enter sample values:
   - Amount: 100
   - Time: 50000
   - V1: -1.35
   - V2: -0.07
   - V3: 2.53
3. Click "Analyze Transaction"
4. See prediction result

### Test Batch Processing:
1. Click on the CSV upload section
2. Upload your `creditcard.csv` file
3. See fraud statistics

---

## 🛠️ Troubleshooting

**"Model not loaded" error:**
- Make sure `credit_card_model.pkl` exists (run notebook first)

**"Port 5000 already in use":**
- Edit `app.py` line at bottom: `app.run(port=5001)`

**"Module not found":**
- Run: `pip install -r requirements.txt`

**CORS errors:**
- Already handled - Flask-CORS is configured

---

## 🎯 No Complications!

✅ No Docker needed
✅ No npm/node_modules bloat
✅ No build tools required
✅ No complex deployment
✅ Pure Python + HTML/CSS/JavaScript
✅ Works offline (after initial setup)

Just install requirements and run!

---

## 📞 Need Help?

1. **Check the terminal** - Flask shows error messages
2. **Check the browser console** - JavaScript errors shown there (F12)
3. **Verify model file** - Make sure `credit_card_model.pkl` exists
4. **Test the backend** - Visit `http://localhost:5000/api/model-info`

---

## 🚀 Ready to Deploy?

Want to share this with others?

1. **On local network:**
   - In `app.py` change: `app.run(host='0.0.0.0', port=5000)`
   - Access from other computers: `http://your-ip:5000`

2. **On the internet:**
   - Use services like Heroku, PythonAnywhere, or Replit
   - Upload your 5 files (index.html, app.py, model.pkl, requirements.txt, README.md)

---

**Enjoy your fraud detection app! 🔐**
