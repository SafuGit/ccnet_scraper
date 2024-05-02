import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"  # Use this option to create a GUI executable on Windows

executables = [Executable("main.py", base=base)]

options = {
    "build_exe": {
        "packages": ['townscraper', 'bs4', 'selenium', 'time', 'hider', 'pandas'],  # List of packages to include
        "include_files": [''],  # List of additional files to include
    },
}

setup(
    name="CCNet Scraper",
    version="1.0",
    license = 'MIT',
    author = 'Safu',
    url = 'https://github.com/SafuGit/ccnet_scraper',
    description="Scrape your towns upkeep",
    options=options,
    executables=executables
)
