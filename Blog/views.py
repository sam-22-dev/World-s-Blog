from django.shortcuts import render
from .models import Question,Answer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AnswerForm


class QuestionList(ListView):
    model = Question


def question_details(request,question_id):
    data = Question.objects.get(id = question_id)
    question_answers = Answer.objects.filter(question=data)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.question = data
            myform.save()
    else:
        form = AnswerForm()
    return render(request,'Blog/question_details.html',{'question':data, 'answers':question_answers, 'form':form})


class AddQuestion(CreateView):
    model = Question
    fields = ['author','question','content','created_date','draft','tags']
    success_url = ('/questions')



class UpdateQuestion(UpdateView):
    model = Question
    fields = ['author','question','content','created_date','draft','tags']
    success_url = ('/questions')
    template_name = 'Blog/edit_question.html'


class DeleteQuestion(DeleteView):
    model = Question
    success_url = ('/questions')