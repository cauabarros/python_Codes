import tkinter as tk
from tkinter import messagebox

def verificar_login():
    if usuario.get() == 'admin' and senha.get() == 'senha':
        messagebox.showinfo('Login', 'Login realizado com sucesso!')
    else:
        messagebox.showerror('Erro', 'Usuário ou senha incorretos.')

janela = tk.Tk()
janela.title('Login')

usuario = tk.Entry(janela)
usuario.pack()

senha = tk.Entry(janela, show='*')
senha.pack()

botao = tk.Button(janela, text='Login', command=verificar_login)
botao.pack()

janela.mainloop()