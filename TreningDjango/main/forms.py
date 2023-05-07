from django import forms


class PythonistForm(forms.Form):
    name = forms.CharField(label='Imię', max_length=30, help_text='Wpisz imię wielką literą')
    birth_date = forms.DateField(label='Data urodzenia', widget=forms.SelectDateWidget(years=range(1980, 2024)))
    email = forms.EmailField(label='E-mail', initial='mail@domena.pl', required=False)