from rest_framework import viewsets
from .models import (
    CrossoutOperator,
)
from .serializers import (
    CrossoutOperatorSerializer,
)

class CrossoutOperatorViewsets (viewsets.ModelViewSet):
    serializer_class = CrossoutOperatorSerializer
    queryset = CrossoutOperator.objects.all()
    lookup_field = 'crossout'