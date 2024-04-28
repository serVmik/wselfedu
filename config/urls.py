import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dotenv import load_dotenv

from config import views

load_dotenv()

admin_url = os.getenv('ADMIN_URL')

urlpatterns = [
    path(admin_url, admin.site.urls),
    path(
        '',
        views.HomeView.as_view(), name='home'),
    path(
        'math-home/',
        views.MathHomeView.as_view(),
        name='math_home',
    ),
    path('users/', include('users.urls')),
    path('task/', include('task.urls')),
    path('english/', include('english.urls')),
    path('notion/', include('notion.urls')),
]

if (
        os.getenv('ENVIRONMENT') != 'PRODUCTION'
        and os.getenv('DEBUG_TOOLBAR') == 'True'
):
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
