from rest_framework import routers
from .views import (
    TboperatorlistViewsets,
    OptItemmastermainViewsets,
    OptDbseikeimdrcrossoutViewsets,
)

router = routers.SimpleRouter()
router.register(r'operators', TboperatorlistViewsets)
router.register(r'crossout', OptDbseikeimdrcrossoutViewsets)

urlpatterns = router.urls