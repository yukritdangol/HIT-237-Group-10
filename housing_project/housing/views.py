from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Housing


class HousingListView(LoginRequiredMixin, ListView):

    model = Housing

    template_name = 'housing_list.html'

    login_url = 'login'

    def get_queryset(self):

        return Housing.objects.filter(
            is_available=True
        ).order_by('price')