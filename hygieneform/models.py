from django import forms

class HygieneSurveyForm(forms.Form):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
        ('prefer_not', 'Prefer not to say'),
    ]

    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Your Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    school = forms.CharField(label="School Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    challenges = forms.CharField(label="Menstrual Hygiene Challenges", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    suggestions = forms.CharField(label="Suggestions or Feedback", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))