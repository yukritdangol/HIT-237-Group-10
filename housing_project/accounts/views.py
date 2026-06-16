from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required
from .models import UserProfile



def signup_view(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            UserProfile.objects.create(
                user=user,
                community_name='Unknown',
                contact_number='Not Provided'
            )

            login(request, user)

            return redirect('dashboard')

    else:

        form = UserCreationForm()

    return render(
        request,
        'registration/signup.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('dashboard')

    else:

        form = AuthenticationForm()

    return render(
        request,
        'registration/login.html',
        {
            'form': form
        }
    )


def logout_view(request):

    logout(request)

    return redirect('login')



@login_required
def dashboard_view(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'community_name': 'Darwin',
            'contact_number': '0000000000',
        }
    )

    return render(
        request,
        'dashboard.html',
        {
            'profile': profile
        }
    )