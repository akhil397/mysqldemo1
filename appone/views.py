from django.shortcuts import render
from .models import VideoData

# Create your views here.
def index(request):
    demos = VideoData.objects.all()
    return render(request,'index.html',{'demos':demos})