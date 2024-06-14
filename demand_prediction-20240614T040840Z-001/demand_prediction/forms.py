# demand_prediction/forms.py

from django import forms
from .models import DemandPredictionInput
class DemandPredictionForm(forms.ModelForm):
    class Meta:
        model = DemandPredictionInput
        fields = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine', 'city_code', 'region_code', 'category']
