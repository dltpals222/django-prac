from django import forms
from .models import mytable


class MytableForm(forms.ModelForm):
    class Meta:
        model = mytable
        fields = ["name", "number", "nickname", "deposit", "score"]
