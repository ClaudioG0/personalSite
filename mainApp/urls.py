from django.urls import path
from .views import index, post_detail, about_view, contact_view, projects_view, project_detail
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mainApp'

urlpatterns = [
    path('', index, name='index'),
    path('blog/<slug:post>/', post_detail, name='post_detail'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('projects/', projects_view, name='portfolio'),
    path('projects/<slug:project>/', project_detail, name='project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
