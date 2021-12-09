from django.conf.urls import url
from django.urls import path, include
from .views import (
    PersonView,
)

urlpatterns = [
    path('', PersonView.as_view()),
]
