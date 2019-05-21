import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('description/<int:pk>', mainapp.description, name='description')
]
