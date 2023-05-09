from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_comma_separated_integer_list, validate_email

def validate_first_letter_upper(value):
    if len(value) and value[0].islower():
        raise ValidationError('Musi się zaczynać od wielkiej litery')

def validate_div_3(value):
    if value % 3 != 0:
        raise ValidationError('Musi być podzielne przez 3')

def validate_ends_with_a(value):
    if not value.endswith('a'):
        raise ValidationError('Musi kończyś się na "a"')

def validate_march_month(value):
    if value.month != 3:
        raise ValidationError('Tylko dozwolony marzec')

class EmailAddresses(forms.Field):
    def to_python(self, value):
        # Konwertuj value pola na konkretny typ pythona, tutaj listę adresów e-mail
        if not value:
            return []
        return [x.strip() for x in value.split(',')]

    def validate(self, value):
        # Dla każdego maila z listy, wykonaj funkcje walidacyjna
        # Niczego nie zwracaj z tej funkcji
        for email in value:
            validate_email(email)

    def clean(self, value):
        value = super().clean(value)
        # to_python oraz validate zostały wywołane przez super().clean(value) z klasy bazowej
        # także wykonano run_validators(), która uruchamia wszystkie funkcje walidacyjne na liście validators=[] w formularzu
        value = [v.lower() for v in value]
        return value

class SurveyForm(forms.Form):
    PYTHON_CHOICES = (enumerate(['v2', 'v3']))
    FRAMEWORK_CHOICES = (enumerate(['Tornado', 'Django', 'Flask', 'Bottle', 'Pylon']))
    name = forms.CharField(label='Imię', max_length=30, help_text='Wpisz imię wielką literą',
                           validators=[validate_first_letter_upper, validate_ends_with_a])
    birth_date = forms.DateField(label='Data urodzenia', widget=forms.SelectDateWidget(years=range(1980, 2024)),
                                 validators=[validate_march_month])
    post_code = forms.RegexField(label='Kod pocztowy', regex='^\d{2}-\d{3}$')
    emails = EmailAddresses(label='Adresy e-mail')
    lucky_number = forms.CharField(label='Ulubione liczby', initial='1,2',
                                   validators=[validate_comma_separated_integer_list])
    python_version = forms.CharField(label='Wersja Pythona',
                                     widget=forms.RadioSelect(choices=PYTHON_CHOICES))
    framework = forms.MultipleChoiceField(label='Framework',
                                          widget=forms.CheckboxSelectMultiple,
                                          choices=FRAMEWORK_CHOICES)
    feeling_factor = forms.IntegerField(min_value=1, max_value=10, validators=[validate_div_3])

    def clean_name(self):
        value = self.cleaned_data['name']
        map = {
            'ą': 'a', 'ć': 'c', 'ę': 'e', 'ó': 'o', 'ś': 's', 'ż': 'z', 'ź': 'z', 'ń': 'n', 'ł': 'l',
            'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ó': 'O', 'Ś': 'S', 'Ż': 'Z', 'Ź': 'Z', 'Ń': 'N', 'Ł': 'L'
        }
        for letter in map.keys():
            value = value.replace(letter, map[letter])
        return value

    def clean(self):
        data = super().clean()
        name = data.get('name')
        emails = data.get('emails')
        if name and emails:
            if not any([name.lower() in email for email in emails]):
                raise ValidationError('Imię nie jest zawarte w żadnym adresie e-mail')
        return data
