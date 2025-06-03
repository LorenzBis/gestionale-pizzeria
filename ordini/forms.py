from django import forms
from .models import Ordine
from clienti.models import Cliente
from prodotti.models import Prodotto

class OrdineForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=13)
    prodotto = forms.ModelChoiceField(queryset=Prodotto.objects.all())
    quantita = forms.IntegerField(min_value = 1)