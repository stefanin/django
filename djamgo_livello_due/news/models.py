from django.db import models

# Create your models here.
class Giornalista(models.Model):
    """  Giornalista """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome +" "+ self.cognome

class Articolo(models.Model):
    """  Articolo """
    titolo = models.CharField(max_length=100) # campo char è necessario definirne la lunghezza
    contenuto = models.TextField() # campo text field
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articolo") # crea una relazione uno a molti
                                                                           # on_delete=models.CASCADE gestisce la relazione in caso di delete
                                                                           # related_name nome della relazione

    def __str__(self):
        return self.titolo
