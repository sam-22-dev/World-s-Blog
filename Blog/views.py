from django.shortcuts import render
from .models import Question


def question_list(request):
    data = Question.objects.all()
    return render(request,'question_list.html',{'questions':data})


def question_details(request,question_id):
    data = Question.objects.get(id = question_id)
    return render(request,'question_details.html',{'question':data})