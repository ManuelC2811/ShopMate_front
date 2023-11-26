from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importa el modelo User

# Reordering Form and View

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico")

    class Meta:
        model = User  # Asegúrate de importar el modelo User
        fields = ['username', 'email', 'password1', 'password2']


class PositionForm(forms.Form):
    position = forms.CharField()