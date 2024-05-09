
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.main, name='main'),

    path('usuarios/', views.lista_usuarios.as_view(), name='lista_usuarios'),
    path('usuarios/usuarioNuevo', views.nuevo_usuario, name='nuevo_usuario'),
    path('usuarios/usuarioModif/<int:pk>/', views.modif_usuario.as_view(), name='modif_usuario'),
    path('usuarios/usuarioBorrar/<int:pk>/', views.borrar_usuario.as_view(), name='borrar_usuario'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),

#-----PROYECTO NETCELL--------------------------------------------------------

    path('clientesNet/', views.lista_clientesNet.as_view(), name='lista_clientesNet'),
    path('clientesNet/<int:clienteNet_id>/', views.detalle_clienteNet, name='detalle_clienteNet'),
    path('clientesNet/clienteNetNuevo/', views.nuevo_clienteNet.as_view(), name='nuevo_clienteNet'),
    path('clientesNet/clienteNetModif/<int:pk>/', views.modif_clienteNet.as_view(), name='modif_clienteNet'),
    path('clientesNet/clienteNetBorrar/<int:pk>/', views.borrar_clienteNet.as_view(), name='borrar_clienteNet'),    

    path('proveedores/', views.lista_proveedores.as_view(), name='lista_proveedores'),
    path('proveedores/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/proveedorNuevo/', views.nuevo_proveedor.as_view(), name='nuevo_proveedor'),
    path('proveedores/proveedorModif/<int:pk>/', views.modif_proveedor.as_view(), name='modif_proveedor'),
    path('proveedores/proveedorBorrar/<int:pk>/', views.borrar_proveedor.as_view(), name='borrar_proveedor'),

    path('categoria/', views.lista_categoria.as_view(), name='lista_categoria'),
    path('categoria/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/categoriaNuevo/', views.nuevo_categoria.as_view(), name='nuevo_categoria'),
    path('categoria/categoriaModif/<int:pk>/', views.modif_categoria.as_view(), name='modif_categoria'),
    path('categoria/categoriaBorrar/<int:pk>/', views.borrar_categoria.as_view(), name='borrar_categoria'),

#-----PROYECTO RESERVAS--------------------------------------------------------

    path('encargados/', views.lista_encargados.as_view(), name='lista_encargados'),
    path('encargados/<int:encargado_id>/', views.detalle_encargado, name='detalle_encargado'),
    path('encargados/encargadoNuevo/', views.nuevo_encargado.as_view(), name='nuevo_encargado'),
    path('encargados/encargadoModif/<int:pk>/', views.modif_encargado.as_view(), name='modif_encargado'),
    path('encargados/encargadoBorrar/<int:pk>/', views.borrar_encargado.as_view(), name='borrar_encargado'),    

    path('clientes/', views.lista_clientes.as_view(), name='lista_clientes'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/clienteNuevo/', views.nuevo_cliente.as_view(), name='nuevo_cliente'),
    path('clientes/clienteModif/<int:pk>/', views.modif_cliente.as_view(), name='modif_cliente'),
    path('clientes/clienteBorrar/<int:pk>/', views.borrar_cliente.as_view(), name='borrar_cliente'),

    path('cabanias/', views.lista_cabanias.as_view(), name='lista_cabanias'),
    path('cabanias/<int:cabania_id>/', views.detalle_cabania, name='detalle_cabania'),
    path('cabanias/cabaniaNuevo/', views.nuevo_cabania.as_view(), name='nuevo_cabania'),
    path('cabanias/cabaniaModif/<int:pk>/', views.modif_cabania.as_view(), name='modif_cabania'),
    path('cabanias/cabaniaBorrar/<int:pk>/', views.borrar_cabania.as_view(), name='borrar_cabania'),

    path('complejos/', views.lista_complejos.as_view(), name='lista_complejos'),
    path('complejos/<int:complejo_id>/', views.detalle_complejo, name='detalle_complejo'),
    path('complejos/complejoNuevo/', views.nuevo_complejo.as_view(), name='nuevo_complejo'),
    path('complejos/complejoModif/<int:pk>/', views.modif_complejo.as_view(), name='modif_complejo'),
    path('complejos/complejoBorrar/<int:pk>/', views.borrar_complejo.as_view(), name='borrar_complejo'),

    path('servicios/', views.lista_servicios.as_view(), name='lista_servicios'),
    path('servicios/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicios/servicioNuevo/', views.nuevo_servicio.as_view(), name='nuevo_servicio'),
    path('servicios/servicioModif/<int:pk>/', views.modif_servicio.as_view(), name='modif_servicio'),
    path('servicios/servicioBorrar/<int:pk>/', views.borrar_servicio.as_view(), name='borrar_servicio'),

    path('reservas/', views.lista_reservas.as_view(), name='lista_reservas'),
    path('reservas/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/reservaNuevo/', views.nuevo_reserva.as_view(), name='nuevo_reserva'),
    path('reservas/reservaModif/<int:pk>/', views.modif_reserva.as_view(), name='modif_reserva'),
    path('reservas/reservaBorrar/<int:pk>/', views.borrar_reserva.as_view(), name='borrar_reserva'),

    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.Logout, name='logout'),

    path('reservas/reservas/<int:reserva_id>/factura/', views.factura, name='factura'),

    path('search_clients/', views.search_clients, name='search_clients'),

    path('cabanias/disponibilidad/<int:cabania_id>/', views.disponibilidad_cabania, name='disponibilidad-cabania'),
    path('complejo/disponibilidad/<int:complejo_id>/', views.disponibilidad_complejo, name='disponibilidad-complejo'),
    path('cabanias_disponibles/', views.cabanias_disponibles, name='cabanias_disponibles'),
    path('obtener_cabanias/<int:complejo_id>/', views.obtener_cabanias, name='obtener_cabanias'),

]
