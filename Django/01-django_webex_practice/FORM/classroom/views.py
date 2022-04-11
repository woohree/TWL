from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from .forms import StudentForm


# Create your views here.
@require_safe
def index(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'classroom/index.html', context)


@require_safe
def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
      'student': student,
    }
    return render(request, 'classroom/detail.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('classroom:detail', student.pk)
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'classroom/form.html', context)


# 겟, 포스트 둘 다 받음
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('classroom:detail', student.pk)
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'classroom/form.html', context)


# 포스트요청만 받음
@require_POST
def delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('classroom:index')
