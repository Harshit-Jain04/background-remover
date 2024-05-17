# myapi/urls.py

from django.urls import path
from api.views import ProcessImageView
import api.views

urlpatterns = [
    path('cartoon', ProcessImageView.as_view(), name='cartoon'),
    

]
