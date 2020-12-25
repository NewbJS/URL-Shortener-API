from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.make_short, name='create'),
    path('<slug:short_url>/', views.get_long, name="get-long")
]