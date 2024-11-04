from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def class_temp(request):
    return render(request, 'second_task/class_template.html')


def func_temp(request):
    return render(request, 'second_task/func_template.html')
