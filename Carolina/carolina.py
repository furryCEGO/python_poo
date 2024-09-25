from abc import ABC, abstractmethod
import hashlib

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : int

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    def __str__(self):
        info = f"Nome: {self.nome}\n CPF: {self.cpf}\n"
        return info

    def get_senha(self):
        return self.__senha
    @abstractmethod
    def autenticar(self, user: str, senha: int):
        if user == self.cpf and self.get_senha() == senha:
            return True
        else:
            return False

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if user == self.cpf and self.get_senha() == senha:
            return True
        else:
            return False
    def cancelar_operacao(self):
        return "Operação Cancelada!"

class Operador_Caixa(Funcionario):
    numero_caixa : int

    def __init__(self, nome, cpf, senha, numero_caixa):
        super().__init__(nome,cpf,senha)
        self.numero_caixa = numero_caixa

    def autenticar(self, user: str, senha: int):
        if user == str(self.numero_caixa) and self.get_senha() == senha:
            return True
        else:
            return False

    def registrar_produto(self):
        return "Produto Registrado!"
class Segurança(Funcionario):
    posto : int

    def __init__(self, nome, cpf, senha, posto):
        super().__init__(nome,cpf,senha)
        self.posto = posto

    def autenticar(self, user: str, senha: int):
        if user == str(self.posto) and self.get_senha() == senha:
            return True
        else:
            return False

    def acionar_alarme(self):
        return "UOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOU"
