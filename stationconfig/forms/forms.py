# coding:utf-8

from django import forms
from stationconfig.models.models import SelectManager

class SelectManager(forms.ModelForm):
    class Meta:
        model = SelectManager
        fields = '__all__'