from PySimpleGUI import PySimpleGUI as sg 

# Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entar')]
]  # The closing square bracket is added here

# Janela
janela = sg.Window('Tela de Login', layout)
# Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entar':
        print(valores['usuario'])
        print(valores['senha'])
        print(valores['Salvar o login'])

        
