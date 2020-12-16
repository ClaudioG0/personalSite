from django.urls import path
from .views import index, post_detail


urlpatterns = [
    path('', index, name='index'),
    path('<slug:post>/', post_detail, name='post_detail')
]
