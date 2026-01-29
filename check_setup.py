"""
Setup Validator - Check if everything is ready
Run: python check_setup.py
"""

import os
import sys

def check_file(filename):
    """Check if a file exists"""
    exists = os.path.exists(filename)
    status = "✓" if exists else "✗"
    print(f"  {status} {filename}")
    return exists

def check_module(module_name):
    """Check if a Python module is installed"""
    try:
        __import__(module_name)
        print(f"  ✓ {module_name}")
        return True
    except ImportError:
        print(f"  ✗ {module_name} (NOT INSTALLED)")
        return False

print("\n" + "="*50)
print("Credit Card Fraud Detection - Setup Checker")
print("="*50 + "\n")

# Check files
print("📁 Checking files...")
files_ok = True
files_ok &= check_file("index.html")
files_ok &= check_file("app.py")
files_ok &= check_file("demo.html")
files_ok &= check_file("requirements.txt")
files_ok &= check_file("creditcard.csv")
files_ok &= check_file("CredFrad.ipynb")

model_exists = check_file("credit_card_model.pkl")

# Check Python modules
print("\n📦 Checking Python modules...")
modules_ok = True
modules_ok &= check_module("flask")
modules_ok &= check_module("flask_cors")
modules_ok &= check_module("pandas")
modules_ok &= check_module("sklearn")
modules_ok &= check_module("numpy")

# Summary
print("\n" + "="*50)
print("SETUP STATUS")
print("="*50)

if files_ok and modules_ok and model_exists:
    print("\n✅ Everything is ready! Run: python app.py")
elif files_ok and modules_ok and not model_exists:
    print("\n⚠️  Files OK, Python modules OK")
    print("❌ Model not found: credit_card_model.pkl")
    print("\n📝 Action needed:")
    print("   1. Open CredFrad.ipynb in VS Code")
    print("   2. Run all cells (Ctrl+Alt+Enter)")
    print("   3. This will create credit_card_model.pkl")
    print("   4. Then run: python app.py")
elif not modules_ok:
    print("\n⚠️  Missing Python modules")
    print("\n📝 Action needed:")
    print("   pip install -r requirements.txt")
    print("   Then run this script again")
else:
    print("\n❌ Some files are missing!")
    print("Make sure all files are in the same directory")

print("\n" + "="*50 + "\n")
