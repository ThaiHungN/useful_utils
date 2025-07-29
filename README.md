# Useful Utils

A collection of reusable code snippets and utilities for cross-project development.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Import utilities:**
   ```python
   from utils import set_debug, help
   ```

3. **Get help:**
   ```python
   help('list')                    # List all functions
   help('detail', 'set_debug')     # Get function details
   help('search', 'logging')       # Search functions
   ```

## Built-in Help System

The library includes an interactive help system for quick function lookup:

```python
from utils import help

help()                    # Show help usage
help('list')             # List all available functions
help('detail', 'set_debug')  # Get detailed function information
help('search', 'debug')   # Search functions by name or description
```

## Documentation

- **📚 [Documentation Index](docs/README.md)** - Complete documentation overview
- **📖 [Available Functions](docs/functions.md)** - Complete list of all utilities with examples
- **📚 [Usage Examples](docs/examples.md)** - Detailed usage examples and patterns
- **🔧 [Installation Guide](docs/installation.md)** - Setup and configuration details

## Project Structure

```
useful_utils/
├── utils/          # Utility modules
├── examples/       # Example scripts
├── docs/          # Documentation
└── requirements.txt
```

## Adding New Utilities

1. Create utility module in `utils/`
2. Update `docs/functions.md` with documentation
3. Add examples to `docs/examples.md`
4. Update `requirements.txt` if needed

## Dependencies

See `requirements.txt` for the complete list.
