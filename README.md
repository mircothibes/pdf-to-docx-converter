# 🧩 PDFtoDOCX Converter

A simple and user-friendly desktop application to batch convert `.pdf` files to `.docx` format using a clean graphical interface built with **Tkinter**.

## 🚀 Features

- ✅ Convert one or multiple PDF files to DOCX format.
- ✅ Select output folder for saving the converted files.
- ✅ Simple and intuitive GUI.
- ✅ Desktop shortcut with custom icon.
- ✅ Built with Python 🐍.

---

## 🖼️ Screenshots

### Application Icon
<img src="https://github.com/mircothibes/pdf-to-docx-converter/raw/main/docs/images/icon.png" width="80">

### Main Interface
<img src="https://github.com/mircothibes/pdf-to-docx-converter/raw/main/docs/images/interface.png" width="300">

### Success Message
<img src="https://github.com/mircothibes/pdf-to-docx-converter/raw/main/docs/images/success.png" width="250">

---

## 📁 Project Structure

pdf-to-docx-converter/
├── inputs_pdfs/ # Folder for input files (optional)
├── outputs_docx/ # Output folder for .docx files
├── logs/ # Logs are saved here
├── src/
│ └── my_package/
│ ├── main.py # PDF conversion logic
│ └── gui.py # GUI logic
├── scripts/
│ └── create_shortcut.ps1 # Powershell shortcut generator
├── dist/ # Compiled executable via PyInstaller
├── icon.ico # Custom icon for the executable
├── setup.py # Packaging config
├── pyproject.toml # Optional project config
└── README.md # You are here