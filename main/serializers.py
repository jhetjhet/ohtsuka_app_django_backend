from rest_framework import serializers
from .models import (
    Tboperatorlist,
    OptDbseikeimdrcrossout,
)

class TboperatorlistSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Tboperatorlist
        fields = '__all__'

class OptDbseikeimdrcrossoutSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = OptDbseikeimdrcrossout
        fields = '__all__'