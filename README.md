# cpp-init-windows
cpp program for creating project templates and automatically installing dependencies using conan and meson

# Dependencies
- scoop (package manager for windows)
- conan
- meson
- cmake
- pkg-config
- ninja
- python (recommended but optional)

install scoop using powershell
```pwsh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

install all dependencies
```pwsh
scoop install main/conan
scoop install main/meson
scoop install main/cmake
scoop install main/pkg-config
scoop install main/ninja
scoop install main/python
```

# Usage

run cpp-init through console

```pwsh
.\cpp-init Project-Name
```