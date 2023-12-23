from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index.courses"),
    path('course/<int:id>',course,name='courses.show'),
    path('course-register/<int:id>',regest,name='register.course'),
    path('succes/<int:id>',success,name='course.success')
]
