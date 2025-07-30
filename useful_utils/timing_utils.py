"""
Timing utilities for performance monitoring and logging.
"""

import time
from contextlib import contextmanager
from functools import wraps
from loguru import logger


@contextmanager
def log_time(label="⏱️ Code block"):
    """
    Context manager for timing a block of code and logging the time.

    Args:
        label (str): Label to display in the log message

    Usage:
        with log_time("Loading data"):
            # Your code here
            load_data()
    """
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        logger.info(f"{label} completed in {elapsed:.2f} seconds")


def timeit(label="⏱️ Function"):
    """
    Decorator version of log_time for timing functions.

    Args:
        label (str): Label to display in the log message

    Usage:
        @timeit("Training model")
        def train():
            # Your function code here
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with log_time(label):
                return func(*args, **kwargs)
        return wrapper
    return decorator 