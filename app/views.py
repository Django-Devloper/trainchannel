from django.shortcuts import render
from .models import TrainDetails ,CHOOSE_STATUS
from django.forms import ModelForm

class ArticleForm(ModelForm):
  class Meta:
      model = TrainDetails
      fields = ['status']


# Create your views here

def index(request):
    trains=TrainDetails.objects.all()
    form = ArticleForm()
    return render(request,'index.html',{'trains':trains,'choose':form})