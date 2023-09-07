from django.contrib import admin
from .models import Profil #, #AutreModele1, AutreModele2

# Classe d'administration pour le modèle Profil
class ProfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'adresse_ville', 'numero_telephone']  # Configurez les champs à afficher dans la liste des objets

# Classe d'administration pour les autres modèles
#class AutreModele1Admin(admin.ModelAdmin):
    # Configurez les options d'administration pour AutreModele1

#class AutreModele2Admin(admin.ModelAdmin):
    # Configurez les options d'administration pour AutreModele2

# Enregistrez les classes d'administration
admin.site.register(Profil, ProfilAdmin)
    #admin.site.register(AutreModele1, AutreModele1Admin)
    #Eadmin.site.register(AutreModele2, AutreModele2Admin)
