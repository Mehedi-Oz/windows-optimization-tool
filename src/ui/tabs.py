from .components.progress_dialog import ProgressDialog
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QCheckBox,
    QGroupBox,
    QScrollArea,
    QFrame
)
from PySide6.QtCore import Qt

from core.functions import (
    create_restore_point, clear_temp_files, toggle_windows_defender,
    set_high_performance, disable_telemetry, disable_superfetch,
    show_file_extensions, optimize_network, clear_dns_cache,
    remove_bloatware, toggle_windows_update
)
# Function mapping for checkbox actions
FUNCTION_MAPPING = {
    "Create System Restore Point": create_restore_point,
    "Clear Temporary Files": clear_temp_files,
    "Disable Windows Defender": lambda: toggle_windows_defender(False),
    "Enable Windows Defender": lambda: toggle_windows_defender(True),
    "Enable High Performance": set_high_performance,
    "Disable Telemetry": disable_telemetry,
    "Disable Superfetch/SysMain": disable_superfetch,
    "Show File Extensions": show_file_extensions,
    "Optimize Network Adapter": optimize_network,
    "Clean DNS Cache": clear_dns_cache,
    "Enable Windows Update": lambda: toggle_windows_update(True),
    "Disable Windows Update": lambda: toggle_windows_update(False),
    # Bloatware removal mappings
    "Xbox Game Bar": lambda: remove_bloatware("XboxGamingOverlay"),
    "Cortana": lambda: remove_bloatware("Microsoft.549981C3F5F10"),
    "OneDrive": lambda: remove_bloatware("Microsoft.OneDrive"),
    "3D Viewer": lambda: remove_bloatware("Microsoft.Microsoft3DViewer"),
    "Feedback Hub": lambda: remove_bloatware("Microsoft.WindowsFeedbackHub")
}

def create_scrollable_group(title, options, layout_type="vertical"):
    group = QGroupBox(title)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setFrameShape(QFrame.NoFrame)
    
    content = QWidget()
    layout = QVBoxLayout() if layout_type == "vertical" else QHBoxLayout()
    layout.setSpacing(12)
    
    for option in options:
        checkbox = QCheckBox(option)
        checkbox.setMinimumHeight(32)
        if option in FUNCTION_MAPPING:
            checkbox.stateChanged.connect(
                lambda state, fn=FUNCTION_MAPPING[option]: fn() if state else None
            )
        layout.addWidget(checkbox)
    
    content.setLayout(layout)
    scroll.setWidget(content)
    
    group_layout = QVBoxLayout()
    group_layout.addWidget(scroll)
    group.setLayout(group_layout)
    return group

def create_tabs(tab_widget):
    # Safety Tab
    safety_tab = QWidget()
    safety_layout = QVBoxLayout(safety_tab)
    safety_options = [
        "Create System Restore Point",
        "Backup Registry",
        "Enable System Protection"
    ]
    safety_layout.addWidget(create_scrollable_group("System Safety", safety_options))
    tab_widget.addTab(safety_tab, "Safety")

    # Clean Up Tab
    cleanup_tab = QWidget()
    cleanup_layout = QVBoxLayout(cleanup_tab)
    cleanup_options = [
        "Clear User Temp Files",
        "Clear Windows Temp Files",
        "Clean Prefetch Data",
        "Clean AMD Shader Cache",
        "Clean DNS Cache",
        "Clear Windows Update Cache",
        "Clean Junk Files (*.log, *.tmp, etc.)",
        "Defragment System Drive"
    ]
    cleanup_layout.addWidget(create_scrollable_group("System Cleanup", cleanup_options))
    tab_widget.addTab(cleanup_tab, "Clean Up")

    # Privacy Tab
    privacy_tab = QWidget()
    privacy_layout = QVBoxLayout(privacy_tab)
    privacy_options = [
        "Disable Telemetry",
        "Disable Cortana",
        "Disable Location Tracking",
        "Disable Activity History",
        "Disable Windows Tips",
        "Disable Feedback Hub"
    ]
    privacy_layout.addWidget(create_scrollable_group("Privacy Settings", privacy_options))
    tab_widget.addTab(privacy_tab, "Privacy")

    # Performance Tab
    performance_tab = QWidget()
    performance_layout = QVBoxLayout(performance_tab)
    performance_options = [
        "Enable High Performance Power Plan",
        "Optimize Network Adapter",
        "Disable Superfetch/SysMain",
        "Disable Edge Preload",
        "Show File Extensions",
        "Show Hidden Files"
    ]
    performance_layout.addWidget(create_scrollable_group("Performance Tweaks", performance_options))
    tab_widget.addTab(performance_tab, "Performance")

    # Bloatware Tab
    bloatware_tab = QWidget()
    bloatware_layout = QVBoxLayout(bloatware_tab)
    bloatware_options = [
        "Xbox Game Bar",
        "Cortana",
        "OneDrive",
        "3D Viewer",
        "Feedback Hub",
        "Microsoft Teams",
        "Your Phone"
    ]
    bloatware_layout.addWidget(create_scrollable_group("Remove Bloatware", bloatware_options))
    tab_widget.addTab(bloatware_tab, "Bloatware")

    # Windows Update Tab
    updates_tab = QWidget()
    updates_layout = QVBoxLayout(updates_tab)
    update_options = [
        "Enable Windows Update",
        "Disable Windows Update",
        "Defer Feature Updates"
    ]
    updates_layout.addWidget(create_scrollable_group("Windows Update Settings", update_options))
    tab_widget.addTab(updates_tab, "Updates")

    # Activation Tab
    activation_tab = QWidget()
    activation_layout = QVBoxLayout(activation_tab)
    activate_btn = QPushButton("Activate Windows & Office")
    activate_btn.setMinimumHeight(40)
    activation_layout.addWidget(activate_btn)
    activation_layout.addStretch()
    tab_widget.addTab(activation_tab, "Activation")
    
def execute_with_progress(parent, function, title, message):
    progress = ProgressDialog(parent, title, message)
    progress.show()

    def on_timeout():
        try:
            success = function()
            if not success:
                progress.show_error("Operation failed")
            progress.finished.emit(success)
        except Exception as e:
            progress.show_error(str(e))
            progress.finished.emit(False)
        finally:
            progress.close()

    QTimer.singleShot(100, on_timeout)
    return progress.exec_()

def create_scrollable_group(title, options, layout_type="vertical"):
    # ...existing code...
    for option in options:
        checkbox = QCheckBox(option)
        checkbox.setMinimumHeight(32)
        if option in FUNCTION_MAPPING:
            checkbox.stateChanged.connect(
                lambda state, opt=option, fn=FUNCTION_MAPPING[option], cb=checkbox:
                handle_checkbox_change(state, opt, fn, cb)
            )
        layout.addWidget(checkbox)
    # ...existing code...

def handle_checkbox_change(state, option, function, checkbox):
    if state:
        success = execute_with_progress(
            checkbox.window(),
            function,
            "Processing",
            f"Applying: {option}..."
        )
        if not success:
            checkbox.setChecked(False)

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
    
def create_scrollable_group(title, options, layout_type="vertical"):
    group = QGroupBox(title)
    
    # Create scroll area
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setFrameShape(QFrame.NoFrame)
    
    # Create content widget
    content = QWidget()
    
    # Create layout for content
    if layout_type == "vertical":
        content_layout = QVBoxLayout()
    else:
        content_layout = QHBoxLayout()
    content_layout.setSpacing(12)
    
    # Add checkboxes to content layout
    for option in options:
        checkbox = QCheckBox(option)
        checkbox.setMinimumHeight(32)
        if option in FUNCTION_MAPPING:
            checkbox.stateChanged.connect(
                lambda state, fn=FUNCTION_MAPPING[option]: fn() if state else None
            )
        content_layout.addWidget(checkbox)
    
    # Set layout for content widget
    content.setLayout(content_layout)
    
    # Add content to scroll area
    scroll.setWidget(content)
    
    # Create and set layout for group
    group_layout = QVBoxLayout()
    group_layout.addWidget(scroll)
    group.setLayout(group_layout)
    
    return group