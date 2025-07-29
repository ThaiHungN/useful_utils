"""
Example usage of the help system.
"""

import sys
import os

# Add the parent directory to the path so we can import from utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from useful_utils import help, list_functions


def main():
    """Demonstrate the help system functionality."""
    
    print("=== Help System Example ===\n")
    
    # Example 1: List all available functions
    print("1. Listing all available functions:")
    print(help('list'))
    
    print("\n" + "="*60 + "\n")
    
    # Example 2: Get detailed information about a function
    print("2. Getting detailed information about 'set_debug':")
    print(help('detail', 'set_debug'))
    
    print("\n" + "="*60 + "\n")
    
    # Example 3: Search for functions
    print("3. Searching for functions containing 'debug':")
    print(help('search', 'debug'))
    
    print("\n" + "="*60 + "\n")
    
    # Example 4: Search for functions containing 'logging':")
    print("4. Searching for functions containing 'logging':")
    print(help('search', 'logging'))
    
    print("\n" + "="*60 + "\n")
    
    # Example 5: Show help usage
    print("5. Help system usage:")
    print(help())
    
    print("\n" + "="*60 + "\n")
    
    # Example 6: Using list_functions() directly
    print("6. Using list_functions() directly:")
    functions = list_functions()
    print(f"Available functions: {functions}")


if __name__ == "__main__":
    main() 