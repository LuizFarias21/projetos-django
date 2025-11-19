from django.contrib import admin
from .models import Filme
from rest_framework.authtoken.models import Token

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
   list_display = ['titulo', 'diretor', 'ano', 'genero', 'duracao']
   search_fields = ['titulo', 'diretor', 'ano', 'genero', 'duracao']
   list_filter = ['ano', 'diretor', 'genero', 'duracao'] #Não coloquei titulo pois acredito que não faz mto sentido

admin.site.register(Token)