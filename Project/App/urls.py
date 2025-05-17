from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/',views.admin, name='admin'),
    path('events/', views.events, name='events'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course-details/', views.details, name='course-details'),
    # path('index/<int:id>/', views.download_file, name='index'),
]