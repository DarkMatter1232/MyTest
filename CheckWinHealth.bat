@echo off

PowerShell -Command "Start-Process cmd -ArgumentList '/k DISM /Online /Cleanup-Image /CheckHealth' -Verb runAs"
