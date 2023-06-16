from django.urls import path
from . import views
from .views import IndexView, ShortenURLView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shorten/', ShortenURLView.as_view(), name='shorten'),
]