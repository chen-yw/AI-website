from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('phone',)

class FortuneDateForm(forms.Form):
    BIRTH_DATE_CHOICES = [
        ('solar', '阳历'),
        ('lunar', '阴历'),
    ]
    birth_year = forms.IntegerField()
    birth_month = forms.IntegerField()
    birth_day = forms.IntegerField()
