from django.shortcuts import render
from .forms import HygieneSurveyForm

def survey_view(request):
    if request.method == 'POST':
        form = HygieneSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = HygieneSurveyForm()
    return render(request, 'survey.html', {'form': form})