from django.urls import path

from .views import (
    HousingListView,
    create_housing_view,
)

urlpatterns = [

    path(
        '',
        HousingListView.as_view(),
        name='housing_list'
    ),

    path(
        'create/',
        create_housing_view,
        name='create_housing'
    ),
]