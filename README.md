# DEBUGSYS

DEBUGSYS is a custom implementation of a debugging system designed to provide developers with an efficient way to manage and log messages during the development process. It offers a modular logging system, allowing for easy integration and management of multiple loggers.

## Table of Contents

- [DEBUGSYS](#debugsys)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Additional Usage Examples](#additional-usage-examples)
  - [Features](#features)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Getting Started

This project provides a comprehensive logging system that allows developers to track and manage logs efficiently. It supports multiple loggers, each configurable with its own output file.

### Prerequisites

Before you begin, ensure you have the following software installed:

```bash
Python 3.12 or above
```

### Installation
Follow these steps to set up your development environment:

```bash
# Clone the repository
git clone https://github.com/Flyns157/debug_sys.git

# Navigate to the project directory
cd debug_sys

# Install dependencies
pip install -r debug_sys/requirements.txt
```

### Usage
To use DEBUGSYS, you can create instances of LogManager and manage your loggers effectively. Here's a basic example:

```python
from debug_sys.log_manager import LogManager


# Initialize the log manager
log_manager = LogManager()

# Add a new logger
log_manager.add_logger('example_logger', 'example.log')

# Log a message
log_manager.log('example_logger', 'INFO', 'This is an informational message.')

# Print the last 5 log messages
log_manager.print_logs('example_logger', limit=5)
```

### Additional Usage Examples
Clear Logs: You can clear the logs of a specific logger.

```python
log_manager.clear_logs('example_logger', archive=True, saving_folder='archive/')
```

Accessing Loggers: You can access loggers directly via their names.

```python
log_manager.EXAMPLE_LOGGER.log('ERROR', 'An error occurred.')
```

## Features
Multiple Loggers: Manage multiple loggers with different configurations.
Log Management: Add, clear, and print logs easily.
Customizable Logging: Set file names and content size limits for logs.

Archiving: Option to archive logs before clearing them.

## Contributing
We welcome contributions to DEBUGSYS! If you would like to contribute, please follow these steps:

Fork the repository
Create your feature branch (git checkout -b feature/NewFeature)
Commit your changes (git commit -m 'Add some NewFeature')
Push to the branch (git push origin feature/NewFeature)
Open a pull request
Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
CUISSET Mattéo - [matteo.cuisset@gmail.com](mailto:matteo.cuisset@gmail.com)

Project Link: [GitHub Repository Link](https://github.com/Flyns157/debug_sys.git)
