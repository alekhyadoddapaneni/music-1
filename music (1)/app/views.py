from django.contrib import messages
from django.db.models import Q

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from app.forms import UploadForm
from app.models import UploadModel


class MusicHome(View):
    def get(self,request):
        return render(request,"MusicHome.html")


class UploadSongs(View):
    def get(self,request):
        return render(request,"upload.html",{"data":UploadForm()})
    def post(self,request):
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully uploaded")
            return redirect("upload")
        else:
            messages.error(request, "valid files uploaded")
            return render(request, "upload.html", {"data":form })


class Viewsongs(View):
    def get(self,request):
        all=UploadModel.objects.all()
        return render(request,"viewallsongs.html",{"alls":all})



class DeleteSongs(View):
    def get(self,request):
        all = UploadModel.objects.all()
        return render(request, "deletesongs.html", {"alls": all})
    def post(self,request):
        d=request.POST.getlist("t1")
        for x in d:
            r=UploadModel.objects.filter(song=x)
            r.delete()
        all = UploadModel.objects.all()
        return render(request, "deletesongs.html", {"alls": all})


class SearchSong(View):
    def post(self,request):
        sr=request.POST.get("search")
        sng=UploadModel.objects.filter(Q(moviename=sr)|Q(song=sr))
        # sng=UploadModel.objects.filter(moviename=sr)or UploadModel.objects.filter(song=sr)
        return render(request,"searchsongs.html",{"songs":sng})


class PlaySong(View):
    def get(self,request):
        y=request.GET.get("t1")
        return render(request,"playsong.html",y)
    pass