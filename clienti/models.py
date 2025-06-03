from django.db import models

# Creo il modello Cliente

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.EmailField()
    indirizzo = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
