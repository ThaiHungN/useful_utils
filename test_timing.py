#!/usr/bin/env python3

from useful_utils import log_time, timeit, set_debug
from loguru import logger
import time

# Enable debug mode
set_debug(debug_mode=True)

# Test log_time
print("Testing log_time:")
with log_time("Simple test"):
    print("Hello world")
    time.sleep(0.1)

# Test timeit decorator
@timeit("Test function")
def test_function():
    time.sleep(0.1)
    return "Function completed"

print("\nTesting timeit decorator:")
result = test_function()
print(f"Result: {result}") 