from django import forms

from .models import Question, Answer



class QuestionForm(forms.ModelForm):
    """
    Allow to post question
    """
    class Meta:
        model = Question
        fields = ['title']

class AnswerForm(forms.ModelForm):
    """
    Allow to post answer
    """
    class Meta:
        model = Answer
        fields = ['text']
