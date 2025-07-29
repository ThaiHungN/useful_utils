# Usage Examples

Practical examples and patterns for using the utilities.

## Help System Examples

### Basic Help Usage

```python
from useful_utils import help

# Show help system usage
print(help())

# List all available functions
print(help('list'))

# Get detailed information about a function
print(help('detail', 'set_debug'))

# Search for functions
print(help('search', 'debug'))
```

### Interactive Development

```python
from useful_utils import help, set_debug

# Quick lookup during development
print(help('list'))  # See what's available

# Get function details
print(help('detail', 'set_debug'))

# Use the function
set_debug(debug_mode=True)
```

### Programmatic Access

```python
from useful_utils import list_functions, get_function_info

# Get list of functions programmatically
functions = list_functions()
print(f"Available functions: {functions}")

# Get function info as data
info = get_function_info('set_debug')
if info:
    print(f"Function: {info['name']}")
    print(f"Category: {info['category']}")
    print(f"Description: {info['description']}")
```

## Logging Examples

### Basic Usage

```python
from useful_utils import set_debug
from loguru import logger

# Simple debug toggle
set_debug(True)  # Show all messages
logger.debug("Processing started")
logger.info("File loaded successfully")

set_debug(False)  # Show only INFO and above
logger.debug("This won't show")
logger.info("This will show")
```

### Development vs Production

```python
import os
from useful_utils import set_debug
from loguru import logger

# Automatically set debug mode based on environment
is_development = os.getenv('ENVIRONMENT') == 'development'
set_debug(debug_mode=is_development)

def process_data(data):
    logger.debug(f"Input data: {data}")
    
    if len(data) > 1000:
        logger.warning("Large dataset detected")
    
    result = data.upper()
    logger.info(f"Processed {len(data)} items")
    
    return result
```

### CLI Application Pattern

```python
import argparse
from useful_utils import set_debug
from loguru import logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    # Set logging level based on CLI argument
    set_debug(debug_mode=args.debug)
    
    logger.info("Application started")
    
    # Your application logic here
    process_files()
    
    logger.info("Application completed")

def process_files():
    logger.debug("Starting file processing")
    # ... processing logic
    logger.info("Files processed successfully")
```

### Error Handling with Logging

```python
from useful_utils import set_debug
from loguru import logger

set_debug(debug_mode=True)

def safe_divide(a, b):
    logger.debug(f"Attempting division: {a} / {b}")
    
    try:
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Cannot divide {a} by zero")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None

# Usage
safe_divide(10, 2)   # Success
safe_divide(10, 0)   # Error logged
```

### Configuration Management

```python
import json
from useful_utils import set_debug
from loguru import logger

def load_config(config_path):
    logger.debug(f"Loading config from: {config_path}")
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Set debug mode from config
        debug_mode = config.get('debug', False)
        set_debug(debug_mode=debug_mode)
        
        logger.info("Configuration loaded successfully")
        return config
        
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in config file: {config_path}")
        return {}
```

## Running Examples

You can run the provided example scripts:

```bash
# Run the logging example
python examples/logging_example.py

# Run with debug mode
python examples/logging_example.py --debug
```

## Best Practices

1. **Set debug mode early** in your application startup
2. **Use appropriate log levels:**
   - `DEBUG`: Detailed information for debugging
   - `INFO`: General information about program execution
   - `WARNING`: Something unexpected happened but the program can continue
   - `ERROR`: A serious problem occurred

3. **Include context** in log messages for better debugging
4. **Use structured logging** for complex data
5. **Keep production logs clean** by setting `debug_mode=False` 