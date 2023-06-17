from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#1C1C1D")
        self.root.geometry("700x500")
        self.root.resizable(False, False)


Application()

