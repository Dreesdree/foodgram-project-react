from django.contrib import admin

from recipes.models import (
    ShoppingCart, FavoriteRecipe, Ingredient, IngredientsAmount, Recipe, Tag,
)


class Admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class RecipeAdmin(Admin):
    list_display = ('name', 'author', 'times_favorited')
    list_filter = ('name', 'author', 'tags')

    def times_favorited(self, object):
        return object.favorite.count()


class IngredientAdmin(Admin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('^name',)

class TagAdmin(Admin):
    list_display = ('name',)
    list_filter = ('name', 'color', 'slug')

class ShoppingCartAdmin(Admin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)

class IngredientAmountAdmin(Admin):
    list_display = ('name', 'amount')
    list_filter = ('name',)

class FavoriteRecipeAdmin(Admin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(IngredientsAmount, IngredientAmountAdmin)
admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)