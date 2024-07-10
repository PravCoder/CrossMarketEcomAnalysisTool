from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("get-product/<str:pk>/", views.get_product, name="get-product"),
    path("view-product/<str:pk>/", views.view_product, name="view-product"),
    
    path("get-product-cross-products/<str:pk>/", views.get_product_cross_products, name="get-product-cross-products"),

    path("get-tracked-products/", views.get_tracked_products_home, name="get-tracked-products-home"),

    # TESTING STUFF BELOW
    path("get-foo/", views.get_foo, name="get-foo"),
    path("create-foo/", views.create_foo, name="create-foo"),
]