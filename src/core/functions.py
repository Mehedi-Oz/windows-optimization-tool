import os
import subprocess
import winreg
import ctypes
from pathlib import Path

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

def clear_temp_files():
    """Clear temporary files from Windows and User temp directories."""
    temp_paths = [
        os.environ.get('TEMP'),
        os.environ.get('TMP'),
        r'C:\Windows\Temp'
    ]
    
    for path in temp_paths:
        if path:
            try:
                for item in Path(path).glob('*'):
                    try:
                        if item.is_file():
                            item.unlink()
                        elif item.is_dir():
                            for sub_item in item.glob('*'):
                                sub_item.unlink(missing_ok=True)
                            item.rmdir()
                    except:
                        continue
            except:
                continue
    return True

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
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "HideFileExt", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        # Refresh Explorer
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], check=False)
        subprocess.Popen("explorer.exe")
        return True
    except WindowsError:
        return False

def optimize_network():
    """Optimize network adapter settings."""
    try:
        commands = [
            "netsh interface tcp set global autotuninglevel=normal",
            "netsh interface tcp set global chimney=enabled",
            "netsh interface tcp set global dca=enabled",
            "netsh interface tcp set global netdma=enabled",
            "powershell Set-NetAdapterAdvancedProperty -Name '*' -RegistryKeyword '*PowerSaving*' -RegistryValue 0"
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

def set_high_performance():
    """Set power plan to high performance."""
    try:
        # High Performance power plan GUID
        subprocess.run([
            "powershell.exe",
            "-Command",
            "powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
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
    