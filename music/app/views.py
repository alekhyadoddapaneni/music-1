from django.contrib import messages
from django.db.models import Q
from .models import UploadModel

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from app.forms import UploadForm



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
            messages.error(request, "only mp3 files can access")
            return render(request, "upload.html",{"data":form })


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
        song=UploadModel.objects.filter(Q(moviename=sr)|Q(song=sr))
        # sng=UploadModel.objects.filter(moviename=sr)or UploadModel.objects.filter(song=sr)
        return render(request,"searchsongs.html",{"songs":song})


class PlaySong(View):
    def get(self,request):
        y=request.GET.get("n")
        return render(request,"playsong.html",{"song":y})



class SearchSongs(View):
    def get(self,request):
        return render(request,"opensearchpage.html")
