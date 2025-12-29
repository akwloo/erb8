from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', include('pages.urls',namespace='pages')),
    path('listings/', include('listings.urls',namespace='listings')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()

admin.site.site_header = "Clinic Administration"
admin.site.site_title = "Clinic Admin Portal"
admin.site.index_title = "Welcome to Clinic Portal"