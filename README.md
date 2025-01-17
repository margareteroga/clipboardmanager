# ClipboardManager

ClipboardManager is a simple Python application that manages clipboard history on Windows. It allows users to save and retrieve previous clipboard entries, providing an easy way to access frequently used text snippets.

## Features

- Save current clipboard content to history.
- Retrieve and copy previous clipboard entries back to the clipboard.
- Delete specific entries from the clipboard history.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `pyperclip` library

## Installation

1. Clone the repository or download the `ClipboardManager.py` file.

2. Install the required `pyperclip` library if it's not already installed:

   ```bash
   pip install pyperclip
   ```

3. Run the application:

   ```bash
   python ClipboardManager.py
   ```

## Usage

1. Launch the application.
2. Use the "Save Clipboard" button to save the current clipboard content to the history.
3. Select an entry from the list and click "Retrieve" to copy it back to the clipboard.
4. Select an entry and click "Delete" to remove it from the history.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI toolkit.
- [Pyperclip](https://pypi.org/project/pyperclip/) - A cross-platform clipboard module for Python.