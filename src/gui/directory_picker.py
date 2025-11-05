import tkinter as tk
from tkinter import filedialog
from typing import Optional

def select_directory(title: str = "Select input image directory") -> Optional[str]:
    """
    Show a directory selection dialog and return the selected path as string,
    or empty string if canceled.
    """
    root = tk.Tk()
    root.withdraw()  # hide the main window
    directory = filedialog.askdirectory(title=title)
    root.destroy()
    return directory
