from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('accounts/', include('accounts.urls')),
    path('notifications/', include('notifications.urls')),
    path('study/', include('study.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
