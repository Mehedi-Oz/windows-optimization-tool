# filepath: c:\A - PROJECTS\windows-gui\src\ui\components\widgets.py
from PySide6.QtWidgets import QPushButton, QLabel, QCheckBox, QGroupBox, QVBoxLayout, QHBoxLayout, QWidget

class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: #0078d4; color: white; border-radius: 5px; padding: 10px;")

class CustomLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("color: #ffffff; font-size: 12pt;")

class CustomCheckBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("color: #ffffff;")

class CustomGroupBox(QGroupBox):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("QGroupBox { border: 1px solid #3d3d3d; border-radius: 5px; }")
        self.setLayout(QVBoxLayout())
    
    def add_widget(self, widget):
        self.layout().addWidget(widget)