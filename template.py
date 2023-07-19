import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter you project name")
    if project_name != "":
        break

# src/__init__.py
# src/component/__init__py
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/___init__.py",
    f"{project_name}/config/___init__.py",
    f"{project_name}/constants/___init__.py",
    f"{project_name}/entity/___init__.py",
    f"{project_name}/exception/___init__.py",
    f"{project_name}/logger/___init__.py",
    f"{project_name}/pipeline/___init__.py",
    f"{project_name}/utils/___init__.py",
    f'config/config.yaml',
    "schema.yaml",
    "app.py",
    "main.py"
    "logs.py"
    "exception.py"
    "setup.py"
]

for filpth in list_of_files:
    filepath = Path(filpth)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass

    else:
        logging.info("file is already present: {filepath}")