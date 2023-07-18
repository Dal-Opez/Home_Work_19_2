from django.contrib import admin
from django.urls import path
from catalog_app.views import home, contacts

from catalog_app.apps import CatalogAppConfig
from catalog_app.views import home, contacts, product

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts),
    path('product/', product, name='product'),
]