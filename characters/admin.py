from django.contrib import admin
from characters.models import *

# Register your models here.
class RaceAdmin (admin.ModelAdmin):
    ...

class OriginAdmin (admin.ModelAdmin):
    ...

class FaithAdmin (admin.ModelAdmin):
    ...

class ClasseAdmin (admin.ModelAdmin):
    ...

class CharacterAdmin (admin.ModelAdmin):
    ...

admin.site.register(Race, RaceAdmin)
admin.site.register(Origin, OriginAdmin)
admin.site.register(Faith, FaithAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Character, CharacterAdmin)
