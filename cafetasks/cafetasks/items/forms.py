from django import forms
from cafetasks.items.models import Item


class ItemCreateForm(forms.ModelForm):
    name = forms.CharField(label="Название")
    description = forms.CharField(label="Описание", widget=forms.Textarea())
    cost = forms.IntegerField(label="Цена")

    class Meta:
        model = Item
        fields = ["name", "description", "cost"]
