"""
Example usage of the timing utilities.
"""

import sys
import os
import time

# Add the parent directory to the path so we can import from useful_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from useful_utils import log_time, timeit, help, set_debug
from loguru import logger


def simulate_work(duration=1.0):
    """Simulate some work for testing timing."""
    time.sleep(duration)


@timeit("Heavy computation")
def heavy_computation():
    """Example function that takes time to complete."""
    simulate_work(0.5)
    return "Computation completed"


def main():
    """Demonstrate the timing utility functionality."""
    
    print("=== Timing Utility Example ===\n")
    
    # Enable debug mode to see all log levels
    set_debug(debug_mode=True)
    
    # Show available functions
    print("1. Available functions:")
    print(help('list'))
    
    print("\n" + "="*60 + "\n")
    
    # Example 1: Using log_time context manager
    print("2. Using log_time context manager:")
    with log_time("Data processing"):
        simulate_work(0.3)
        logger.info("Processing data...")
        simulate_work(0.2)
    
    print("\n" + "="*60 + "\n")
    
    # Example 2: Using timeit decorator
    print("3. Using timeit decorator:")
    result = heavy_computation()
    print(f"Result: {result}")
    
    print("\n" + "="*60 + "\n")
    
    # Example 3: Nested timing
    print("4. Nested timing:")
    with log_time("Outer operation"):
        with log_time("Inner operation 1"):
            simulate_work(0.1)
        
        with log_time("Inner operation 2"):
            simulate_work(0.2)
    
    print("\n" + "="*60 + "\n")
    
    # Example 4: Function details
    print("5. Function details:")
    print(help('detail', 'log_time'))
    
    print("\n" + "="*60 + "\n")
    
    # Example 5: Search for timing functions
    print("6. Search for timing functions:")
    print(help('search', 'timing'))


if __name__ == "__main__":
    main() 