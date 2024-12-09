import sys
import os
from shutil import copy

argv = sys.argv
argc = len(sys.argv)
projectName: list[str]
tempPath = "cpp-init-templates"

if (argc == 1):
    print("Missing params: Project-Name")
    sys.exit(1)
else:
    argv.pop(0)
    projectName = '-'.join(argv)
    print(f"Project Name: {projectName}")

try:
    os.mkdir(projectName)
    print(f"Created Directory: {projectName}")
except PermissionError as permE:
    print(f"Permission error: {permE}")

try:
    os.mkdir(f"{projectName}\\src")
    print(f"Created Directory: {projectName}\\src")
except PermissionError as permE:
    print(f"Permission error: {permE}")

copy(f"{tempPath}\\main-t.txt",f"{projectName}\\src\\main.cpp")
copy(f"{tempPath}\\conanfile-t.txt", f"{projectName}\\conanfile.txt")
copy(f"{tempPath}\\mesonbuild-t.txt", f"{projectName}\\meson.build")

try: 
    os.system(f"powershell.exe cd .\\{projectName}\\; conan install . --output-folder=build --build=meson; cd .\\build\\; meson setup --native-file conan_meson_native.ini .. meson-src; meson compile -C .\\meson-src\\")
except PermissionError as permE:
    print(f"Permission error: {permE}")