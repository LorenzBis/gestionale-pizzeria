from django.db import models

# Creo il modello Prodotto

class Prodotto(models.Model):
    nome = models.CharField(max_length=100)
    prezzo = models.DecimalField(max_digits=6, decimal_places=2)
    descrizione = models.TextField(blank=True)
    immagine = models.ImageField(upload_to='prodotti/', blank=True, null=True)

    def __str__(self):
        return self.nome