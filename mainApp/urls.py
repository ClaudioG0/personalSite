from django.urls import path
from .views import index, post_detail, about_view, contact_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('<slug:post>/', post_detail, name='post_detail'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
