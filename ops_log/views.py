from rest_framework import viewsets
from django.http import Http404
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

    def get_object(self):
        res = self.get_queryset().filter(**self.kwargs).first()
        if not res:
            raise Http404()
        return res