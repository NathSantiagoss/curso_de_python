from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=255)
    apto = models.CharField(max_length=100)
    telefone = models.IntegerField()
    email = models.EmailField()
    data = models.DateField(null=True)
    assunto = models.CharField(null=True, max_length=255)
    descripiton = models.TextField(null=True)

    def __str__(self):
        return (f'{self.assunto} - {self.nome} - {self.apto}')
