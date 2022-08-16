from rest_framework import routers
from .views import (
    CrossoutOperatorViewsets,
)

router = routers.SimpleRouter()
router.register(r'crossout_ops', CrossoutOperatorViewsets)

urlpatterns = router.urls