from django.urls import path
from . import views

urlpatterns = [
    path('test-signal/', views.my_view, name='test_signal'),
]