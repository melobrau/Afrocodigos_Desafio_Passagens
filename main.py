from passagens import PassagensAereasManager

from menu import mostra_menu


while True:

    passagens_aereas_manager = PassagensAereasManager()

    #MOSTRAR O MENU
    mostra_menu()

    entrada_do_usuario = int(input())
    #RECEBER ENTRADA DO USUARIO
    if entrada_do_usuario == 1:
        print("Voce escolheu comprar passagens")
        print("Digite o destino da sua viagem:")
        print("digite agora o local de partida:")
        print("Digite o valor da sua passagem:")

    elif entrada_do_usuario == 2:
        print("Segue abaixo uma lista das suas passagens:")
        print(passagens_aereas_manager.passagens_compradas)

    #EM CASO DE ENTRADA INVALIDA
#   if  entrada_do_usuario != [1,2,3]:
#      print("Não entendi! Você deve digitar uma das opções 1, 2 ou 3!")
    #SAIDA DO PROGRAMA
    elif entrada_do_usuario == 3:
        print("Encerrando o programa. Valeu! Volte sempre!")
    break