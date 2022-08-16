from rest_framework import routers
from .views import (
    TboperatorlistViewsets,
    TbfarminsubconstocksViewsets,
    # OptItemmastermainViewsets,
    OptDbseikeimdrcrossoutViewsets,
)

router = routers.SimpleRouter()
router.register(r'operators', TboperatorlistViewsets)
router.register(r'subcons', TbfarminsubconstocksViewsets)
router.register(r'crossout', OptDbseikeimdrcrossoutViewsets)

urlpatterns = router.urls