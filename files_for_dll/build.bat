@echo off
setlocal

REM Ruta a tu g++
set "GPP=C:\mingw64\bin\g++.exe"

REM Crear carpeta de build si no existe (en main/build)
if not exist ..\main\build mkdir ..\main\build

REM Compilar la DLL en main/build
%GPP% -shared -o ..\main\build\list.dll ^
List.cpp listpy.cpp Node.cpp ^
-static-libgcc -static-libstdc++ -Wl,--out-implib,..\main\build\liblist.a

if errorlevel 1 (
    echo ❌ Build failed.
    exit /b 1
)

echo ✅ Built: ..\main\build\list.dll
endlocal
