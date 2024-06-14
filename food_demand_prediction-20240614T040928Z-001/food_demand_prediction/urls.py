from django.contrib import admin
from django.urls import path, include
from demand_prediction.views import predict_demand

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demand_prediction/', include('demand_prediction.urls')),
    path('', predict_demand, name='home'),
]
