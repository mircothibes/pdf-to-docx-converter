"""
PDF to DOCX Converter Tool

This script performs batch or individual conversion of PDF files into DOCX format.
It supports both CLI and GUI usage. Users can either provide a folder containing PDF files
or a list of specific files. All converted DOCX files are saved to the specified output directory.

Features:
---------
- Reads configuration values (input folder, output folder, and log file path) from a `.env` file.
- Automatically creates missing directories.
- Supports both folder-based and file list conversion.
- Logs all actions, successes, and errors.
- Prints a clean summary to the terminal.
- Integrated with GUI via tkinter (`gui.py`).

Usage:
------
- CLI: Automatically runs using values from the `.env` file.
- GUI: Can be triggered using the tkinter interface in `gui.py`.

Dependencies:
-------------
- pdf2docx : For converting PDF files to DOCX.
- python-dotenv : For reading environment variables from a `.env` file.
- os, logging : Built-in modules used for file management and logging.

Author: Marcos Kemer  
Date: July 2025
"""

import os  # Used for file/directory manipulation
import logging  # Handles application logging
from dotenv import load_dotenv  # Loads environment variables from a .env file
from pdf2docx import Converter  # Library to convert PDF to DOCX


def setup_logging(log_path: str):
    """
    Sets up the logging configuration.

    Parameters:
    -----------
    log_path : str
        Path to the log file where logs will be saved.
    """
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging started.")


def convert_pdfs_to_docx(input_source, output_dir: str):
    """
    Converts one or more PDF files to DOCX format.

    Parameters:
    -----------
    input_source : str | list | tuple
        Can be either:
            - A path to a directory containing PDF files.
            - A list/tuple of full file paths to specific PDF files.

    output_dir : str
        Path to the directory where converted DOCX files will be saved.

    Behavior:
    ---------
    - Filters out invalid files.
    - Converts each PDF to DOCX.
    - Logs each success and failure.
    - Prints a summary to the terminal.
    """
    try:
        logging.info("Starting PDF to DOCX conversion.")

        # Detect and process input type
        if isinstance(input_source, (list, tuple)):
            # If a list or tuple, ensure each path is a PDF and a file
            pdf_files = [f for f in input_source if f.lower().endswith(".pdf") and os.path.isfile(f)]
        elif isinstance(input_source, str) and os.path.isdir(input_source):
            # If a folder path, list and filter valid PDF files
            pdf_files = [
                os.path.join(input_source, f)
                for f in os.listdir(input_source)
                if f.lower().endswith(".pdf") and os.path.isfile(os.path.join(input_source, f))
            ]
        else:
            logging.error("Invalid input path or file list provided.")
            print("Invalid input path or file list.")
            return

        if not pdf_files:
            logging.warning("No PDF files found to convert.")
            print("No valid PDF files found.")
            return

        success_count = 0  # Counter for successful conversions

        # Loop over all PDF files and convert
        for pdf_path in pdf_files:
            filename = os.path.splitext(os.path.basename(pdf_path))[0]  # Extract file name without extension
            docx_path = os.path.join(output_dir, filename + ".docx")

            logging.info(f"Converting: {pdf_path} → {docx_path}")
            try:
                # Perform conversion
                converter = Converter(pdf_path)
                converter.convert(docx_path, start=0, end=None)
                converter.close()

                logging.info(f"Successfully converted: {filename}")
                success_count += 1
            except Exception as e:
                # Catch conversion-level errors (per file)
                logging.error(f"Failed to convert {filename}: {e}")

        # Print summary to console
        print("\n--- Conversion Summary ---")
        print(f"Total PDF files found: {len(pdf_files)}")
        print(f"Successfully converted: {success_count}")
        print(f"Failed to convert: {len(pdf_files) - success_count}")

    except Exception as e:
        # Catch higher-level errors (global)
        logging.critical(f"Unexpected error: {e}")
        print(f"Critical error during conversion: {e}")


def main():
    """
    Entry point for script execution via CLI.

    Loads configuration from `.env`, ensures directories exist,
    sets up logging, and starts conversion process.
    """
    # Load values from .env file
    load_dotenv()
    input_folder = os.getenv("INPUT_FOLDER")
    output_folder = os.getenv("OUTPUT_FOLDER")
    log_file = os.getenv("LOG_FILE")

    # Ensure input/output folders exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # Initialize logging
    setup_logging(log_file)

    # Run conversion based on configured input
    convert_pdfs_to_docx(input_folder, output_folder)


# CLI entry point
if __name__ == "__main__":
    main()


