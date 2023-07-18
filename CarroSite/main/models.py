from django.db import models

class Carro(models.Model):

    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    tipo_cor = (('PRETO','Preto'),('PRATA','Prata'), ('BRANCO','Branco'), ('VERMELHO','Vermelho'))
    cor = models.CharField(max_length=25, choices=tipo_cor, default='Preto' )
    data_compra = models.DateField(null=True)
    observacoes = models.TextField()

    def __str__(self):
        return self.modelo