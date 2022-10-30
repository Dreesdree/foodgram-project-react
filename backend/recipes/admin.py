from django.contrib import admin

from recipes.models import (FavoriteRecipe, Ingredient, IngredientAmount,
                            Cart, Recipe, Tag)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('^name',)


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'amount')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'times_favorited')
    list_filter = ('author', 'name', 'tags')

    def times_favorited(self, object):
        favorited = FavoriteRecipe.objects.filter(recipe=object).count()
        return favorited


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
