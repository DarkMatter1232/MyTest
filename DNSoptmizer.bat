@echo off
:: Abrir o CMD como administrador e executar os comandos dentro do CMD
PowerShell -Command "Start-Process cmd -ArgumentList '/c ipconfig /flushdns && ipconfig /release && ipconfig /renew && exit' -Verb runAs"
