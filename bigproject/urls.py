
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login),
    path('signup', views.signup),
    path('test_token', views.test_token),
    path('user', views.user_details),
    path('upload_profile_picture', views.upload_profile_picture),
    path('profile_picture', views.get_profile_picture),
    path('update_profile_picture', views.update_profile_picture),
    path('logout', views.logout),
    path('course', views.get_courses),
    path('update_course', views.update_course),
    path('create_course', views.create_course),
]
