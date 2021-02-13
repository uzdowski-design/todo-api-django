from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()            # create router to manage routes
router.register('tasks', views.TaskView)    # set up /tasks route for tasks
router.register('lists', views.ListView)  # set up /lists route for lists


# enforce all routes set up in router
urlpatterns = [
    path('', include(router.urls))
]
