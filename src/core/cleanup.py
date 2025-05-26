def clean_temp_files():
    """Function to clean temporary files."""
    import os
    import shutil
    temp_dir = os.path.join(os.environ['TEMP'])
    try:
        shutil.rmtree(temp_dir)
        print("Temporary files cleaned successfully.")
    except Exception as e:
        print(f"Error cleaning temporary files: {e}")

def clear_dns_cache():
    """Function to clear DNS cache."""
    import subprocess
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("DNS cache cleared successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error clearing DNS cache: {e}")

def clear_windows_update_cache():
    """Function to clear Windows Update cache."""
    import os
    import shutil
    update_cache_dir = r"C:\Windows\SoftwareDistribution\Download"
    try:
        shutil.rmtree(update_cache_dir)
        print("Windows Update cache cleared successfully.")
    except Exception as e:
        print(f"Error clearing Windows Update cache: {e}")

def defragment_system_drive():
    """Function to defragment the system drive."""
    import subprocess
    try:
        subprocess.run(["defrag", "C:"], check=True)
        print("System drive defragmented successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error defragmenting system drive: {e}")