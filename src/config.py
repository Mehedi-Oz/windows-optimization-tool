import os

# Application settings
APP_NAME = "Windows Optimization Tool"
APP_VERSION = "1.0.0"

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "src", "assets")
ICON_PATH = os.path.join(ASSETS_DIR, "code.jpg")

# Theme settings
DEFAULT_THEME = "dark"
WINDOW_MIN_SIZE = (700, 500)

# Registry settings
REGISTRY_ORG = "WindowsOptimizationTool"
REGISTRY_APP = "MainWindow"