from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # all myapi-app urls will have prefix api/
    path("api/", include("myapi.urls"))
]
