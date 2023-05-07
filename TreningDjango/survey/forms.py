from django import forms


class SurveyForm(forms.Form):
    PYTHON_CHOICES = (enumerate(['v2', 'v3']))
    FRAMEWORK_CHOICES = (enumerate(['Tornado', 'Django', 'Flask', 'Bottle', 'Pylon']))
    name = forms.CharField(label='Imię', max_length=30, help_text='Wpisz imię wielką literą')
    birth_date = forms.DateField(label='Data urodzenia', widget=forms.SelectDateWidget(years=range(1980, 2024)))
    post_code = forms.RegexField(label='Kod pocztowy', regex='^\d{2}-\d{3}$')
    python_version = forms.CharField(label='Wersja Pythona',
                                     widget=forms.RadioSelect(choices=PYTHON_CHOICES))
    framework = forms.MultipleChoiceField(label='Framework',
                                          widget=forms.CheckboxSelectMultiple,
                                          choices=FRAMEWORK_CHOICES)
    feeling_factor = forms.IntegerField(min_value=1, max_value=10)