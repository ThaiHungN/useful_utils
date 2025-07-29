# Available Functions

Complete reference of all utilities in the library.

## Help System (`utils/help_utils.py`)

### `help(command=None, *args)`

Interactive help system for useful_utils functions.

**Parameters:**
- `command` (str, optional): Command to execute ('list', 'detail', 'search')
- `*args`: Additional arguments (function name for 'detail', search query for 'search')

**Returns:** str - Help information

**Examples:**
```python
from useful_utils import help

# Show help usage
help()

# List all available functions
help('list')

# Get detailed information about a function
help('detail', 'set_debug')

# Search for functions
help('search', 'logging')
```

### `list_functions()`

Return a list of all available function names.

**Returns:** List[str] - List of function names

**Example:**
```python
from useful_utils import list_functions

functions = list_functions()
print(functions)  # ['set_debug']
```

### `get_function_info(function_name)`

Get detailed information about a specific function.

**Parameters:**
- `function_name` (str): Name of the function

**Returns:** Optional[Dict] - Function information or None if not found

---

## Logging Utilities (`utils/logging_utils.py`)

### `set_debug(debug_mode=True)`

Configure loguru logger with debug or info level.

**Parameters:**
- `debug_mode` (bool): If `True`, shows DEBUG level messages. If `False`, shows INFO level and above.

**Returns:** None

**Example:**
```python
from useful_utils import set_debug
from loguru import logger

# Enable debug mode (shows all log levels)
set_debug(debug_mode=True)
logger.debug("This will be shown")
logger.info("This will be shown")
logger.warning("This will be shown")

# Disable debug mode (shows INFO and above only)
set_debug(debug_mode=False)
logger.debug("This will NOT be shown")
logger.info("This will be shown")
logger.warning("This will be shown")
```

**Features:**
- 🟢 Visual debug mode indicator
- 🔴 Visual info mode indicator
- Automatic logger configuration
- Clean console output without timestamps
- Removes default loguru handlers

**Use Cases:**
- Development vs production logging
- Conditional debug output
- Clean console logging for CLI tools
- Consistent logging across projects

---

*More utilities will be added here as the library grows.* 