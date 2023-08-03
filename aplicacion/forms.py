from django import forms

class ConsolaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la Consola", max_length=50, required=True)
    compania = forms.CharField(label="Nombre de la Compañia", max_length=50, required=True)
    precio = forms.IntegerField(label="Precio", required=True)

class JuegoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Juego", max_length=50, required=True)
    genero = forms.CharField(label="Genero del Juego", max_length=50, required=True)
    desarrolladora = forms.CharField(label="Desarrolladora del Juego", max_length=50, required=True)
    precio = forms.IntegerField(label="Precio", required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Cliente", max_length=50, required=True)
    apellido = forms.CharField(label="Apelldio del Cliente", max_length=50, required=True)
    email = forms.EmailField(label="Mail del Cliente", required=True)
