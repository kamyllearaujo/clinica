from django.contrib import admin
from .models import Clinica, Medico, Paciente, Agendamento
 
# Registrando os modelos no Django Admin
admin.site.register(Clinica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Agendamento)

# Register your models here.
