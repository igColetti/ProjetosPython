import PySimpleGUI as sg
import back

sg.theme('LIGHTGREY1')

menu_def = [
    ['Pessoa', ['Cadastrar', 'Editar']],
    ['Ajuda', 'Sobre'],
]

layout = [
    [sg.Menu(menu_def)],
    [sg.Image(filename='logo.png')]
]

telaCadastroAtiva = False
telaEditarAtiva = False
telaSobreAtiva = False

window = sg.Window('Tela Inicial', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Cadastrar' and not telaCadastroAtiva:
        telaCadastroAtiva = True
        window.hide()
        
        estados = [
        'Acre',
        'Alagoas',
        'Amapá',
        'Amazonas',
        'Bahia',
        'Ceará',
        'Distrito Federal',
        'Espírito Santo',
        'Goiás',
        'Maranhão',
        'Mato Grosso',
        'Mato Grosso do Sul',
        'Minas Gerais',
        'Pará',
        'Paraíba',
        'Paraná',
        'Pernambuco',
        'Piauí',
        'Rio de Janeiro',
        'Rio Grande do Norte',
        'Rio Grande do Sul',
        'Rondônia',
        'Roraima',
        'Santa Catarina',
        'São Paulo',
        'Sergipe',
        'Tocantins'
        ]
        
        layoutCadastro = [
            [sg.Column([[sg.Text('Cadastro de pessoas', size=(17, 1), font=('Helvetica', 18))]], justification='center')],
            [sg.Text('CPF:', size=(5, 1), font=('Helvetica', 11)), sg.InputText(key='input_cpf', size=(20), font=('Helvetica', 11)),
            sg.Text('Nome:', size=(5, 1), font=('Helvetica', 11)), sg.InputText(key='input_nome', size=(40), font=('Helvetica', 11))],
            [sg.Text('Endereço:', size=(7, 1), font=('Helvetica', 11)), sg.InputText(key='input_endereco', size=(67), font=('Helvetica', 11))],
            [sg.Text('Cidade:', size=(7, 1), font=('Helvetica', 11)), sg.InputText(key='input_cidade', size=(30), font=('Helvetica', 11)),
            sg.Text('Estado:', size=(7, 1), font=('Helvetica', 11)), sg.Combo(values=estados, k='-COMBO-', size=(23, 1), font=('Helvetica', 11))],
            [sg.Frame('Sexo', [
                [sg.Radio('Feminino', 'grupo', key='-FEMININO-', font=('Helvetica', 11)), sg.Radio('Masculino', 'grupo', key='-MASCULINO-', font=('Helvetica', 11))],
            ])],
            [sg.Text('E-mail:', size=(5, 1), font=('Helvetica', 11)), sg.InputText(key='input_email', size=(30), font=('Helvetica', 11)),
            sg.Text('Data de nascimento:', size=(15, 1), font=('Helvetica', 11)), sg.InputText(key='input_dataNascimento', size=(15), font=('Helvetica', 11))],
            [sg.Text('Observações', size=(10, 1), font=('Helvetica', 11))],
            [sg.Multiline(size=(60, 6), key='input_observacoes', font=('Helvetica', 11))],
            [sg.Column([[sg.Button('Cadastrar', size=(10, 2), key='btnCadastrar', font=('Helvetica', 11))]], justification='center')]
        ]

        cadastro = sg.Window('Tela de Cadastros', layoutCadastro)


        while True:
            event, values = cadastro.read()
            
            if event == 'btnCadastrar':
                cpf = values['input_cpf']
                nome = values['input_nome']
                endereco = values['input_endereco']
                cidade = values['input_cidade']
                estado = values['-COMBO-']
                if values['-FEMININO-']:
                    sexo = 'Feminino'
                elif values['-MASCULINO-']:
                    sexo = 'Masculino'
                else:
                    sexo = 'Não informado'
                email = values['input_email']
                dtaNascimento = values['input_dataNascimento']
                obs = values['input_observacoes']
                
                back.adicionarPessoa(nome, cpf, endereco,cidade,estado,sexo,email,dtaNascimento,obs)
                
                layoutOK = [
                    [sg.Column([[sg.Text('Cadastro realizado com sucesso!!', size=(30, 1), font=('Helvetica', 12))]], justification='center')],
                    [sg.Column([[sg.Button('OK', size=(10, 2), key='btnOK', font=('Helvetica', 11))]], justification='center')]
                ]
                
                telaOK = sg.Window('Confirmação Cadastro', layoutOK)
                while True:
                    eventOK, valuesOK = telaOK.read()
                    
                    if eventOK == 'btnOK' or eventOK == sg.WINDOW_CLOSED:
                        telaOK.close()
                        cadastro.close()
                        telaCadastroAtiva = False
                        break
                

            if event == sg.WINDOW_CLOSED or event == 'Exit':
                cadastro.close()
                telaCadastroAtiva = False  # Reinicializa a variável para permitir a abertura da janela novamente
                window.un_hide()
                break

    if event == 'Editar' and not telaEditarAtiva:
        telaEditarAtiva = True
        window.hide()
        
        cabecalho = ['CPF', 'NOME', 'ENDERECO', 'CIDADE', 'ESTADO', 'SEXO', 'EMAIL', 'DATA DE NASCIMENTO', 'OBSERVACOES']
        
        dados = back.listaPessoas()
        
        print(dados)
        
        layoutEdicao = [
            [sg.Column([[sg.Text('Pessoas cadastradas', size=(17, 1), font=('Helvetica', 12))]], justification='center')],
            [sg.Table(values = dados[0:][:], headings = cabecalho, 
                      max_col_width=50, 
                      auto_size_columns = True,
                      display_row_numbers = True, 
                      enable_events = True,
                      key = '-TABLE-')],
            [sg.Column([[sg.Button('Remover', size=(10, 2), key='btnRemover')]], justification='center')],
        ]

        edicao = sg.Window('Lista das Pessoas Cadastradas', layoutEdicao)
        
        while True:
            event, values = edicao.read()
            
            if event == 'btnRemover':
                if dados:
                                        
                    if values['-TABLE-']:
                        indice_linha_selecionada = values['-TABLE-'][0]
                        
                        registro_selecionado = dados[indice_linha_selecionada]
                        
                        cpf = registro_selecionado[1]
                        
                        back.excluirPessoa(cpf)
                        
                        dados.remove(registro_selecionado)
                        
                        edicao['-TABLE-'].update(values=dados)
                        
                        
                    
            
            if event == sg.WINDOW_CLOSED or event =='Exit':
                edicao.close()
                telaEditarAtiva = False
                window.un_hide()
                break

    if event == 'Sobre' and not telaSobreAtiva:
        telaSobreAtiva = True
        window.hide()
        
        # Criar a lista com as informações
        informacoes = [
            {
                'Nome': 'Igor Faria Coletti',
                'Formação': 'Cursando Engenharia de Software',
                'Cargo': 'Desenvolvedor Junior',
                'Local de Trabalho': 'Agilizae Tecnologia',
                'Área de Atuação': 'Desenvolvimento'
            },
            {
                'Nome': 'Gabriel Moura',
                'Formação': 'Cursando Engenharia de Software',
                'Cargo': 'Desempregado',
                'Local de Trabalho': 'CASA',
                'Área de Atuação': 'DORMIR'
            },
            {
                'Nome': 'Pedro Sales',
                'Formação': 'Cursando Engenharia de Software',
                'Cargo': 'Acho que é Gerente',
                'Local de Trabalho': 'MeliControl',
                'Área de Atuação': 'Não sei'
            }
        ]
        
        layout = [
            [sg.Text('Criadores do projeto')]
        ]

        for informacao in informacoes:
            dados = [[f'{chave}: {valor}'] for chave, valor in informacao.items()]
            layout.append([sg.Listbox(values=dados, size=(40, 5), enable_events=False)])
            

        sobre = sg.Window('Tela de Cadastros', layout)
        
        
        
        while True:
            event, values = sobre.read()
            
            if event == sg.WINDOW_CLOSED or event =='Exit':
                sobre.close()
                telaSobreAtiva = False
                window.un_hide()
                break

window.close()
