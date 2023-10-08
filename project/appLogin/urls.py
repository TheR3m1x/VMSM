from django.urls import include, path
from . import views

# registar las rutas de la app en especifico
urlpatterns = [

    # landing page
    path('', views.redic, name="redirect"),
    path("home/", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    # resources
    path("resources/listClients/", views.listClients, name="listClients"),
    path("resources/deleteClient/<int:id>/", views.deleteClient, name="deleteClient"),
    path("resources/listProducts/", views.listProducts, name="listProducts"),
    path("resources/deleteProduct/<int:id>/", views.deleteProduct, name="deleteProduct"),
    path("resources/listStores/", views.listStores, name="listStores"),
    path("resources/deleteStore/<int:id>/", views.deleteStore, name="deleteStore"),

    # main
    path("main/home/", views.home, name="mainHome"),
    path("main/customers/", views.customers, name="customers"),
    path("main/customers/create/", views.customersCreate, name="customersCreate"),
    path("main/products/", views.products, name="products"),
    path("main/products/create/", views.productsCreate, name="productsCreate"),
    path("main/stores/", views.stores, name="stores"),
    path("main/stores/create/", views.storesCreate, name="storesCreate"),
    path("main/register/", views.register, name="register"), # nuevo registro
]
