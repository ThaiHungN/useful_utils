# Public Usage Guide

This is a public utility library designed to be shared and used by everyone. Here's how to get started.

## Quick Installation

```bash
# Clone the repository
git clone https://github.com/ThaiHungN/useful_utils.git
cd useful_utils
pip install -r requirements.txt

# Or install in development mode (recommended for contributors)
pip install -e .
```

## Basic Usage

```python
# Import utilities
from useful_utils import help, set_debug
from loguru import logger

# Explore what's available
help('list')

# Get detailed information about a function
help('detail', 'set_debug')

# Use the logging utility
set_debug(debug_mode=True)
logger.info("Hello from useful_utils!")
```

## Jupyter Notebook Usage

```python
# In any Jupyter notebook
from useful_utils import help, set_debug

# Quick function discovery
help('list')

# Search for functions
help('search', 'logging')
```

## Command Line Usage

```bash
# Show available functions
useful-utils help list

# Get function details
useful-utils help detail set_debug

# Configure logging
useful-utils logging --debug --message "Test message"
```

## What You Can Do

✅ **Use freely** - Install and use in any project  
✅ **Fork and modify** - Customize for your needs  
✅ **Share with others** - Recommend to colleagues  
✅ **Contribute** - Add new utilities or improvements  

## Getting Help

- **Built-in help**: `help('list')` or `help('detail', 'function_name')`
- **Documentation**: Check the `docs/` folder
- **Examples**: Run `python examples/help_example.py`
- **Issues**: Report problems on GitHub

## Contributing

Feel free to:
- Add new utility functions
- Improve documentation
- Fix bugs
- Suggest new features

This library is designed to grow with the community! 