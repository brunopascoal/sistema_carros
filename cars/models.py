from django.db import models
from django.conf import settings


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # funcao que retorna o modelo ou brand ou o que desejar na interface do admin
    def __str__(self):
        return self.name


# classe car é o nome da tabela do BD
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=10)
    value = models.FloatField()
    photo = models.ImageField(upload_to="cars/")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_cars")


    # funcao que retorna o modelo ou brand ou o que desejar na interface do admin
    def __str__(self):
        return self.model
