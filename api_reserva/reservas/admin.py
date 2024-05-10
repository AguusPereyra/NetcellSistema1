from django.contrib import admin
from .models import Cliente, Encargado, Usuario, Complejo, Cabania, Reserva, Servicio, ReservaServicio, ClienteNet, Proveedor, Categoria, Articulo

# Register your models here.

#-------NETCELL-----------------------

admin.site.register(ClienteNet)

admin.site.register(Proveedor)

admin.site.register(Categoria)

admin.site.register(Articulo)

admin.site.register(Usuario)

#-------RESERVAS-----------------------

admin.site.register(Cliente)

admin.site.register(Encargado)

admin.site.register(Complejo)

admin.site.register(Cabania)

admin.site.register(Reserva)

admin.site.register(Servicio)

admin.site.register(ReservaServicio)