from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']  # Поля формы
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'username': 'Имя пользователя'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
