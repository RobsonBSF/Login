import PySimpleGUI as sg
from time import sleep

sg.theme('DarkAmber')

layout = [
    [sg.Text(size=34)],
    [sg.Text('Usuário', 7), sg.Input(size=27)],
    [sg.Text('Senha', 7), sg.Input(size=27, password_char="*")],
    [sg.Text()],
    [sg.Button('Novo Usuário'),sg.Button('Login'), sg.Button('Sair')]
]

Window01 = sg.Window('Login Screen', layout)

while True:
    # <<< inicializar janela >>>
    event, value = Window01.read()

    # <<< sair da tela >>>
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    # <<< cadastrar novo usuário >>>
    elif event == 'Novo Usuário':
        nome = value[0]
        senha = value[1]
        registro = nome + '-' + senha + '\n'

        with open('Usuarios.txt', 'r') as arquivo:

            if registro not in arquivo.readlines():

                with open('Usuarios.txt', 'a') as arquivo2:
                    arquivo2.write(registro)
                    sg.popup_quick_message('Cadastrando usuário...', auto_close_duration=2)
                    sleep(2)
                    sg.popup_quick_message('Usuário Cadastrado com sucesso!', auto_close_duration=2)
            else:
                sg.popup_quick_message('Usuário já Cadastrado!', auto_close_duration=2)
    
    # <<< Login >>>
    elif event == 'Login':
        nome = value[0]
        senha = value[1]
        registro = nome + '-' + senha + '\n'

        with open('Usuarios.txt', 'r') as arquivo:

            if registro in arquivo.readlines():
                sg.popup_quick_message('Login Realizado Com Sucesso!', auto_close_duration=2)
            
            else:
                sg.popup_quick_message('Usuário não Cadastrado', auto_close_duration=2)
