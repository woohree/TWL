from django.shortcuts import render

# Create your views here.

def dinner(request, menu, number):
    context = {
      'dinner_menu': menu,
      'number': number,
    }
    return render(request, 'pages/dinner.html', context)


def check(request):
    return render(request, 'pages/home.html')