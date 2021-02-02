from django.forms import ModelForm
from app.models import Cars

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['indice', 'Modelo','Marca','Ano','Inclusao','Placa','Chassi','CLRV']






