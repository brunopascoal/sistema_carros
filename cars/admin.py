from django.contrib import admin
from cars.models import Car, Brand

# Pra aparecer a tabela no admin, preciso registrar aqui


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year", "model_year", "value")
    search_fields = ("model", "brand", "factory_year", "model_year", "value")


# funcao pra aparecer la no admin, parametro do model criado e das funcoes de admin desse model
admin.site.register(Car, CarAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Brand, BrandAdmin)
