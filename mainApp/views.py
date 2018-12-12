from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Employee
from mainApp.form import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
from django import forms
from django.urls import reverse
 

# получение данных из бд
def index(request):
    people = Employee.objects.all()
    return render(request, "mainApp/index.html", {"people": people})

 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Employee()
        person.name = request.POST.get("name")
        person.position = request.POST.get("position")
        person.date_employment = request.POST.get("date_employment")
        person.wage = request.POST.get("wage")
        person.save()
    return HttpResponseRedirect("/")

# изменение данных в бд
def edit(request, id):
    try:
        person = Employee.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.position = request.POST.get("position")
            person.date_employment = request.POST.get("date_employment")
            person.wage = request.POST.get("wage")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "mainApp/edit.html", {"person": person})
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Сотрудник не найден</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Employee.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Сотрудник не найден</h2>")

#регистрация пользователя
def registration_view(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')

        new_user.username = username
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    context = { 'form': form }
    return render(request, 'mainApp/registration.html', context)

#авторизация (логин) пользователя
def  login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'mainApp/login.html', context)

def add_view(request):
    return render(request, "mainApp/add.html")