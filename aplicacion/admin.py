from django.contrib import admin
from .models import Artista

# Register your models here.
class AdmArtistas(admin.ModelAdmin):
    pass


admin.site.register(Artista)