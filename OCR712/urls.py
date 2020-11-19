from django.urls import path
from . import views

urlpatterns = [path('',views.model_form_upload,name="model_form_upload"),
                path('down',views.downForm, name="down"),
                path('down/excel', views.download_file)]