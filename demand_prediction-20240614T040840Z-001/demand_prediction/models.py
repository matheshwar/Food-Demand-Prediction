from django.db import models

# Create your models here.
# demand_prediction/models.py

# demand_prediction/models.py

from django.db import models

class DemandPredictionInput(models.Model):
    homepage_featured = models.BooleanField()
    emailer_for_promotion = models.BooleanField()
    op_area = models.FloatField()
    cuisine = models.CharField(max_length=255)
    city_code = models.IntegerField()
    region_code = models.IntegerField()
    category = models.CharField(max_length=255)

    class Meta:
        app_label = 'demand_prediction'
