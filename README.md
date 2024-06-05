# debug_sys

## Overview

`debug_sys` is a Python module designed to facilitate logging and managing log files in your applications. It offers functionalities to log messages with different types and content, as well as the ability to clear and archive log files. The module is particularly useful for developers who need a straightforward and efficient way to handle logging in their projects.

## Features

- **Logging Messages**: Log messages with specified types and content, with options to limit the content size.
- **Clearing Logs**: Clear the content of log files with optional archiving.
- **Customizable Log Files**: Specify the name and location of log files.

## Installation

To install `debug_sys`, simply copy the `debug_sys.py` file to your project directory.

## Usage

### Logging Messages

To log a message, use the `log` function:

```python
from debug_sys import log

# Example of logging a message
log(msg_type="INFO", msg_content="This is an informational message.")
```

You can also specify a list of message types and a custom content size limit:

```python
log(msg_type=["ERROR", "DATABASE"], msg_content="Database connection failed.", content_size_limit=100)
```

### Clearing Logs

To clear the content of a log file and optionally archive it, use the `clear_logs` function:

```python
from debug_sys import clear_logs

# Example of clearing logs with archiving
clear_logs(file="application.log", archive=True, saving_folder="log_archives")
```

### Function Definitions

#### `log`

```python
def log(msg_type: str | list[str], msg_content: str, content_size_limit: int = 150, file: str = 'gaza') -> None:
    """
    Enregistre un message dans un fichier journal spécifié.
    
    Args:
        msg_type (str | list[str]): Le ou les types du message à enregistrer.
        msg_content (str): Le contenu du message à enregistrer.
        content_size_limit (int, optional): La limite de taille du contenu du message. Par défaut, elle est fixée à 150 caractères.
        file (str, optional): Le nom du fichier journal dans lequel enregistrer le message. Par défaut, il est fixé à 'gaza.log'.
    
    Returns:
        None
    """
```

#### `clear_logs`

```python
def clear_logs(file: str = 'gaza.log', archive: bool = True, saving_folder: str = None) -> bool:
    """
    Efface le contenu d'un fichier log et l'archive éventuellement dans un dossier spécifié.
    
    Args:
        file (str, optional): Chemin d'accès complet du fichier log à effacer et à archiver. Par défaut, 'gaza.log'.
        archive (bool, optional): Si True, le fichier log sera archivé avant d'être effacé. Par défaut, True.
        saving_folder (str, optional): Chemin d'accès du dossier dans lequel l'archive du fichier log sera sauvegardée. 
                                       Si aucun dossier n'est spécifié ou si le dossier n'existe pas, l'archive sera sauvegardée 
                                       dans le même dossier que le fichier log d'origine. Par défaut, None.
    
    Returns:
        bool: True si le fichier log a été effacé et éventuellement archivé avec succès, False sinon.
    """
```

## Version

Current version: 2.4.1

## Authors

- CUISSET Mattéo

## License

This project is licensed under the [APACHE License](https://github.com/Flyns157/debug_sys/blob/main/LICENSE). See the [LICENSE file](https://github.com/Flyns157/debug_sys/blob/main/LICENSE) for details.

---

For further questions or contributions, feel free to contact the author or open an issue on the project's repository.
