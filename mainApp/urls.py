from django.urls import path
from mainApp import views
from mainApp.views import {
	registration_view,
	login_view
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
]
