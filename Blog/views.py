from django.shortcuts import render
from .models import Question
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class QuestionList(ListView):
    model = Question


def question_details(request,question_id):
    data = Question.objects.get(id = question_id)
    return render(request,'Blog/question_details.html',{'question':data})


class AddQuestion(CreateView):
    model = Question
    fields = ['author','question','content','created_date','draft','tags']
    success_url = ('/question')



class UpdateQuestion(UpdateView):
    model = Question
    fields = ['author','question','content','created_date','draft','tags']
    success_url = ('/questions')
    template_name = 'Blog/edit_question.html'