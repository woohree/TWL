from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'galaxy/ping.html')


def pong(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    else:
        username = request.GET['username']
        password = request.GET['password']

    context = {
      'id': username,
      'password': password,
    }
    return render(request, 'galaxy/pong.html', context)


def pingpong(request):
    if request.method == 'GET':
        return render(request, 'galaxy/form.html')
    elif request.method == 'POST':
        c = request.POST['temperature']
        f = int(c)*1.8 + 32
        context = {
          'f': f,
        }
        return render(request, 'galaxy/result.html', context)