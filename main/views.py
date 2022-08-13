from rest_framework import viewsets
from .models import (
    Tboperatorlist,
    OptItemmastermain,
    OptDbseikeimdrcrossout,
)
from .serializers import (
    TboperatorlistSerializer,
    OptItemmastermainSerializer,
    OptDbseikeimdrcrossoutSerializer,
)

class TboperatorlistViewsets (viewsets.ModelViewSet):
    serializer_class = TboperatorlistSerializer
    queryset = Tboperatorlist.objects.all()
    lookup_field = 'id'

class OptItemmastermainViewsets (viewsets.ModelViewSet):
    serializer_class = OptItemmastermainSerializer
    queryset = OptItemmastermain.objects.all()

class OptDbseikeimdrcrossoutViewsets (viewsets.ModelViewSet):
    serializer_class = OptDbseikeimdrcrossoutSerializer
    queryset = OptDbseikeimdrcrossout.objects.all()
    lookup_field = 'ctlno'