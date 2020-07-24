from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import ArticleView
from article.views import ArticleViewSet

app_name = "articles"

router = DefaultRouter()
# router.register(r'articles', ArticleView, basename='user')
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls
