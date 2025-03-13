import tkinter as tk
from tkinter import ttk
import os

def aplicar_estilo():
    style = ttk.Style()

    # Configuração de um estilo para o botão
    style.configure('TButton',
                    background='blue',
                    foreground='red',
                    font=('Arial', 14, 'bold'),
                    padding=3)

    # Configuração de um estilo para o Label
    style.configure('TLabel',
                    background='lightgray',
                    foreground='black',
                    font=('Arial', 12),
                    padding=5)

def DNScleaning():
    os.startfile(r"MultiFuncTool\Tools\DNSoptmizer.bat")

def upgrade_programs():
    os.startfile(r"MultiFuncTool\Tools\UPgradePrograms.bat")

def check_win_health():
    os.startfile(r"MultiFuncTool\Tools\CheckWinHealth.bat")

def Restore_win_health():
    os.startfile(r"MultiFuncTool\Tools\RestoreWinHealth.bat")

def sfc_scannow():
    os.startfile(r"MultiFuncTool\Tools\scannow.bat")


ToolWindow = tk.Tk()
ToolWindow.title("Tool Window")
ToolWindow.config(bg='black')
ToolWindow.geometry("400x600")
ToolWindow.resizable(width=False, height=False)



ToolWindow.grid_rowconfigure(0, weight=1)
ToolWindow.grid_rowconfigure(1, weight=1)
ToolWindow.grid_rowconfigure(2, weight=1)
ToolWindow.grid_rowconfigure(3, weight=1)
ToolWindow.grid_rowconfigure(4, weight=1)
ToolWindow.grid_rowconfigure(5, weight=1)


ToolWindow.grid_columnconfigure(0, weight=1)
ToolWindow.grid_columnconfigure(1, weight=2)
ToolWindow.grid_columnconfigure(2, weight=1)




dns_button = ttk.Button(ToolWindow, text='DNSoptimize', command=DNScleaning, style='TButton')
dns_button.grid(row=1, column=1, pady=20, sticky="ew")

upgrade_button = ttk.Button(ToolWindow, text='Upgrade Programs', command=upgrade_programs, style='TButton')
upgrade_button.grid(row=2, column=1, pady=20, sticky="ew")

CWH = ttk.Button(ToolWindow, text='CheckWinHealth', command=check_win_health, style='TButton')
CWH.grid(row=3, column=1, pady=20, sticky="ew")

RWH = ttk.Button(ToolWindow, text='RestoreWinHealth', command=Restore_win_health, style="TButton")
RWH.grid(row=4, column=1, pady=20, sticky="ew")

sfc = ttk.Button(ToolWindow, text='SFC/scannow', command=sfc_scannow, style='TButton')
sfc.grid(row=5, column=1, pady=20, sticky="ew")


ToolWindow.mainloop()
