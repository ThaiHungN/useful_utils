"""
Example usage of the logging utilities.
"""

import sys
import os

# Add the parent directory to the path so we can import from utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.logging_utils import set_debug
from loguru import logger


def main():
    """Demonstrate the logging utility functionality."""
    
    print("=== Logging Utility Example ===\n")
    
    # Example 1: Enable debug mode
    print("1. Enabling debug mode:")
    set_debug(debug_mode=True)
    
    # Now all log levels will be shown
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Disable debug mode (info level and above only)
    print("2. Disabling debug mode:")
    set_debug(debug_mode=False)
    
    # Now only INFO level and above will be shown
    logger.debug("This debug message will NOT be shown")
    logger.info("This info message WILL be shown")
    logger.warning("This warning message WILL be shown")
    logger.error("This error message WILL be shown")
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: Practical usage in a function
    print("3. Practical usage in a function:")
    set_debug(debug_mode=True)
    
    def process_data(data):
        logger.debug(f"Processing data: {data}")
        if len(data) > 10:
            logger.warning("Data is quite large")
        result = data.upper()
        logger.info(f"Processed result: {result}")
        return result
    
    process_data("hello world")
    process_data("this is a very long string that will trigger a warning")


if __name__ == "__main__":
    main() 