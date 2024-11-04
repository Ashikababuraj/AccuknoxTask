from django.shortcuts import render
import logging
import time
from django.dispatch import Signal, receiver

# By default, Django signals are executed synchronously.
# when a signal is sent, the associated receivers are executed synchronously.

# Example :



logger = logging.getLogger(__name__)

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    logger.info("Receiver started")
    time.sleep(2)
    logger.info("Receiver finished")