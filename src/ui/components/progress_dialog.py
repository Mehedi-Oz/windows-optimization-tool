import os
import subprocess
import winreg
import ctypes
from pathlib import Path
from PySide6.QtWidgets import QDialog, QProgressBar, QLabel, QVBoxLayout, QMessageBox
from PySide6.QtCore import Qt, Signal

class ProgressDialog(QDialog):
    finished = Signal(bool)

    def __init__(self, parent=None, title="Processing", message="Please wait..."):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowModality(Qt.WindowModal)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setFixedSize(300, 100)

        layout = QVBoxLayout(self)
        
        self.message_label = QLabel(message)
        self.message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.message_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        layout.addWidget(self.progress_bar)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)
    
    def create_restore_point():
        """Create a system restore point."""
        try:
            subprocess.run([
                "powershell.exe",
                "-Command",
                "Checkpoint-Computer -Description 'Windows Optimization Tool Restore Point' -RestorePointType 'MODIFY_SETTINGS'"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def toggle_windows_defender(enable=True):
        """Enable or disable Windows Defender."""
        try:
            if enable:
                subprocess.run([
                    "powershell.exe",
                    "-Command",
                    "Set-MpPreference -DisableRealtimeMonitoring $false"
                ], check=True)
            else:
                subprocess.run([
                    "powershell.exe",
                    "-Command",
                    "Set-MpPreference -DisableRealtimeMonitoring $true"
                ], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def set_high_performance():
        """Set power plan to high performance."""
        try:
            subprocess.run([
                "powercfg",
                "/setactive",
                "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def disable_telemetry():
        """Disable Windows telemetry and data collection."""
        try:
            keys = [
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection",
                r"SOFTWARE\Policies\Microsoft\Windows\DataCollection"
            ]
            for key_path in keys:
                key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "AllowTelemetry", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
            return True
        except WindowsError:
            return False

    def disable_superfetch():
        """Disable Superfetch/SysMain service."""
        try:
            subprocess.run([
                "powershell.exe",
                "-Command",
                "Stop-Service -Name 'SysMain' -Force; Set-Service -Name 'SysMain' -StartupType Disabled"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def show_file_extensions():
        """Show file extensions in Explorer."""
        try:
            key = winreg.CreateKeyEx(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
                0, winreg.KEY_WRITE
            )
            winreg.SetValueEx(key, "HideFileExt", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            # Refresh Explorer
            subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=False)
            subprocess.Popen("explorer.exe")
            return True
        except WindowsError:
            return False

    def optimize_network():
        """Optimize network settings."""
        try:
            commands = [
                "netsh interface tcp set global autotuninglevel=normal",
                "netsh interface tcp set global chimney=enabled",
                "netsh interface tcp set global dca=enabled",
                "netsh interface tcp set global netdma=enabled"
            ]
            for cmd in commands:
                subprocess.run(cmd, shell=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def clear_dns_cache():
        """Clear DNS resolver cache."""
        try:
            subprocess.run(["ipconfig", "/flushdns"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def remove_bloatware(app_name):
        """Remove specified Windows bloatware."""
        try:
            subprocess.run([
                "powershell.exe",
                "-Command",
                f"Get-AppxPackage *{app_name}* | Remove-AppxPackage"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def toggle_windows_update(enable=True):
        """Enable or disable Windows Update service."""
        try:
            action = "Automatic" if enable else "Disabled"
            subprocess.run([
                "powershell.exe",
                "-Command",
                f"Set-Service -Name 'wuauserv' -StartupType {action}"
            ], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        
        
