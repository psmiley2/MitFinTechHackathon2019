from home.api.views import QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', QuestionViewSet, base_name='questions')
urlpatterns=router.urls
