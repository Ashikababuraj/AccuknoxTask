from django.shortcuts import render
from django.http import HttpResponse
from .signals import my_signal
# import time
import threading
import logging
from .models import SignalModel


logger = logging.getLogger(__name__)

def my_view(request):
    print("Sending signal")
    my_signal.send(sender=None)
    print("Signal sent")
    return HttpResponse("Signal sent and receiver executed.")


def my_thread_view(request):
    current_thread = threading.get_ident()
    logger.info(f"Sending signal from thread: {current_thread}")
    my_signal.send(sender=None)
    return HttpResponse("Signal sent, check console for thread info.")

def signal_model_view(request):
    instance = SignalModel.objects.create(name="Original instance")
    logger.info(f"Created instance: {instance}")

    my_signal.send(sender=SignalModel)

    return HttpResponse("Instance created, and signal sent. Check the database.")