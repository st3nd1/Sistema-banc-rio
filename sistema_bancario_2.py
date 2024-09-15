# -*- coding: utf-8 -*-
"""estudos_python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bAQc5YB-_Sxx6Ak-meHgdIASf1gmXgOB
"""

def saque(*, saldo, valor, numero_saque, limite_saque):
  if numero_saque > limite_saque:
    print(f"Você excedeu o limite de saques diários.")
  else:
    if valor > saldo:
      print(f"Você não tem saldo para essa operação.\nSeu saldo é de: {saldo}.")
    else:
      saldo -= valor
      print(f"Operação realizada com sucesso.\nSeu novo saldo é de: {saldo}.")

def deposito(saldo, valor, /):
  saldo += valor
  print(f"Operação realizada com sucesso.\nSeu novo saldo é de: {saldo}")
  return saldo

def extrato(inicio = "datetime.today()", fim = "datetime.today()", /, *, saldo, saques, depositos, escolha):
  from datetime import datetime
  import random
  if escolha == 1:
    inicio = datetime.today()
    data_formatada = inicio.strftime('%d/%m/%Y')
    print(f"Saldo em {data_formatada}: R${saldo}")
    print(f"(+) Total de entradas (entradas) no período: R${depositos}")
    print(f"(-) Total de saques (saídas) no período: R${saques}")
    print(f"Saldo final em {data_formatada}: R${saldo + depositos - saques}")
  else:
    inicio_transformado = datetime.strptime(inicio, '%d/%m/%Y')
    fim_transformado = datetime.strptime(fim, '%d/%m/%Y')
    inicio_formatado = inicio_transformado.strftime('%d/%m/%Y')
    fim_formatado = fim_transformado.strftime('%d/%m/%Y')
    SI_random = random.randint(1, 1000)
    DP_random = random.randint(1, 1000)
    SQ_random = random.randint(1, 500)
    print(f"Saldo em {inicio_formatado}: R${SI_random}")
    print(f"(+) Total de entradas (entradas) no período: R${DP_random}")
    print(f"(-) Total de saques (saídas) no período: R${SQ_random}")
    print(f"Saldo em {fim_formatado}: R${SI_random + DP_random - SQ_random}")

def cadastro_cliente(name, born, CPF, address, memoria):
    CPF = CPF.strip()
    if CPF in memoria:
        print("Já há um cliente com esse CPF cadastrado.")
    else:
        info = [name, born, address]
        memoria[CPF] = info
        print("Cliente cadastrado com sucesso.")



def cadastro_conta(agencia, numero_conta, cpf, contas):
  nova_conta = (agencia, numero_conta)
  if cpf in contas:
      if nova_conta in contas[cpf]:
          return print("Essa conta já está cadastrada para este CPF.")
      else:
          contas[cpf].append(nova_conta)
          return print("Conta cadastrada com sucesso!")
  else:
      contas[cpf] = [nova_conta]
      return print("Conta cadastrada com sucesso!")

def consulta(CPF, clientes, contas):
  if CPF in contas:
    print(f"Foram encontradas as seguintes contas nesse CPF: {contas[CPF]}")
  else:
    print(f"Não foram encontradas contas nesse CPF.")

def sistema_bancario():
  import random
  start_balance = bank_balance = random.randint(1, 1000)
  lim_saque = 2
  saidas = entradas = num_saque = 0
  banco_de_clientes = {}
  banco_de_contas = {}

  while True:
    print("Menu Inicial:\n1 - Já é cliente\n2 - Não é cliente\n3 - Encerrar")
    resposta_1 = int(input("Sua resposta: "))

    while resposta_1 == 1:
      print("1 - Saque\n2 - Deposito\n3 - Extrato\n4 - Encerrar")
      resposta_2 = int(input("Sua resposta: "))

      if resposta_2 == 1:
        print(f"Saldo inicial: {bank_balance}")
        withdrawal = int(input("Informe o valor: R$"))
        num_saque += 1
        if withdrawal <= bank_balance:
          saidas += withdrawal
        saque(saldo=bank_balance, valor=withdrawal, numero_saque=num_saque, limite_saque=lim_saque)
        if withdrawal <= bank_balance:
          bank_balance -= withdrawal
      elif resposta_2 == 2:
        print(f"Saldo inicial: {bank_balance}")
        deposit = int(input("Informe o valor do deposito: R$"))
        entradas += deposit
        deposito(bank_balance, deposit)
      elif resposta_2 == 3:
        print("1 - Extrato do dia\n2 - Outra data")
        resposta_3 = int(input("Sua resposta: "))
        if resposta_3 == 2:
          start = str(input("Informe o inicio do período: "))
          end = str(input("Informe o final do período: "))
          extrato(start, end, saldo=start_balance, saques=saidas,depositos=entradas, escolha=resposta_3)
        else:
          extrato(saldo=start_balance, saques=saidas,depositos=entradas, escolha=resposta_3)
      else:
        break

    while resposta_1 == 2:
      print('1 - Cadastrar cliente\n2 - Cadastrar conta corrente\n3 - Consultar cliente\n4 - Encerrar')
      resposta_4 = int(input("Sua resposta: "))

      if resposta_4 == 1:
        nome = str(input("Informe o nome: "))
        nasc = str(input("Informe a data de nascimento (DD/MM/AAAA): "))
        cpf = str(input("Informe o CPF: "))
        endereço = str(input("Informe o endereço: "))
        cadastro_cliente(name=nome, born=nasc, address=endereço, CPF=cpf, memoria=banco_de_clientes)
      elif resposta_4 == 2:
        agencia = int(input("Informe uma agência: "))
        num_conta = int(input("Informe o número da conta: "))
        cadastro_pessoa_fisica = int(input("Informe o CPF para está conta: "))
        cadastro_conta(agencia= agencia, numero_conta= num_conta, cpf= cadastro_pessoa_fisica, contas=banco_de_contas)
      elif resposta_4 == 3:
        cpf = int(input("Informe o CPF: "))
        consulta(CPF=cpf, clientes=banco_de_clientes, contas=banco_de_contas)
      else:
        break
    if resposta_1 == 3:
      break

sistema_bancario()