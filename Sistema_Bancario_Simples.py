menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair 

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIA = 3

while True:

    opcao = input(menu)

    if opcao == "1":
       valor_deposito = float(input("Digite o valor do depósito: "))

       if valor_deposito > 0:
           saldo += valor_deposito
           extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

       else:
           print("Operação falhou! O valor informado é inválido.")   

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques_dia = numero_saques >= LIMITE_SAQUES_DIA

        if excedeu_saldo:
            print("Operação inválida, saldo insuficiente!")

        elif excedeu_limite:
            print("Operação inválida, o saque excede o limite!")  

        elif excedeu_saques_dia:
            print("Operação inválida, quantidade de saques diários excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou, o valor informado é inválido!")
      
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor preencha novamente com a operação desejada!")         