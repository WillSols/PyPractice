import os


nome_arquivo = "funcionarios.txt"
funcionario = {"Nome":"","CPF":0,"Telefone":0}



def IsNum(text):
    x = False
    valor = 0
    while True:
        n = str(input(text))
        if n.isnumeric():
            valor = str(n)
            x = True
        else:
            print("Valor inválido")
        if x:
             break
    return valor

def IsAlpha(text):
    t = False
    value = 0
    while True:
        n = str(input(text))
        if n.isalpha():
            value = str(n)
            t = True
        else:
            print("Valor inválido")
        if t:
            break
    return value

if not os.path.exists(nome_arquivo):
    arquivo_cadastro = open(nome_arquivo, "w+t")
    arquivo_cadastro.close()

def salvar_funcionario(funcionario):
    arquivo_cadastro = open(nome_arquivo, "r")
    posiçao_funcionario = arquivo_cadastro.read().count("funcionario")+1
    arquivo_cadastro.close()

    arquivo_cadastro = open(nome_arquivo, "a+t")
    arquivo_cadastro.write("\nfuncionarios" + str(posiçao_funcionario) + "\n")
    
    for chave in funcionario:
        arquivo_cadastro = open(nome_arquivo, "a+t")
        arquivo_cadastro.write(" " + chave + ": " + funcionario[chave])
    arquivo_cadastro.close()

while True:
    print('Escolha uma operação: ')
    print('1 - Cadastrar funcionário')
    print('2 - Consultar ( nome, idade, cpf, telefone)')
    print('3 - Relatório de idades')
    print('4 - Finalizar Programa')

    op = int(input('Escolha uma operação: ')) 

    if op == 1:

        funcionario["Nome"] = IsAlpha("Digite o nome do funcionário:")
        funcionario["Idade"] = IsNum("Digite a idade do funcionário:")
        funcionario["CPF"] = IsNum("Digite o CPF do funcionário:")
        funcionario["Telefone"] = IsNum("Digite o telefone do funcionário:")


        salvar_funcionario(funcionario)

    elif op == 2:
        y = str(input("Digite o CPF:"))
        with open("funcionarios.txt", 'r') as f:
            for line in f:
                if y  in line:
                    print(line)

    elif op == 3:
        Idade = str(input("Insira da Idade desejada:")) 
        count = 0
        with open("funcionarios.txt", 'r') as f:
            for lines in f:
                if Idade in lines:
                    print(lines)
                else:
                    pass
        with open("funcionarios.txt", 'r') as f:  
            for lines in f:
                if Idade in lines:
                    count =+ len(Idade)
                    print("Numero de pessoas com essa Idade:", count)
                else:
                    pass
       
    elif op == 4:
        break 
