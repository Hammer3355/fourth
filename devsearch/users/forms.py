from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']  # Поля формы
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'username': 'Имя пользователя', 'password1': 'Пароль','password2': 'Повторите пароль'}
