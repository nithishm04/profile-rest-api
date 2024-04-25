from django.urls import path
from profile_api import views

urlpatterns = [
    path('hello-views/', views.HelloApiView.as_view()),
]
