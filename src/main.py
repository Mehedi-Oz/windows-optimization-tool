import os
import sys
import logging
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QFrame,
    QMessageBox,
    QStyleFactory,
)
from PySide6.QtCore import Qt, QFile
from PySide6.QtGui import QIcon
from ui.themes import ThemeManager
from ui.tabs import create_tabs
from ui.components.titlebar import TitleBar

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

from config import (
    APP_NAME, WINDOW_MIN_SIZE, ICON_PATH,
    REGISTRY_ORG, REGISTRY_APP, DEFAULT_THEME
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setMinimumSize(*WINDOW_MIN_SIZE)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set window icon
        if QFile.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))
            logging.info("Window icon loaded successfully")
        else:
            logging.warning(f"Icon file not found at {ICON_PATH}")

        # Initialize settings
        self.settings = QSettings(REGISTRY_ORG, REGISTRY_APP)
        if self.settings.value("geometry"):
            self.restoreGeometry(self.settings.value("geometry"))
            logging.info("Window geometry restored")
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add custom title bar
        self.title_bar = TitleBar(self)
        main_layout.addWidget(self.title_bar)

        # Add separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background-color: #2C2E33;")
        main_layout.addWidget(separator)

        # Create tab widget with styling
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setStyleSheet(
            """
            QTabWidget::pane {
                border: none;
                background: transparent;
            }
            QTabBar::tab {
                padding: 8px 16px;
                margin: 4px 2px 0px 2px;
                border-radius: 4px 4px 0 0;
            }
        """
        )
        main_layout.addWidget(self.tab_widget)

        # Initialize theme manager and apply theme
        self.theme_manager = ThemeManager()
        self.theme_manager.apply_theme(self, "dark")

        # Create tabs
        create_tabs(self.tab_widget)

    def closeEvent(self, event):
        # Save window geometry
        self.settings.setValue("geometry", self.saveGeometry())

        reply = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    try:
        app = QApplication(sys.argv)
        app.setStyle("Fusion")

        window = MainWindow()
        window.show()
        logging.info("Application started successfully")

        return app.exec()
    except Exception as e:
        logging.error(f"Application failed to start: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
