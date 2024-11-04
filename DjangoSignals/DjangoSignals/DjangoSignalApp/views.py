from django.shortcuts import render
from django.http import HttpResponse
from .signals import my_signal
import time


def my_view(request):
    print("Sending signal")
    my_signal.send(sender=None)
    print("Signal sent")
    return HttpResponse("Signal sent and receiver executed.")
