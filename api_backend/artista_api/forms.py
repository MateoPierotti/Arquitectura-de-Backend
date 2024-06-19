from django import forms

from artista_api.models import Cancion, Artista

# def validate_number(value):
#     if not isinstance(value, int):
#         raise ValidationError("El numero debe ser un número entero.")
#     if value > -1:
#         raise ValidationError("El año de aparición debe tener exactamente 4 dígitos.")



class ArtistaForm(forms.ModelForm):

    class Meta:
        model = Artista
        fields = [
            'name',
            'fecha_nacimiento',
        ]


class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = [
            'Nombre',
            'artista',
            'fechaDeLanzamiento',
            'reproducciones',
        ]


