from django.urls import path
from . import views

urlpatterns = [
    path('test-signal/', views.my_view, name='test_signal'),
    path('send-thread-signal/', views.my_thread_view, name='send_thread_signal'),
    path('create-instance/', views.signal_model_view, name='create_instance'),
]