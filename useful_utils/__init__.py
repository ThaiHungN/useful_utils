"""
Useful Utils - A collection of reusable code snippets and utilities.
"""

__version__ = "1.0.0"
__author__ = "Hung Nguyen"

# Import main utilities
from .logging_utils import set_debug
from .help_utils import help, list_functions, get_function_info

# Make functions available at package level
__all__ = [
    'set_debug',
    'help',
    'list_functions', 
    'get_function_info'
] 