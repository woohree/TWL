from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as lin, logout as lout, get_user_model
from .forms import SignupForm


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('articles:article_index')
        else:
            form = SignupForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    return redirect('articles:article_index')


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                lin(request, user)
                return redirect(request.GET.get('next') or 'articles:article_index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    return redirect('articles:article_index')


def logout(request):
    lout(request)
    return redirect('articles:article_index')


def profile(request, username):
    user1 = get_object_or_404(get_user_model(), username=username)
    is_follow = user1.followers.filter(username=request.user.username).exists()
    context = {
        'user1': user1,
        'is_follow': is_follow,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, username):
    user1 = get_object_or_404(get_user_model(), username=username)
    if user1.followers.filter(username=request.user.username).exists():
        user1.followers.remove(request.user)
    else:
        user1.followers.add(request.user)
    return redirect('accounts:profile', user1.username)
