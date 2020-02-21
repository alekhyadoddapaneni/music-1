from django import forms

from app.models import UploadModel
import os


class UploadForm(forms.ModelForm):
    song=forms.FileField()
    class Meta:
        model=UploadModel
        fields="__all__"
    def clean_song(self):
        song = self.cleaned_data["song"]
        bb,cc=os.path.splitext(song.name)
        # print(cc)
        print(song)
        if cc==".mp3":
            return song
        else:
            raise forms.ValidationError("up_load mp3 files only")
