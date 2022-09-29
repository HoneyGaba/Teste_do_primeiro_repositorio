
#desafio 115


def titulo(msg):
    print('~'*50)
    print(f'{msg:^50}')
    print('~'*50)
    print()


def cor(c):
    c.strip().lower()
    if c == 'vermelho':
        return '\033[0;40;31m'
    elif c == 'azul':
        return '\033[0;40;34m'
    elif c == 'amarelo':
        return '\033[0;40;33m'
    elif c == 'cinza':
        return '\033[0;40;100m'
    elif c == 'verde':
        return '\033[0;40;32m'
    elif c == 'roza':
        return '\033[0;40;35m'
    elif c == 'padrao':
        return '\033[0;0;0m'
    else:
        return ''


def menu():    
    titulo('MENU PRINCIPAL')
    print(f'{cor("amarelo")}1 {cor("padrao")}- {cor("azul")}Ver pessoas cadastradas')
    print(f'{cor("amarelo")}2 {cor("padrao")}- {cor("azul")}Cadastrar nova Pessoa')
    print(f'{cor("amarelo")}3 {cor("padrao")}- {cor("azul")}Sair do sistema')
    print(f'{cor("padrao")}')
    print('~'*50)
    r = input('Sua opção: ')
    if r not in '123':
        print(f'{cor("vermelho")}ERRO! Digite uma opção válida!{cor("padrao")}\n')
        r = menu()
    elif r == '3':
        print('~'*50)
        return 'exit'
    elif r == '2':
        return 'cadastrar'
    elif r == '1':
        return 'ler'
    return r


def cadastrar():
    titulo('NOVO CADASTRO')
    nome = str(input('Nome: '))
    while True:   
        try:
            idade = int(input('Idade: '))
        except Exception as erro:
            print(erro.__class__)
            print(f'{cor("vermelho")}ERRO! Digite uma idade válida!{cor("padrao")}\n')
        else:
            break
        
    arquivo = open('cadastro.txt', 'a')
    arquivo.write(nome)
    arquivo.write(f'{idade:>35}')
    arquivo.write('\n')
    print(f'Novo registro de {nome} adicionado!')


def ler():
    titulo('LEITURA...')
    try:            
        with open('cadastro.txt', 'r') as arquivo:
            print(arquivo.read())
            '''
            for valor in arquivo:
                print(valor)'''
    except:
        print('Nenhum cadastro encontrado...')
        

def principal():
    while True:
        escolha = menu()
        if escolha == 'exit':
            print(cor('roza'))
            titulo('ATÉ MAIS, OBRIGADO!!!')
            print(cor('padrao'))
            break
        elif escolha == 'cadastrar':
            cadastrar()
        elif escolha == 'ler':
            ler()
       