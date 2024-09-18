# -*- coding: utf-8 -*-
"""desafio_classes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WUTl4mguw7Y2OFL3_0jbpStjgxpopbgb
"""

from abc import ABC, abstractclassmethod, abstractproperty

class Cliente():
  def __init__(self, endereco, contas):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    self.transacao(conta)

  def adicionar_conta(self, conta):
    self.contas.append(conta)

class PessoaFisica(Cliente):
  def __init__(self, cpf, nome, data_nascimento):
    super.__init__(endereco, contas)
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf = cpf

class Conta():
  def __init__(self, saldo, numero, agencia, cliente, historico):
    self._saldo = 0
    self._numero = numero
    self._agencia = 1092
    self._cliente = cliente
    self._historico = Historico()
    self.nmr_saque = 0
  @classmethod
  def nova_conta(cls, conta, numero):
    return cls(conta, numero)

  def saldo(self):
    return self.saldo

  @property
  def numero(self):
      return self._numero

  @property
  def agencia(self):
      return self._agencia

  @property
  def cliente(self):
      return self._cliente

  @property
  def historico(self):
      return self._historico

  def sacar(self, valor):
    if valor > self._saldo:
      print("Você não tem saldo para essa operação.")
    elif valor > 0:
      print("Operação realizada com sucesso.")
      self.nmr_saque += 1
    else:
      print("Valor inválido.")

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print("Operação realizada com sucesso.")
    else:
      print("Valor inválido.")

class ContaCorrente(Conta):
  def __init__(self, limite, limite_saques):
    super().__init__(saldo, numero, agencia, cliente, historico)
    self._limite = 1000
    self._limite_saques = 4

  def sacar(self, valor):
    if self.nmr_saque > self._limite_saques:
      print("Você excedeu o número de saques por hoje.")
    elif valor > self._limite:
      print("Você execeu o limite de saques.")
    else:
      return super().sacar(valor)

  def __str__(self):
    return f"""\
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
    """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)