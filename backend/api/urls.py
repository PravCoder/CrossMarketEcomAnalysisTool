from django.urls import path
from . import views

urlpatterns = [

    
    path("", views.home, name="home"),
    path("view-product/<str:pk>/", views.home, name="home"),

    # TESTING STUFF BELOW
    path("get-foo/", views.get_foo, name="get-foo"),
    path("create-foo/", views.create_foo, name="create-foo"),
]