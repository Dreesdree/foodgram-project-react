from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from api.views import (
    ShoppingCartViewSet, FavoriteViewSet, FollowerViewSet, IngredientViewSet,
    RecipeViewSet, TagViewSet, UserViewSet
)

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)
router.register('ingredients', IngredientViewSet)
router.register(
    r'recipes/(?P<recipe_id>\d+)/shopping_cart',
    ShoppingCartViewSet,
    basename='carts'
)
router.register(
    r'recipes/(?P<recipe_id>\d+)/favorite',
    FavoriteViewSet,
    basename='favorites'
)
router.register(
    r'users/(?P<user_id>\d+)/subscribe',
    FollowerViewSet,
    basename='carts'
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)