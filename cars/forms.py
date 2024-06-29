from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        exclude = ('created_by',)  # Exclui o campo created_by do formulário

        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factory_year': 'Ano de Fabricação',
            'model_year': 'Ano do Modelo',
            'plate': 'Placa',
            'value': 'Valor',
            'photo': 'Foto',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 20000:
            self.add_error("value", "Valor mínimo do carro deve ser R$ 20.000")
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 1975:
            self.add_error(
                "factory_year",
                "Não é possível cadastrar carros fabricados antes de 1975",
            )
        return factory_year

    def save(self, commit=True):
        car = super().save(commit=False)
        if self.request:
            car.created_by = self.request.user  # Atribui o usuário logado como criador do carro
        if commit:
            car.save()
        return car