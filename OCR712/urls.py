from django.urls import path
from . import views

urlpatterns = [path('',views.model_form_upload,name="model_form_upload"),
                path('down',views.downForm, name="down"),
                path(r'^download/(?P<file_path>.*)/$', views.download, name='file_download'),]