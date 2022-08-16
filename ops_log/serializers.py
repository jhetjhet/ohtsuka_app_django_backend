from rest_framework import serializers
from .models import (
    CrossoutOperator,
)

class CrossoutOperatorSerializer (serializers.ModelSerializer):

    class Meta:
        model = CrossoutOperator
        fields = '__all__'