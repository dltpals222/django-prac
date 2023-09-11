from django import forms
from .models import pracTable


class PracTableForm(forms.ModelForm):
    class Meta:
        model = PracTable
        fields = ["name", "number", "nickname", "deposit", "score"]
