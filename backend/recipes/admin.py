from django.contrib import admin

from recipes.models import (FavoriteRecipe, Ingredient, IngredientAmount,
                            Cart, Recipe, Tag)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('measurement_unit',)
    search_fields = ('^name',)


class IngredientAmountAdmin(admin.TabularInline):
    model = IngredientAmount
    fk_name = 'recipe'


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'times_favorited')
    list_filter = ('tags',)
    search_fields = ('name', 'author__username', 'author__email')
    exclude = ('ingredients',)

    inlines = [
        IngredientAmountAdmin,
    ]

    def times_favorited(self, object):
        favorited = FavoriteRecipe.objects.filter(recipe=object).count()
        return favorited


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('recipe__tags',)
    search_fields = ('user__username', 'recipe__name')


class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('recipe__tags',)
    search_fields = ('user__username', 'recipe__name')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    search_fields = ('ingredient__name', 'recipe__author__username')
    list_filter = ('recipe__tags',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
admin.site.register(IngredientAmount, RecipeIngredientAdmin)
