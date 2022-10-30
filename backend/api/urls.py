from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import UserView, TagViewSet, IngredientsViewSet, RecipeViewSet

app_name = 'recipes'

router = DefaultRouter()

router.register('users', UserView, basename='users')
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
]
