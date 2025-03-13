@echo off
This will restore the health of the windows

PowerShell -Command "Start-Process cmd -ArgumentList '/k DISM /Online /Cleanup-Image /RestoreHealth' -Verb runAS"


