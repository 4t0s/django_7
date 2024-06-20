from django.contrib import admin
from django.urls import path
from app.views import list_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_todo),
]
