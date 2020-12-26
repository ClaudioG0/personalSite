from django.urls import path
from .views import search_view

app_name = "searchApp"

urlpatterns = [
    path('search/', search_view, name='search')
]
