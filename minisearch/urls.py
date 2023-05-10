from django.urls import path
from . import views

app_name = 'minisearch'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('minisearch', views.search_index, name = 'search_view'),
    path('login/', views.login, name='login'),
]
