import modules
import tkinter as tk
from tkinter import filedialog

# Janela para mensagem de erro
def error_window(error_message):
    error_window = tk.Toplevel()
    error_window.title("Erro")
    #error_window.iconbitmap(default="resource\erro.ico")
    error_label = tk.Label(error_window, text=error_message)
    error_label.pack(padx=30, pady=20)

window = tk.Tk()
#window.iconbitmap(default="resource\icon.ico")
window.title("Janela Principal")
window.geometry("300x300")
window.minsize(300, 200)
window.maxsize(300, 200)

# Cria o input para o caminho da pasta
label_folder_path = tk.Label(window, text="Caminho de arquivo:")
label_folder_path.pack()
entry_folder_path = tk.Entry(window)
entry_folder_path.pack()

# Cria o botão "Browse"
button_browse = tk.Button(window, text="Browse", command=modules.print_something)
button_browse.pack()

# Label do input
label_name = tk.Label(window, text="Entrada:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

# Cria o botão "Isolar"
button_isolate = tk.Button(window, text="Enviar", command=modules.print_something)
button_isolate.pack()

