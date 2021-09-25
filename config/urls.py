from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user', include('api.user.urls')),
    path('api/board', include('api.board.urls')),
]
