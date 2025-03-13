@echo off

:: Abrir o CMD como administrador e executar o comando SFC /scannow
PowerShell -Command "Start-Process cmd -ArgumentList '/k SFC /scannow && exit' -Verb runAs"
