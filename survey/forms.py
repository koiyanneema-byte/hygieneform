from django import forms
from .models import HygieneSurvey

class HygieneSurveyForm(forms.ModelForm):
    class Meta:
        model = HygieneSurvey
        fields = ['name', 'age', 'gender', 'school', 'challenges', 'suggestions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your school'}),
            'challenges': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe any challenges you face', 'rows': 3}),
            'suggestions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any ideas or feedback?', 'rows': 3}),
        }