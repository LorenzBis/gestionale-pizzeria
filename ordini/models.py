from django.db import models
from clienti.models import Cliente
from prodotti.models import Prodotto 

# creo il modello Ordine

class Ordine(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.PositiveIntegerField()
    data_ordine = models.DateTimeField(auto_now_add=True)
    stato = models.CharField(max_length=50, choices=[
        ('in attesa', 'In Attesa'),
        ('completato', 'Completato'),
        ('annullato', 'Annullato'),
    ], default='in_attesa')

    def __str__(self):
        return f"{self.cliente.nome} - {self.prodotto.nome} - ({self.quantita})"

