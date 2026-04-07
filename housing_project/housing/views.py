from django.views.generic import ListView
from .models import Housing

class HousingListView(ListView):
    model = Housing
    template_name = 'housing_list.html'

    def get_queryset(self):
        return Housing.objects.all()