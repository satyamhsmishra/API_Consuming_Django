from django.contrib import admin
from django.urls import path
from consume.views import save_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consume/',save_data,name='consume'),
]
