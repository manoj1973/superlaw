import os

from dotenv import load_dotenv
from django.core.management import execute_from_command_line
import sys
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlaw_django_project.settings")
# Support for PyInstaller's temp extraction (_MEIPASS)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Load .env (even if embedded in .exe)
load_dotenv(resource_path(".env"))

if __name__ == '__main__':
    sys.argv += ['runserver', '127.0.0.1:8000', '--noreload']
    execute_from_command_line(sys.argv)