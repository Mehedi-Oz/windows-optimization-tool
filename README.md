# Windows Optimization Tool

This project is a Windows optimization tool designed to provide users with a modern GUI for managing various system settings and optimizations. The application includes features for system safety, cleanup, privacy management, system tweaks, performance adjustments, bloatware removal, Windows updates, activation, and Windows Defender management.

## Project Structure

```
windows-optimization-tool
├── src
│   ├── main.py                # Main entry point of the application
│   ├── core                   # Core functionality modules
│   │   ├── __init__.py        # Marks the core directory as a package
│   │   ├── safety.py          # Functions for creating system restore points
│   │   ├── cleanup.py         # Functions for cleaning up temporary files and caches
│   │   ├── privacy.py         # Functions for managing privacy settings
│   │   ├── tweaks.py          # Functions for UI tweaks and settings
│   │   ├── performance.py      # Functions for adjusting performance settings
│   │   ├── bloatware.py       # Logic for managing bloatware applications
│   │   ├── updates.py         # Functions for managing Windows updates
│   │   ├── activation.py      # Functions for activating Windows and Office
│   │   └── defender.py        # Functions for managing Windows Defender
│   └── ui                     # UI components and themes
│       ├── __init__.py        # Marks the ui directory as a package
│       ├── themes.py          # Defines theme stylesheets for the application
│       ├── tabs.py            # Defines the layout and structure of the tabs
│       └── components          # Reusable UI components
│           ├── __init__.py    # Marks the components directory as a package
│           ├── titlebar.py     # Custom title bar for the application
│           └── widgets.py      # Reusable UI components
├── requirements.txt           # Lists dependencies required for the project
├── .gitignore                 # Specifies files and directories to ignore by Git
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd windows-optimization-tool
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python src/main.py
   ```

## Usage

- The application provides a user-friendly interface to manage various system settings.
- Navigate through the tabs to access different functionalities such as Safety, Clean Up, Privacy, Tweaks, Performance, Bloatware, Updates, Activation, and Defender.
- Each tab contains specific options and actions related to its category.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.