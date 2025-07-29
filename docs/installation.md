# Installation Guide

Setup and configuration instructions for the Useful Utils library.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Internet connection (for GitHub installation)

## Installation

### Method 1: Install from GitHub (Recommended)

```bash
# Install directly from GitHub
pip install git+https://github.com/yourusername/useful_utils.git

# Or install a specific branch
pip install git+https://github.com/yourusername/useful_utils.git@main
```

### Method 2: Clone and Install Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/useful_utils.git
cd useful_utils

# Install in development mode
pip install -e .
```

### Method 3: Manual Installation

```bash
# Clone the repository
git clone <repository-url>
cd useful_utils

# Install dependencies
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
# Test the package
python -c "from utils import help; print(help('list'))"

# Or run examples
python examples/logging_example.py
```

## Virtual Environment (Recommended)

It's recommended to use a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Dependencies

### Required Packages

- **loguru** (>=0.7.0) - Advanced logging library

### Optional Dependencies

None currently required.

## Configuration

### Environment Variables

You can set debug mode using environment variables:

```bash
# Enable debug mode
export DEBUG=true
python your_script.py

# Disable debug mode
export DEBUG=false
python your_script.py
```

### Python Configuration

```python
import os
from utils.logging_utils import set_debug

# Set debug mode from environment variable
debug_mode = os.getenv('DEBUG', 'false').lower() == 'true'
set_debug(debug_mode=debug_mode)
```

## Troubleshooting

### Common Issues

1. **Import Error: No module named 'utils'**
   - Make sure you're in the correct directory
   - Add the project root to your Python path:
     ```python
     import sys
     import os
     sys.path.append(os.path.dirname(os.path.abspath(__file__)))
     ```

2. **loguru not found**
   - Install dependencies: `pip install -r requirements.txt`
   - Check if virtual environment is activated

3. **Permission errors**
   - Use virtual environment instead of system Python
   - Check file permissions

### Getting Help

- Check the [functions documentation](functions.md) for API reference
- See [usage examples](examples.md) for common patterns
- Run example scripts to verify installation 