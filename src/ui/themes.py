from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

class ThemeManager:
    def __init__(self):
        self.themes = {
            "dark": {
                "background": "#1a1b1e",
                "secondary": "#25262b",
                "accent": "#4dabf7",
                "text": "#ffffff",
                "border": "#2C2E33",
                "button": "#25262b",
                "button_hover": "#4dabf7",
                "button_pressed": "#339af0",
                "tab_selected": "#25262b",
                "tab_unselected": "#1a1b1e"
            }
        }

    def apply_theme(self, widget, theme_name):
        if theme_name not in self.themes:
            return
        
        theme = self.themes[theme_name]
        widget.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background-color: {theme["background"]};
                color: {theme["text"]};
            }}
            
            QTabWidget::pane {{
                border: none;
                background: {theme["secondary"]};
                border-radius: 8px;
            }}
            
            QTabBar::tab {{
                background: {theme["tab_unselected"]};
                color: {theme["text"]};
                padding: 8px 16px;
                margin: 4px 2px 0px 2px;
                border-radius: 4px 4px 0 0;
            }}
            
            QTabBar::tab:selected {{
                background: {theme["tab_selected"]};
                color: {theme["accent"]};
            }}
            
            QPushButton {{
                background: {theme["button"]};
                color: {theme["text"]};
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }}
            
            QPushButton:hover {{
                background: {theme["button_hover"]};
            }}
            
            QPushButton:pressed {{
                background: {theme["button_pressed"]};
            }}
            
            QCheckBox {{
                color: {theme["text"]};
                spacing: 8px;
            }}
            
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 2px solid {theme["border"]};
            }}
            
            QCheckBox::indicator:checked {{
                background: {theme["accent"]};
                border: 2px solid {theme["accent"]};
            }}
            
            QGroupBox {{
                background: {theme["secondary"]};
                border-radius: 8px;
                padding: 16px;
                margin-top: 16px;
                color: {theme["text"]};
            }}
        """)