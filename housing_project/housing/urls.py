from django.urls import path
from .views import HousingListView

urlpatterns = [
    path('', HousingListView.as_view(), name='housing_list'),
]