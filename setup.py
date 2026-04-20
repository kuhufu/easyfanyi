#!/usr/bin/env python3
"""
EasyFanyi Setup Script
Installs the translation tool and configures shell aliases.
"""

import sys
import os
import shutil
from pathlib import Path


def alias_conf(filepath: str, line: str) -> None:
    """Add an alias configuration line to the specified file.
    
    Args:
        filepath: Path to the configuration file (e.g., .bashrc)
        line: The alias line to add
    """
    with open(filepath, 'at', encoding='utf-8') as out:
        out.write('\n# easyfanyi')
        out.write('\n' + line)


def copy_dir(src: str, dest: str) -> None:
    """Copy directory from source to destination.
    
    Args:
        src: Source directory path
        dest: Destination directory path
    """
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main() -> int:
    """Main entry point for the setup script.
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    if len(sys.argv) < 2:
        print("Usage: sudo python3 setup.py <username>")
        print("Example: sudo python3 setup.py $USER")
        return 1
    
    user = sys.argv[1]
    src_dir = Path(__file__).parent / 'dic'
    dest_dir = Path('/opt/easyfanyi')
    bashrc_path = Path.home() / user / '.bashrc' if user != '$USER' else Path.home() / '.bashrc'
    
    # Handle $USER variable
    if user == '$USER':
        bashrc_path = Path.home() / '.bashrc'
    else:
        bashrc_path = Path(f'/home/{user}/.bashrc')
    
    try:
        # Copy dictionary files
        copy_dir(str(src_dir), str(dest_dir))
        print(f"✓ Copied {src_dir} to {dest_dir}")
        
        # Add alias to bashrc
        alias_line = "alias dic='python3 /opt/easyfanyi/dic-youdao.py'"
        alias_conf(str(bashrc_path), alias_line)
        print(f"✓ Added alias to {bashrc_path}")
        
        print("\nSetup completed successfully!")
        print("Please restart your terminal or run: source ~/.bashrc")
        return 0
        
    except PermissionError as e:
        print(f"Error: Permission denied. Please run with sudo.")
        print(f"Details: {e}")
        return 1
    except Exception as e:
        print(f"Error during setup: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
