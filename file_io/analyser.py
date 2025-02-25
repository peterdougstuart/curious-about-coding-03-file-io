import tkinter as tk
from tkinter import filedialog


class BaseAnalyserForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple File Analysis")
        self._create_widgets()

    def _create_widgets(self):
        # StringVar to hold the selected file path
        self.file_path = tk.StringVar()

        # Row 0 - "Select a file" label, file entry, and "Browse" button
        tk.Label(self, text="Select a file:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.file_path, width=50).grid(
            row=0, column=1, padx=5, pady=5
        )
        tk.Button(self, text="Browse", command=self._browse_file).grid(
            row=0, column=2, padx=5, pady=5
        )

        # Row 1 - "Analyze" button
        tk.Button(self, text="Analyze", command=self._click_analyse).grid(
            row=1, column=1, pady=10
        )

        # Row 2 - Text widget to serve as our "console"
        self.console_text = tk.Text(self, height=10, width=60)
        self.console_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def _browse_file(self):
        """Let the user select a file and store its path in self.file_path."""
        path = filedialog.askopenfilename()
        self.file_path.set(path)

    def _click_analyse(self):

        path = self.file_path.get()

        if not path:
            self.log_text("No file selected.")
        else:
            self.log_text(f"Selected file: {path}")
            self.analyse(path)

    def analyse(self):
        self.log_text("Base analyze method called. Override this in your subclass.")

    def log_text(self, message):
        """
        A helper method to log text to the console widget.
        """
        self.console_text.insert(tk.END, message + "\n")
        self.console_text.see(tk.END)
