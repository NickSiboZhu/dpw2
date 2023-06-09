from django.urls import path
from . import views

app_name = 'minisearch'

urlpatterns = [
    path('', views.search_index, name='search_view'),
    path('results/', views.search_results, name='search_results'),
    path('news/', views.news, name='news')
]
