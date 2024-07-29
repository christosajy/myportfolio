from django.urls import path
from frontend import views

urlpatterns = [
    path('home/', views.f_index, name='f_index'),
    path('contact/', views.contact_mail, name='contact_mail'),
]