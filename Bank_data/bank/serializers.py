from rest_framework.serializers import ModelSerializer
from .models import Details

class Detailserializer(ModelSerializer):
    class Meta:
        model=Details
        fields='__all__'