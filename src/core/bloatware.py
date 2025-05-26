def remove_bloatware(app_name):
    """Remove a specified bloatware application."""
    import subprocess

    try:
        # Command to uninstall the application
        command = f"powershell -Command \"Get-AppxPackage *{app_name}* | Remove-AppxPackage\""
        subprocess.run(command, shell=True, check=True)
        print(f"{app_name} has been successfully removed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove {app_name}. Error: {e}")

def list_bloatware():
    """List installed bloatware applications."""
    import subprocess

    try:
        # Command to list installed applications
        command = "powershell -Command \"Get-AppxPackage | Select Name, PackageFullName\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("Installed bloatware applications:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to list bloatware. Error: {e}")