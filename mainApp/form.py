from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(label="Ваш логин")
	password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

	# Валидация входа проходит в этом методе по логину и паролю
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not User.objects.filter(username=username).exists():
		    raise forms.ValidationError('Пользователь с данным логином не зарегистрирован в системе')
		user = User.objects.get(username=username)
		if user and not user.check_password(password):
			raise forms.ValidationError('Неверный пароль')


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'password_check', 'first_name', 'last_name', 'email']

	username = forms.CharField(label="Ваш логин")
	password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
	password_check = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")
	first_name = forms.CharField(label="Имя")
	last_name = forms.CharField(label="Фамилия")
	email = forms.EmailField(label="Ваша почта")

	# Валидация проходит в этом методе
	def clean(self):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		if User.objects.filter(username=username).exists():
		    raise forms.ValidationError('Пользователь с данным логином уже зарегистрирован в системе')
		if self.cleaned_data.get('password') != self.cleaned_data.get('password_check'):
			raise forms.ValidationError('Пароли должны совпадать!')
		if User.objects.filter(email=email).exists():
		    raise forms.ValidationError('Данная почта уже зарегистрирована в системе')
		return self.cleaned_data