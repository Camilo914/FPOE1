from rest_framework import serializers
from api.models.celular import Celular
class CelularSerializers(serializers.ModelSerializer):
    class Meta:
        model = Celular  
        exclude = ["id"]