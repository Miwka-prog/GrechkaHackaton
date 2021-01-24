from django.urls import path

from . import views

app_name = 'GrechkaApp'
urlpatterns = [
    path('', views.get_settings, name='index'),
    # path('count_field/<int:n>/', views.get_name, name='count_field'),
]
