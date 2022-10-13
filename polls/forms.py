from dataclasses import fields
from django import forms

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'