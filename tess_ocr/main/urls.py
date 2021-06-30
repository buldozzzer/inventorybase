from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('recognizer/', views.RecognizerView.as_view(), name='recognizer')
]
