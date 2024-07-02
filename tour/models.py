from django.db import models

# Create your models here.
class Equip(models.Model):
    nom = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    any_creacio = models.IntegerField(default=0)

    def __str__(self):
        return self.nom
    
class Ciclista(models.Model):    
    nom = models.CharField(max_length=100)
    edat = models.IntegerField()
    pais = models.CharField(max_length=50)
    equip = models.ForeignKey(Equip, related_name='ciclistes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    
class Etapa(models.Model):
    
    primer = models.ForeignKey(Ciclista,on_delete=models.CASCADE,
                    related_name="primer_lloc")
    segon = models.ForeignKey(Ciclista,on_delete=models.CASCADE,
                    related_name="segon_lloc")
    tercer = models.ForeignKey(Ciclista,on_delete=models.CASCADE,
                    related_name="tercer_lloc")
    ciutat_origen = models.CharField(max_length=100)
    ciutat_arribada = models.CharField(max_length=100)
    def primer(self):
        return self.primer
    def segon(self):
        return self.segon
    def tercer(self):
        return self.tercer
    
    