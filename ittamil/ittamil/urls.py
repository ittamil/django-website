from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ittamilapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ittamilapp.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("like/", views.LikeView, name="like_post"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
