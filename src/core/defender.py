def enable_defender():
    """Enable Windows Defender."""
    import subprocess
    subprocess.run(["powershell", "-Command", "Set-MpPreference -DisableRealtimeMonitoring $false"])

def disable_defender():
    """Disable Windows Defender."""
    import subprocess
    subprocess.run(["powershell", "-Command", "Set-MpPreference -DisableRealtimeMonitoring $true"])