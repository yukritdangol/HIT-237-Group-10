from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .models import Housing, Location

from accounts.models import UserProfile

from housing.services.housing_service import HousingService

from .exceptions import (
    InvalidHousingPriceError,
    UnauthorizedActionError
)


class HousingListView(LoginRequiredMixin, ListView):

    model = Housing

    template_name = 'housing_list.html'

    login_url = 'login'


    def get_queryset(self):

        return HousingService.get_available_housing()


@login_required
def create_housing_view(request):

    profile = request.user.userprofile

    if profile.role != 'MANAGER':

        raise UnauthorizedActionError(
            "Only managers can create housing listings."
        )

    if request.method == 'POST':

        title = request.POST.get('title')

        location_id = request.POST.get('location')

        price = int(request.POST.get('price'))

        description = request.POST.get('description')

        location = Location.objects.get(
            id=location_id
        )

        try:

            HousingService.create_housing(
                title,
                location,
                price,
                description
            )

            return redirect('/')

        except InvalidHousingPriceError as error:

            return render(
                request,
                'create_housing.html',
                {
                    'error': str(error),
                    'locations': Location.objects.all()
                }
            )

    return render(
        request,
        'create_housing.html',
        {
            'locations': Location.objects.all()
        }
    )