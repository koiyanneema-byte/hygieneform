from django import forms

class HygieneSurveyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    school = forms.CharField(max_length=150)
    challenges = forms.CharField(widget=forms.Textarea, label="Menstrual Hygiene Challenges")
    suggestions = forms.CharField(widget=forms.Textarea, required=False, label="Suggestions or Feedback")