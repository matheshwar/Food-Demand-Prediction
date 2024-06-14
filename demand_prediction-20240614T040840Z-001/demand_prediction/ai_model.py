# demand_prediction_model.py

import joblib

class DemandPredictor:
    def __init__(self, model_path):
        self.model = joblib.load('C:\\Users\\mones\\Downloads\\food demand prediction\\prediction.pkl')
    
    def predict_demand(self, features):
        return self.model.predict(features)
