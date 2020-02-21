from django import forms

from app.models import UploadModel


class UploadForm(forms.ModelForm):
    song=forms.FileField()
    class Meta:
        model=UploadModel
        fields="__all__"