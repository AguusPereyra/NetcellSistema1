from django import forms
from .models import Cabania, Encargado, Cliente, Categoria, ClienteNet, Complejo, Reserva, Servicio, ReservaServicio, Proveedor, Usuario

class formUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre_usuario', 'apeynombre', 'contrasenia', 'repeat_contrasenia', 'telefono', 'email', 'dni', 'locales', 'roles')
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre de Usuario'}),
            'apeynombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre y Apellido'}),
            'contrasenia': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Contraseña'}),
            'repeat_contrasenia': forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder': 'Repita su contraseña'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Número Telefónico'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su e-mail'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI'}),
            'locales': forms.Select(attrs={'class': 'form-select'}),
            'roles': forms.Select(attrs={'class': 'form-select'})
        }

class formCabania(forms.ModelForm):
    class Meta:
        model = Cabania
        fields = ('nombre', 'tipo', 'capacidad', 'precio', 'complejo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'complejo': forms.Select(attrs={'class': 'form-select'}),
        }


class formEncargado(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = ('apellido_nombre','dni', 'telefono', 'email')
        widgets = {
            'apellido_nombre': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Nombre y Apellido'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'ingrese su DNI'} ),
            'telefono': forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Número Telefónico'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Correo Electrónico'}),
        }

class formProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('nombre_empresa', 'dni', 'telefono', 'direccion', 'comentarios')
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombre de Empresa'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Número de Documento'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una Dirección'}),
            'comentarios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un Comentario'}),
        }        

class formCategoria(forms.ModelForm):
     class Meta:
            model = Categoria
            fields = ('categoria','comentarios')
            widgets = {
                'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese una Categoria'}),
                'comentarios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un Comentario'}),
            }


class formClienteNet(forms.ModelForm):
     class Meta:
            model = ClienteNet
            fields = ('dni', 'nombre_apellido', 'telefono', 'direccion', 'comentarios', 'grupo')
            widgets = {
                'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su DNI o CUIT'}),
                'nombre_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre y Apellido'}),
                'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Direccion'}),
                'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Teléfono'}),
                'comentarios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un Comentario'}),
                'grupo': forms.Select(attrs={'class': 'form-select'}),
            }

class formCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('apellido_nombre', 'dni', 'telefono', 'email', 'pais', 'provincia', 'localidad')
        widgets = {
            'apellido_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Nombre y Apellido'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Número de Documento'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese su Correo Electrónico'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Pais de Origen'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Provincia de Origen'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Localidad de Origen'}),
        }

class formComplejo(forms.ModelForm):
    class Meta:
        model = Complejo
        fields = ('nombre', 'direccion', 'encargado')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Dirección'}),
            'encargado': forms.Select(attrs={'class': 'form-select'}),
        }
    
class formServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('nombre', 'descripcion', 'precio')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Precio'}),
        }

class formReservaServicio(forms.ModelForm):
    
    class Meta:
        model = ReservaServicio
        fields = ('reserva','servicio')
        widgets = {
            'reserva': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
        }


class formReserva(forms.ModelForm):

    cabania_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    cliente_apellido_nombre = forms.CharField(
        required=False,
        label='Cliente',
        widget=forms.TextInput(attrs={'class': 'form-control autocomplete', 'placeholder': 'Ingrese el nombre del cliente'}),
    )
    class Meta:
        model = Reserva
        fields = ('complejo', 'cabania', 'diaEntrada', 'diaSalida','seña')
        widgets = {
            'complejo': forms.Select(attrs={'class': 'form-select', 'id': 'complejo-select'}),
            'cabania': forms.Select(attrs={'class': 'form-select', 'id': 'cabania-select'}),
            'diaEntrada': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'diaSalida': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'seña': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Seña'}),
        }

    ReservaServicioFormset = forms.inlineformset_factory(Reserva, ReservaServicio, form=formReservaServicio, extra=3)
