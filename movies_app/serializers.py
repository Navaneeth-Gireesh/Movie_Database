from rest_framework import serializers
from . models import Movies

class MovieDetailsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None ,use_url = True)
    class Meta:
        model = Movies
        fields = ['id', 'name', 'description', 'duration', 'rating', 'genere', 'image']