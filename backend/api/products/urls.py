from django.conf.urls import url
from django.urls import path, include
from .views import (
    ProductsView,
)

urlpatterns = [
    path('', ProductsView.as_view()),
]
