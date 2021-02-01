from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', views.TodoView)
router.register('lists', views.ListView)

urlpatterns = [
    path('', include(router.urls))
]
