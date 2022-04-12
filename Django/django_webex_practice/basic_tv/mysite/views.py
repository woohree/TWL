from django.http import HttpResponse  # HTML을 응답으로 주는 함수
from django.shortcuts import render   # 그냥 데이터를 응답으로 주는 함수
import random
import datetime


# Create your views here.
def home(request):
    return render(request, 'mysite/home.html')


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'mysite/greeting.html', context)


def lunch(request):
    a = datetime.datetime.today()
    menus = ['고추잡채', '쟘봉', '닭가슴살 샐러드', '리코타 치즈 피자', '까르보나라', '고봉밥']
    context = {
        'today_menu': random.sample(menus, 2),
        'menus': menus,
        'sentence': 'happy happy happpppyyyyy lunch!',
        'today': a,
    }
    return render(request, 'mysite/lunch.html', context)


def lotto(request):
  lucky_numbers = random.sample(range(1, 46), 6)
  context = {
      'lucky_numbers': lucky_numbers,
  }
  return render(request, 'mysite/lotto.html', context)

