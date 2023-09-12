from django import forms
from .models import mytable


class MytableForm(forms.ModelForm):
    class Meta:
        model = mytable
        fields = ["name", "number", "nickname", "deposit", "score"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "width-15percent"}),
            "number": forms.TextInput(attrs={"class": "width-10percent"}),
            "nickname": forms.TextInput(attrs={"class": "width-20percent"}),
            "deposit": forms.TextInput(attrs={"class": "width-35percent"}),
            "score": forms.TextInput(attrs={"class": "width-20percent"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        if not all(cleaned_data.values()):
            raise forms.ValidationError("5군데 모두 입력해 주시기 바랍니다.")
