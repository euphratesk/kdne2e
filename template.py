import os
from pathlib import Path 
import logging


#logging string
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'


list_of_files = [
    ".github/workflows/.gitkeep",   #bu github da gorunmeyecek cod olamdigi committe githuba aktarilmayacak  icin daha sonra CICD icin kullancagiz - CICD Pipeline
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
   " templates/index.html"

]
