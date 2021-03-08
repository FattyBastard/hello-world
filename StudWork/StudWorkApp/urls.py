from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('administrotor/', views.v_admin,   name='admin'),
    path('director/', views.v_director,     name='director'),
    path('student/', views.v_student,       name='student'),
    path('', views.switch_control,  name='switch'),

    path('student/<int:pk>/', views.v_student_edit,  name='student_edit'),
    path('director/<int:pk>/', views.v_director_list_work,  name='director_edit'),
    path('director/dir/<int:pk>/', views.v_director_edit_work,  name='dir'),
    path('administrotor/list/', views.ad_list,  name='administrator_list'),
    path('administrotor/<int:pk>/', views.ad_list_s,  name='administrator_list_s'),

    path('director/gen_tz/<int:pk>', views.gen_tz_d,  name='dir_tz'),
    path('director/gen_kp/<int:pk>', views.gen_kp_d,  name='dir_kp'),

    path('student/gen_tz/<int:pk>', views.gen_tz_s,  name='stud_tz'),
    path('student/gen_kp/<int:pk>', views.gen_kp_s,  name='stud_kp')
]
