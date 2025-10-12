from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from utils.characters.constants import *

# Create your models here.
class Race (models.Model):
    name = models.CharField(max_length=65)
    size = models.CharField(max_length=2, choices=SIZES_CHOICES, default='MD')

    def __str__(self):
        return self.name
    

class Origin (models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Faith (models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Classe (models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Character (models.Model):
    name = models.CharField(max_length=65)
    level = models.IntegerField()
    att_str = models.IntegerField (default=0)
    att_dex = models.IntegerField (default=0)
    att_con = models.IntegerField (default=0)
    att_int = models.IntegerField (default=0)
    att_sab = models.IntegerField (default=0)
    att_char = models.IntegerField (default=0)
    hit_points = models.IntegerField()
    mana_points = models.IntegerField()
    armor_class = models.IntegerField()
    speed = models.DecimalField(max_digits=6, decimal_places=1)
    background = models.TextField()
    #Fixed choices
    size = models.CharField(max_length=2, choices=SIZES_CHOICES)
    role = models.CharField(max_length=3, choices=ROLES_CHOICES)
    picture = models.ImageField(upload_to='characters/pictures/%Y/%m/%d' )
    #ForeignKeys
    player = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE
    )
    origin = models.ForeignKey(
        Origin, on_delete=models.CASCADE
    )
    faith = models.ForeignKey(
        Faith, on_delete=models.SET_NULL, null=True
    )
    #MUDAR FUTURAMENTE PARA MANY TO MANY
    classes = models.ForeignKey(
        Classe, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name