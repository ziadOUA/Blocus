@echo off
pyinstaller blocus.py --windowed -i "blocus_icon.ico"
echo Finished building the program
Xcopy res dist\blocus\res /E /I
Xcopy standard dist\blocus\standard /E /I
echo Finished copying the necessary files
pause