"""
gui.py

Graphical User Interface (GUI) for the PDF to DOCX Converter Application.

This module provides an interactive interface using the Tkinter library, allowing users to:
1. Select one or more PDF files from their local system.
2. Choose an output directory to save the converted DOCX files.
3. Start the conversion process with a single click.
4. Receive visual feedback on the number of selected files and selected folder.
5. Display success or error messages via message boxes.

The GUI interacts with the backend logic defined in `main.py`, specifically:
- convert_pdfs_to_docx: for converting PDFs to DOCX.
- setup_logging: for logging events and errors to a log file.

Logging is automatically initialized and stored in the `logs/gui_conversion.log` file.

Author: Marcos Kemer  
Date: 2025-07-28
"""

import os  # For directory creation
import tkinter as tk  # GUI framework
from tkinter import filedialog, messagebox  # GUI dialogs
from my_package.main import convert_pdfs_to_docx, setup_logging  # Core functions
import logging  # For application logging
import sys  # For handling system exit (used in frozen executable check)

class PDFtoDOCXApp:
    """
    GUI application class for converting PDF files to DOCX format.
    Allows users to select files and a destination folder, then convert.
    """
    def __init__(self, master):
        """
        Initializes the GUI layout and application components.
        """
        self.master = master
        master.title("PDF to DOCX Converter")
        master.geometry("400x280")
        master.resizable(False, False)  # Prevent resizing

        self.input_files = []   # List to hold selected PDF paths
        self.output_dir = ""    # Selected output folder

        # --- Widgets: Labels & Buttons ---

        tk.Label(master, text="Input files (PDFs):").pack(pady=5)

        self.btn_input = tk.Button(master, text="Select PDF files", command=self.select_input_files)
        self.btn_input.pack()

        tk.Label(master, text="Output folder (DOCX):").pack(pady=10)

        self.btn_output = tk.Button(master, text="Select folder", command=self.select_output_dir)
        self.btn_output.pack()

        self.convert_button = tk.Button(master, text="Convert files", command=self.convert_files)
        self.convert_button.pack(pady=15)

        self.exit_button = tk.Button(master, text="Exit", command=self.master.quit)
        self.exit_button.pack()

        self.status_label = tk.Label(master, text="", fg="blue")
        self.status_label.pack(pady=5)

        # Ensure the logs directory exists
        os.makedirs("logs", exist_ok=True)
        setup_logging("logs/gui_conversion.log")

    def select_input_files(self):
        """
        Opens file dialog for user to select one or more PDF files.
        """
        self.input_files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf")]
        )
        count = len(self.input_files)
        self.status_label.config(text=f"{count} file(s) selected")

    def select_output_dir(self):
        """
        Opens folder dialog for user to choose the output directory.
        """
        self.output_dir = filedialog.askdirectory(title="Select output folder")
        if self.output_dir:
            self.status_label.config(text=f"Output folder selected")

    def convert_files(self):
        """
        Starts the PDF to DOCX conversion after validating inputs.
        """
        if not self.input_files:
            messagebox.showerror("Error", "No PDF files selected.")
            return

        if not self.output_dir:
            messagebox.showerror("Error", "No output folder selected.")
            return

        try:
            convert_pdfs_to_docx(self.input_files, self.output_dir)
            messagebox.showinfo("Success", "Conversion completed successfully.")
        except Exception as e:
            logging.error(f"GUI conversion error: {e}")
            messagebox.showerror("Conversion Error", f"An error occurred:\n{e}")

# Entry point: GUI starts only if script is run directly
def main():
    try:
        root = tk.Tk()
        app = PDFtoDOCXApp(root)
        root.mainloop()
    except Exception as e:
        logging.critical(f"Fatal GUI error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


