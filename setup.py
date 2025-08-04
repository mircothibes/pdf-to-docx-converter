from setuptools import setup, find_packages

setup(
    name='pdf_tool_marcos',
    version='0.1.0',
    author='Marcos Kemer',
    description='A PDF to DOCX converter with GUI built using Tkinter.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pdf2docx',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'pdf2docx-gui = my_package.gui:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
)
