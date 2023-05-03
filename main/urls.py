from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register'),
    path("patient/<int:pk>", views.patient_record, name='patient'),
    path("delete/<int:pk>", views.delete_patient, name='delete_patient'),
    path("add/", views.add_patient, name='add_patient'),
    path("edit/<int:pk>", views.edit_patient, name='edit_patient'),
]
