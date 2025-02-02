from django import forms
from cafetasks.statuses.models import Status


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
        labels = {"name": "Название"}
