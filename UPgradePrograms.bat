@echo off

PowerShell -Command "Start-Process cmd -ArgumentList '/k winget upgrade' -Verb runAS "