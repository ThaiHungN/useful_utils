"""
Help utilities for interactive documentation lookup.
"""

import inspect
import sys
from typing import Dict, List, Optional, Any
from pathlib import Path


class HelpSystem:
    """Interactive help system for useful_utils functions."""
    
    def __init__(self):
        self.functions = self._load_function_info()
    
    def _load_function_info(self) -> Dict[str, Dict[str, Any]]:
        """Load function information from the codebase."""
        functions = {}
        
        # Import all utility modules
        try:
            from .logging_utils import set_debug
            functions['set_debug'] = {
                'module': 'logging_utils',
                'function': set_debug,
                'description': 'Configure loguru logger with debug or info level',
                'category': 'Logging'
            }
        except ImportError:
            pass
        
        return functions
    
    def list_functions(self) -> List[str]:
        """Return a list of all available function names."""
        return sorted(self.functions.keys())
    
    def get_function_info(self, function_name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific function."""
        if function_name not in self.functions:
            return None
        
        func_info = self.functions[function_name]
        func = func_info['function']
        
        # Get function signature
        sig = inspect.signature(func)
        
        # Get docstring
        doc = func.__doc__ or "No documentation available."
        
        # Get source code location
        try:
            source_file = inspect.getfile(func)
            source_lines = inspect.getsourcelines(func)
            line_number = source_lines[1]
        except (OSError, TypeError):
            source_file = "Unknown"
            line_number = "Unknown"
        
        return {
            'name': function_name,
            'module': func_info['module'],
            'category': func_info['category'],
            'description': func_info['description'],
            'signature': str(sig),
            'docstring': doc,
            'source_file': source_file,
            'line_number': line_number
        }
    
    def show_function_detail(self, function_name: str) -> str:
        """Display detailed information about a function."""
        info = self.get_function_info(function_name)
        if not info:
            return f"Function '{function_name}' not found. Use help('list') to see available functions."
        
        output = []
        output.append(f"Function: {info['name']}")
        output.append(f"Category: {info['category']}")
        output.append(f"Module: {info['module']}")
        output.append(f"Location: {info['source_file']}:{info['line_number']}")
        output.append("")
        output.append(f"Signature: {info['signature']}")
        output.append("")
        output.append("Description:")
        output.append(info['description'])
        output.append("")
        output.append("Documentation:")
        output.append(info['docstring'])
        
        return "\n".join(output)
    
    def show_list(self) -> str:
        """Display a formatted list of all available functions."""
        functions = self.list_functions()
        if not functions:
            return "No functions available."
        
        output = ["Available Functions:"]
        output.append("=" * 50)
        
        # Group by category
        categories = {}
        for func_name in functions:
            info = self.get_function_info(func_name)
            if info:
                category = info['category']
                if category not in categories:
                    categories[category] = []
                categories[category].append(func_name)
        
        for category, func_names in sorted(categories.items()):
            output.append(f"\n{category}:")
            for func_name in sorted(func_names):
                info = self.get_function_info(func_name)
                if info:
                    output.append(f"  • {func_name} - {info['description']}")
        
        output.append(f"\nTotal: {len(functions)} functions")
        output.append("\nUse help('detail', 'function_name') for detailed information.")
        
        return "\n".join(output)
    
    def search_functions(self, query: str) -> List[str]:
        """Search functions by name or description."""
        query = query.lower()
        results = []
        
        for func_name in self.functions:
            info = self.get_function_info(func_name)
            if info:
                if (query in func_name.lower() or 
                    query in info['description'].lower() or
                    query in info['category'].lower()):
                    results.append(func_name)
        
        return sorted(results)


# Global help system instance
_help_system = HelpSystem()


def help(command: str = None, *args) -> str:
    """
    Interactive help system for useful_utils.
    
    Args:
        command (str): Command to execute ('list', 'detail', 'search')
        *args: Additional arguments (function name for 'detail', search query for 'search')
    
    Returns:
        str: Help information
    
    Examples:
        >>> help('list')
        >>> help('detail', 'set_debug')
        >>> help('search', 'logging')
    """
    if command is None:
        return """Help System Usage:

help('list')                    - Show all available functions
help('detail', 'function_name') - Show detailed information about a function
help('search', 'query')         - Search functions by name or description

Examples:
    help('list')
    help('detail', 'set_debug')
    help('search', 'logging')"""
    
    elif command == 'list':
        return _help_system.show_list()
    
    elif command == 'detail':
        if not args:
            return "Usage: help('detail', 'function_name')"
        function_name = args[0]
        return _help_system.show_function_detail(function_name)
    
    elif command == 'search':
        if not args:
            return "Usage: help('search', 'query')"
        query = args[0]
        results = _help_system.search_functions(query)
        if not results:
            return f"No functions found matching '{query}'"
        
        output = [f"Search results for '{query}':"]
        output.append("=" * 40)
        for func_name in results:
            info = _help_system.get_function_info(func_name)
            if info:
                output.append(f"• {func_name} - {info['description']}")
        
        return "\n".join(output)
    
    else:
        return f"Unknown command '{command}'. Use help() to see available commands."


def list_functions() -> List[str]:
    """Return a list of all available function names."""
    return _help_system.list_functions()


def get_function_info(function_name: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about a specific function."""
    return _help_system.get_function_info(function_name) 