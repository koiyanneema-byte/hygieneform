from django import forms

class HygieneSurveyForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    age = forms.IntegerField(
        label="Your Age",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'})
    )
    school = forms.CharField(
        max_length=150,
        label="School Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your school'})
    )
    challenges = forms.CharField(
        label="Menstrual Hygiene Challenges",
        widget=forms.Textarea(attrs={'placeholder': 'Describe any challenges you face'})
    )
    suggestions = forms.CharField(
        required=False,
        label="Suggestions or Feedback",
        widget=forms.Textarea(attrs={'placeholder': 'Any ideas or feedback?'})
    )