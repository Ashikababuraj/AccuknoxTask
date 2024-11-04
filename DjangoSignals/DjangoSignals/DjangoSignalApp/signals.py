from django.shortcuts import render
import logging
import time
from django.dispatch import Signal, receiver

import threading
from .models import SignalModel

# Question 1 Answer
# By default, Django signals are executed synchronously.
# when a signal is sent, the associated receivers are executed synchronously.


# Question 2 Answer
# Yes, Django signals run in the same thread as the caller.
# when we send a signal, the connected receiver functions are
# executed synchronously in the same thread

# Example showing, when a signal is sent with a threadId... the receiver
# executes the same thread with that threadId.

# Question 3 Answer
# By default, Django signals do not run in the same database
# transaction as the caller. Instead, they execute after the transaction of
# the caller has been committed.

# Example :



logger = logging.getLogger(__name__)

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    logger.info("Receiver started")
    time.sleep(2)
    logger.info("Receiver finished")


@receiver(my_signal)
def my_thread_receiver(sender, **kwargs):
    current_thread = threading.get_ident()  # Get current thread ID
    logger.info(f"Receiver started in thread: {current_thread}")
    time.sleep(2)  # Simulate some processing time
    logger.info(f"Receiver finished in thread: {current_thread}")


@receiver(my_signal)
def create_my_model(sender, **kwargs):
    logger.info("Creating MyModel instance after transaction.")
    SignalModel.objects.create(name="Signal created instance")