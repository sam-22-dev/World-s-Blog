from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Question (models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='Question_User')
    question = models.CharField(max_length=300)
    content = models.TextField(max_length=3000)
    created_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    tags = TaggableManager()

    def __str__(self):
        return self.question



class Answer (models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answer_author')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answer_question')
    answer = models.TextField(max_length=5000)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.author)
