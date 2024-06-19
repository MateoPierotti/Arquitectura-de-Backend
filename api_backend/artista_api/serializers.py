from rest_framework import serializers

from artista_api.models import Cancion, Artista

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista

        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'



