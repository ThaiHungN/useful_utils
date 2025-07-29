"""
Logging utilities for consistent logging across projects.
"""

from loguru import logger


def set_debug(debug_mode=True):
    """
    Configure loguru logger with debug or info level.
    
    Args:
        debug_mode (bool): If True, shows DEBUG level messages. If False, shows INFO level and above.
    
    Example:
        >>> set_debug(debug_mode=True)
        🟢 Debug mode ON
        
        >>> set_debug(debug_mode=False)
        🔴 Debug mode OFF
    """
    logger.remove()
    if debug_mode:
        logger.add(lambda msg: print(msg, end=""), level="DEBUG")
        logger.debug("🟢 Debug mode ON")
    else:
        logger.add(lambda msg: print(msg, end=""), level="INFO")
        logger.debug("�� Debug mode OFF") 