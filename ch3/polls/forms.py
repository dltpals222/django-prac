from django import forms
from .models import PracTable


class PracTableForm(forms.ModelForm):
    class Meta:
        model = PracTable
        fields = ["name", "number", "nickname", "deposit", "score"]
