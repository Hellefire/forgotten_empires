from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login

from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST, request=request)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    next_page = request.GET.get('next', None) or '/'
    return render(
        request, 'user_login.html', context={'next': next_page, 'form': form})


@login_required
def home_page(request):
    if request.user.is_staff:
        return render(request, 'gm_home.html')
    else:
        return render(request, 'player_home.html')


def terms_page(request):
    return render(request, 'terms.html')


@login_required
def logout(request):
    return logout_then_login(request)
