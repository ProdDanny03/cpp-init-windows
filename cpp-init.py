import sys
import os
from shutil import copy
from subprocess import run, CalledProcessError

projectName: list[str]
tempPath = "cpp-init-templates"

if len(sys.argv) == 1:
    print("Missing params: Project-Name")
    sys.exit(1)

projectName = '-'.join(sys.argv[1:])
print(f"Project Name: {projectName}")

directories = [projectName, os.path.join(projectName, "src")]
for directory in directories:
    try:
        os.mkdir(directory)
        print(f"Created Directory: {directory}")
    except PermissionError as permE:
        print(f"Permission error: {permE}")

files_to_copy = [
    ("main-t.txt", "src/main.cpp"),
    ("conanfile-t.txt", "conanfile.txt"),
    ("mesonbuild-t.txt", "meson.build")
]

for src, dest in files_to_copy:
    copy(os.path.join(tempPath, src), os.path.join(projectName, dest))

try:
    run([
        "powershell.exe",
        f"cd .\\{projectName}\\; conan install . --output-folder=build --build=meson; cd .\\build\\; meson setup --native-file conan_meson_native.ini .. meson-src; meson compile -C .\\meson-src\\"
    ], check=True, shell=True)
except (PermissionError, CalledProcessError) as e:
    print(f"Error: {e}")
