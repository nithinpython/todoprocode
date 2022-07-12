from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update')
]
