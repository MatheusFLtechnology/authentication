from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurante(models.Model):
    plates = models.CharField(max_length=100)
    description= models.TextField()
    prices= models.FloatField()
    begin_date= models.DateTimeField(auto_now_add=True)
    photo= models.ImageField(upload_to='restaurante')
    active= models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'restaurant'    


