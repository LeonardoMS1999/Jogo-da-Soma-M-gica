mensagemPositiva = "Soma Mágica! Dois números somados dão o terceiro."
mensagemNegativa = "Não foi dessa vez."

entrada1 = int(input("Digite um numero :"))
entrada2 = int(input("Digite um numero :"))
entrada3 = int(input("Digite um numero :"))

listaNumeros = [entrada1,entrada2,entrada3]
listaNumeros.sort()

if listaNumeros[0] + listaNumeros[1] == listaNumeros[2]:
    print(mensagemPositiva)
else:
    print(mensagemNegativa)