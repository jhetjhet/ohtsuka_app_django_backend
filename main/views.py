from rest_framework import viewsets
from django.http import Http404
from .models import (
    Tboperatorlist,
    OptDbseikeimdrcrossout,
)
from .serializers import (
    TboperatorlistSerializer,
    OptDbseikeimdrcrossoutSerializer,
)

class TboperatorlistViewsets (viewsets.ModelViewSet):
    serializer_class = TboperatorlistSerializer
    queryset = Tboperatorlist.objects.all()
    lookup_field = 'id'

    def get_object(self):
        res = self.get_queryset().filter(**self.kwargs).first()
        if not res:
            raise Http404()
        return res

class OptDbseikeimdrcrossoutViewsets (viewsets.ModelViewSet):
    serializer_class = OptDbseikeimdrcrossoutSerializer
    queryset = OptDbseikeimdrcrossout.objects.all()
    lookup_field = 'ctlno'