from django.shortcuts import render

# Create your views here.
# demand_prediction/views.py

from django.shortcuts import render


from django.shortcuts import render

from .ai_model import DemandPredictor

def predict_demand(request):
    if request.method == 'POST':
        features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine', 'city_code', 'region_code', 'category']
        features = [request.POST.get(feature) for feature in features_name]
        predictor = DemandPredictor('pretrained_model.pkl')
        prediction = round(predictor.predict_demand([features])[0])
        return render(request, 'predict_demand.html' ,{'prediction': prediction})
    else:
        return render(request, 'predict_demand.html')
    
