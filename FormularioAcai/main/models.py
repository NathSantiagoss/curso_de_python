from django.db import models

class Sorvete(models.Model):
    sabor_creme_tipo = (
        ('A', 'Açaí'), ('C', 'Cupuaçu')
    )
    sabor = models.CharField(
        max_length=1, choices=sabor_creme_tipo, 
        default = 'A'
    )

    sabor_cobertura = (
        ('Cho', 'Chocolate'), ('Mor','Morango'),
        ('Car','Caramelo'),('leC','Leite Condesado')
    )
    cobertura = models.CharField(
        max_length=3, 
        choices=sabor_cobertura,
        default='leC'
    )
    
    tipo_tamanho = (
        ('PEQ','Pequeno'),
        ('MED','Médio'),
        ('GRD','Grande'),
        ('BRC','Barca')
    )
    
    tamanho = models.CharField(
        max_length=3,
        choices=tipo_tamanho,
        default='MED'
    )
    
    def __str__(self):
        return self.sabor
