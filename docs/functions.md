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

## Performance Utilities (`useful_utils/timing_utils.py`)

### `log_time(label="⏱️ Code block")`

Context manager for timing a block of code and logging the time.

**Parameters:**
- `label` (str): Label to display in the log message (default: "⏱️ Code block")

**Returns:** Context manager

**Example:**
```python
from useful_utils import log_time
from loguru import logger

with log_time("Data processing"):
    # Your code here
    process_data()
    logger.info("Processing complete")
```

### `timeit(label="⏱️ Function")`

Decorator version of log_time for timing functions.

**Parameters:**
- `label` (str): Label to display in the log message (default: "⏱️ Function")

**Returns:** Decorator function

**Example:**
```python
from useful_utils import timeit

@timeit("Training model")
def train_model():
    # Your function code here
    pass
```

**Features:**
- ⏱️ Visual timing indicators
- Automatic logging with loguru
- Context manager and decorator patterns
- Nested timing support
- Clean, readable output

**Use Cases:**
- Performance monitoring
- Code profiling
- Debugging slow operations
- Production timing logs

---

*More utilities will be added here as the library grows.* 