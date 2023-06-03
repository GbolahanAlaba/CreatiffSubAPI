from django.urls import path
from . import views

urlpatterns = [
    path('api/subscribers/', views.Subscribers, name='Subscribe'),
    path('api/subscribers/<int:id>/', views.SubscribeDetail, name='SubscribeDetail'),

]