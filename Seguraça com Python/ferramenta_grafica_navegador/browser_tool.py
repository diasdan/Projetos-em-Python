import webbrowser
from tkinter import *

root = Tk( ) #representa a tela

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=2030)
root.mainloop()



