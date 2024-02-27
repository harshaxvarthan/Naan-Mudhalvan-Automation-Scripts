@echo off
setlocal

rem Set the Python version you want to install
set PYTHON_VERSION=3.12.2

rem Set the installation directory
set INSTALL_DIR=C:\Python39

rem Set the download URL for the Python installer
set DOWNLOAD_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

rem Create a temporary directory for downloading the installer
set TEMP_DIR=%TEMP%\PythonInstaller
mkdir %TEMP_DIR%
cd %TEMP_DIR%

rem Download the Python installer
curl -o python_installer.exe %DOWNLOAD_URL%

rem Install Python silently
python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

rem Clean up temporary files
cd ..
rmdir /s /q %TEMP_DIR%

echo Python %PYTHON_VERSION% has been successfully installed to %INSTALL_DIR%

rem Install Selenium using pip
echo Installing Selenium...
%INSTALL_DIR%\Scripts\pip install selenium

echo Selenium has been successfully installed.

endlocal
