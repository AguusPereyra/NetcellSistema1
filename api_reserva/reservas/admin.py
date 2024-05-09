from django.contrib import admin
from .models import Cliente, Encargado, Complejo, Cabania, Reserva, Servicio, ReservaServicio, ClienteNet, Proveedor, Categoria

# Register your models here.

admin.site.register(Cliente)

admin.site.register(ClienteNet)

admin.site.register(Proveedor)

admin.site.register(Categoria)

admin.site.register(Encargado)

admin.site.register(Complejo)

admin.site.register(Cabania)

admin.site.register(Reserva)

admin.site.register(Servicio)

admin.site.register(ReservaServicio)