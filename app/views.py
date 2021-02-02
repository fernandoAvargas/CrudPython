from django.shortcuts import render
from app.forms import CarsForm


# Create your views here.

def home(request): return render(request,'index.html')

<<<<<<< HEAD
def form(request):
    data = {}
    data['form'] = CarsForm()
    return render(request,'form.html',data)
=======
def form(request): return render(request,'form.html')
>>>>>>> b8a4d6fcba5384635e19cecd76ab02542a6788ec
