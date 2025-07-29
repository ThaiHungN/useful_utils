# Contributing to Useful Utils

Welcome! This library thrives on community contributions. Everyone is welcome to add useful functions that can help others.

## Quick Start

1. **Fork the repository**
2. **Add your function** following the format below
3. **Test your function**
4. **Submit a pull request**

## How to Add a New Function

### Step 1: Create Your Function Module

Create a new file in the `utils/` directory following this naming convention:
- Use descriptive names: `file_utils.py`, `data_utils.py`, `web_utils.py`
- Use lowercase with underscores
- Keep related functions together

**Example:** `utils/file_utils.py`
```python
"""
File utilities for common file operations.
"""

import os
from pathlib import Path
from typing import List, Optional


def safe_read_file(file_path: str, encoding: str = 'utf-8') -> Optional[str]:
    """
    Safely read a file with error handling.
    
    Args:
        file_path (str): Path to the file to read
        encoding (str): File encoding (default: 'utf-8')
    
    Returns:
        Optional[str]: File contents or None if error
    
    Example:
        >>> content = safe_read_file('config.txt')
        >>> if content:
        ...     print("File read successfully")
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"Error reading file: {e}")
        return None
```

### Step 2: Update the Help System

Add your function to `utils/help_utils.py` in the `_load_function_info` method:

```python
def _load_function_info(self) -> Dict[str, Dict[str, Any]]:
    """Load function information from the codebase."""
    functions = {}
    
    # Existing functions...
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
    
    # Add your new function
    try:
        from .file_utils import safe_read_file
        functions['safe_read_file'] = {
            'module': 'file_utils',
            'function': safe_read_file,
            'description': 'Safely read a file with error handling',
            'category': 'File Operations'
        }
    except ImportError:
        pass
    
    return functions
```

### Step 3: Update Package Exports

Add your function to `utils/__init__.py`:

```python
# Import main utilities
from .logging_utils import set_debug
from .file_utils import safe_read_file  # Add this line
from .help_utils import help, list_functions, get_function_info

# Make functions available at package level
__all__ = [
    'set_debug',
    'safe_read_file',  # Add this line
    'help',
    'list_functions', 
    'get_function_info'
]
```

### Step 4: Update Documentation

#### Update `docs/functions.md`:
```markdown
## File Utilities (`utils/file_utils.py`)

### `safe_read_file(file_path, encoding='utf-8')`

Safely read a file with error handling.

**Parameters:**
- `file_path` (str): Path to the file to read
- `encoding` (str): File encoding (default: 'utf-8')

**Returns:** Optional[str] - File contents or None if error

**Example:**
```python
from utils import safe_read_file

content = safe_read_file('config.txt')
if content:
    print("File read successfully")
```

**Features:**
- Error handling for common file issues
- Configurable encoding
- Safe return values
```

#### Update `docs/examples.md`:
```markdown
## File Operation Examples

### Safe File Reading

```python
from utils import safe_read_file

# Read a file safely
content = safe_read_file('config.json')
if content:
    print("File loaded successfully")
else:
    print("Could not read file")
```
```

### Step 5: Create an Example

Create `examples/file_example.py`:
```python
"""
Example usage of file utilities.
"""

import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import safe_read_file, help


def main():
    """Demonstrate file utility functionality."""
    
    print("=== File Utility Example ===\n")
    
    # Show help
    print("1. Available functions:")
    print(help('list'))
    
    print("\n2. Function details:")
    print(help('detail', 'safe_read_file'))
    
    print("\n3. Testing file reading:")
    # Create a test file
    with open('test.txt', 'w') as f:
        f.write("Hello, this is a test file!")
    
    content = safe_read_file('test.txt')
    print(f"File content: {content}")
    
    # Clean up
    os.remove('test.txt')


if __name__ == "__main__":
    main()
```

### Step 6: Update Requirements (if needed)

If your function needs new dependencies, add them to `requirements.txt`:
```txt
loguru>=0.7.0
requests>=2.25.0  # Add new dependencies here
```

## Function Guidelines

### ✅ Good Function Examples

```python
def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def format_duration(seconds: int) -> str:
    """Convert seconds to human-readable duration."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def chunk_list(lst: list, size: int) -> List[List]:
    """Split a list into chunks of specified size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]
```

### ❌ Avoid These

- Functions that are too specific to one project
- Functions that duplicate standard library functionality
- Functions without proper error handling
- Functions without documentation

### 📝 Documentation Standards

1. **Docstring format:**
   ```python
   def function_name(param1: type, param2: type = default) -> return_type:
       """
       Brief description of what the function does.
       
       Args:
           param1 (type): Description of parameter
           param2 (type): Description of parameter
       
       Returns:
           return_type: Description of return value
       
       Example:
           >>> function_name("example")
           "result"
       
       Raises:
           ValueError: When something goes wrong
       """
   ```

2. **Include examples** in docstrings
3. **Add type hints** for all parameters and return values
4. **Handle errors gracefully**
5. **Keep functions focused** on one specific task

## Testing Your Function

```bash
# Test the help system
python -c "from utils import help; print(help('list'))"

# Run your example
python examples/file_example.py

# Test import
python -c "from utils import your_function; print('Import successful')"
```

## Pull Request Process

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b add-file-utils`
3. **Make your changes** following the format above
4. **Test everything works**
5. **Commit with clear messages:**
   ```bash
   git add .
   git commit -m "Add file utilities with safe_read_file function"
   ```
6. **Push to your fork**
7. **Create a pull request** with:
   - Clear description of what you added
   - Example usage
   - Any new dependencies

## Categories for Functions

Use these categories when adding functions:
- **File Operations** - File reading, writing, manipulation
- **Data Processing** - Data validation, transformation, analysis
- **Web Utilities** - HTTP requests, URL parsing, web scraping
- **Text Processing** - String manipulation, text analysis
- **System Utilities** - OS operations, process management
- **Math & Statistics** - Calculations, statistical functions
- **Date & Time** - Date manipulation, time formatting
- **Logging** - Logging utilities (already exists)
- **Other** - Miscellaneous utilities

## Need Help?

- Check existing functions for examples
- Use the built-in help system: `help('list')`
- Look at the documentation in `docs/`
- Ask questions in issues or discussions

## Thank You!

Every contribution makes this library more useful for everyone. Thank you for helping build a better utility collection! 🚀 