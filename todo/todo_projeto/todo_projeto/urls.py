
from django.contrib import admin
from django.urls import path, include
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('',include('todo_app.urls'))
]
