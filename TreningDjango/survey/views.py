from django.shortcuts import render, HttpResponse
from .forms import SurveyForm


def send_survey(request):
    cd = None
    if request.method == 'GET':
        form = SurveyForm()
    else:
        form = SurveyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    return render(request, 'survey/survey.html', {'form':form, 'data':cd})


# def send_survey(request):
#     cd = None
#     form = SurveyForm(request.POST or None)
#     if form.is_valid():
#         cd = form.cleaned_data
#     return render(request, 'survey/survey.html', {'form':form, 'data':cd})