from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset')



urlpatterns = [
    path('hello-views/', views.HelloApiView.as_view()),
    path('',include(router.urls))
]
