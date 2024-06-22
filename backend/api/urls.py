from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("view-product/<str:pk>/", views.view_product, name="view-product"),
    path("get-tracked-products/", views.get_tracked_products_home, name="get-tracked-products-home"),

    # TESTING STUFF BELOW
    path("get-foo/", views.get_foo, name="get-foo"),
    path("create-foo/", views.create_foo, name="create-foo"),
]