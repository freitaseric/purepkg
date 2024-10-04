import os
import sys
from datetime import datetime

from cx_Freeze import Executable, setup  # type: ignore

version_type = os.getenv("VERSION_TYPE")
now = datetime.now()
version = f"{now.year}.{now.month}.{now.day}{f"-{version_type}" if version_type != None else ""}"

build_exe_options = {
  "packages": ["os"],
  "excludes": [],
  "include_files": []
}

base = None
if sys.platform == "win32":
  base = "Console"

setup(
  name = "purepkg",
  version = version,
  description = "A simple and fast universal package manager.",
  options = {"build_exe": build_exe_options},
  executables = [Executable("src/purepkg.py", base=base)]
)
