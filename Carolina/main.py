from carolina import *

if __name__ == "__main__":
    g = Gerente("Alexandre","123123", 1231231)
    print(g)
    if g.autenticar("123123", 1231231):
        print(g.cancelar_operacao())
    else:
        print("falha de autenticação")

    op = Operador_Caixa("Biggas","2233333", 43332, 1)
    print(op)
    if op.autenticar("1",43332):
        print(op.registrar_produto())
    else:
        print("falha de autenticação")

    s = Segurança("Carlos", "12415662", 52132451, 34)
    print(s)
    if s.autenticar("34",52132451):
        print(s.acionar_alarme())
    else:
        print("falha de autenticação")
