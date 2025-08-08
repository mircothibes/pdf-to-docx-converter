# 🧩 PDFtoDOCX Converter
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-lightgrey)
![Build](https://img.shields.io/badge/Build-PyInstaller-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)


A simple and user-friendly desktop application to batch convert `.pdf` files to `.docx` format using a clean graphical interface built with **Tkinter**.

---

## 🚀 Features

- ✅ Convert one or multiple PDF files to DOCX format.  
- ✅ Select output folder for saving the converted files.  
- ✅ Simple and intuitive GUI.  
- ✅ Desktop shortcut with custom icon.  
- ✅ Built with Python 🐍.

---

## 🖼️ Screenshots

### Application Icon  
<img src="https://github.com/mircothibes/pdf-to-docx-converter/raw/main/docs/icon.png" width="80">

### Main Interface  
<img src="https://github.com/mircothibes/pdf-to-docx-converter/raw/main/docs/Interface.png" width="100">

### Success Message  
<img src="https://github.com/mircothibes/pdf-to-docx-converter/raw/main/docs/Success.png" width="100">

---

## 📁 Project Structure

```bash
pdf-to-docx-converter/
├── inputs_pdfs/             # Folder for input files (optional)
├── outputs_docx/            # Output folder for .docx files
├── logs/                    # Logs are saved here
├── src/
│   └── my_package/
│       ├── main.py          # PDF conversion logic
│       └── gui.py           # GUI logic
├── scripts/
│   └── create_shortcut.ps1  # PowerShell shortcut generator
├── dist/                    # Compiled executable via PyInstaller
├── icon.ico                 # Custom icon for the executable
├── setup.py                 # Packaging config
├── pyproject.toml           # Optional project config
└── README.md                # You are here
🛠️ Installation (Executable)
Download the latest .zip release from the Releases section.

Extract all contents.

Double-click gui.exe or use the desktop shortcut.

Select PDFs → Output folder → Convert. ✅

🐍 Run via Python (Developers)
Requirements
Python 3.11+

Virtual environment (recommended)

Installation
bash
Copiar
Editar
git clone https://github.com/mircothibes/pdf-to-docx-converter.git
cd pdf-to-docx-converter
python -m venv .venv
.venv\Scripts\activate
pip install -e .
Run
bash
Copiar
Editar
pdf2docx-gui
📦 Build Executable (PyInstaller)
To generate a .exe version for Windows:

bash
Copiar
Editar
pyinstaller --noconsole --onefile --icon=icone.ico src/my_package/gui.py
The output .exe will be placed in the dist/ folder.

👤 Author
Developed by Marcos Vinicius Thibes Kemer

📄 License
This project is licensed under the MIT License.
