# Useful Utils

A collection of reusable code snippets and utilities for cross-project development.

## Quick Start

### Clone and Use
```bash
git clone https://github.com/ThaiHungN/useful_utils.git
cd useful_utils
pip install -r requirements.txt
```

### Import and Use
```python
from useful_utils import set_debug, help
```

3. **Get help:**
   ```python
   help('list')                    # List all functions
   help('detail', 'set_debug')     # Get function details
   help('search', 'logging')       # Search functions
   ```

### Alternative: Add to Python Path
```python
import sys
sys.path.append('/path/to/useful_utils')
from useful_utils import help, set_debug
```

## Built-in Help System

The library includes an interactive help system for quick function lookup:

```python
from useful_utils import help

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

## Public Usage

This is a public utility library. Feel free to:
- Install and use in any project
- Fork and modify for your needs
- **Add your own useful functions** (see [CONTRIBUTING.md](CONTRIBUTING.md))
- Contribute improvements
- Share with others

## Contributing

**Everyone is welcome to add functions!** 🚀

This library grows through community contributions. If you have a useful function that others might benefit from, please add it!

- 📖 **See [CONTRIBUTING.md](CONTRIBUTING.md)** for detailed instructions
- 🔧 **Simple format** - Just follow the template
- 🎯 **Built-in help system** - Your functions automatically appear in `help('list')`
- 📚 **Auto-documentation** - Examples and docs are generated automatically

## Project Structure

```
useful_utils/
├── useful_utils/   # Main package (utility modules)
├── examples/       # Example scripts
├── docs/          # Documentation
├── requirements.txt
├── setup.py       # Package configuration
└── pyproject.toml # Modern Python packaging
```

## Adding New Utilities

1. Create utility module in `utils/`
2. Update `docs/functions.md` with documentation
3. Add examples to `docs/examples.md`
4. Update `requirements.txt` if needed

## Dependencies

See `requirements.txt` for the complete list.
