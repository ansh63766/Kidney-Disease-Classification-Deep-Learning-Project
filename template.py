import os
from pathlib import Path
import logging

# Configure logging format and level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name definition
project_name = 'cnnClassifier'

# List of files and directories to be created
list_of_files = [
    # GitHub workflows directory
    ".github/workflows/.gitkeep",
    
    # Source code directories and files
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
    # Configuration files
    "config/config.yaml",
    
    # DVC pipeline files
    "dvc.yaml",
    "params.yaml",
    
    # Project setup and dependencies
    "requirements.txt",
    "setup.py",
    
    # Research-related files
    "research/trials.ipynb",
    
    # Templates for web interfaces
    "templates/index.html"
]

# Create directories and files
for filepath in list_of_files:
    # Convert string path to a `Path` object for cross-platform compatibility
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # Create empty files if they don't exist or are empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")
