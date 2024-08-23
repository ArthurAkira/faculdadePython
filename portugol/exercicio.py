#あきら
def numeroInt():
    numero = int(input("numero inteiro: ")) #var numero, dobro, terco inteiros
    dobro = numero * 2
    terco = numero / 3
    print(dobro) #Escreva dobro
    print(terco) #Escreva terco

def qtdLata():
    altura = float(input("altura: "))
    largura = float(input("largura: "))
    lata = 2
    quantidadePintada= altura * largura
    quantidadeTinta = quantidadePintada / lata
    print(quantidadePintada)
    print(quantidadeTinta)

def precoDesconto():
    preco = float(input("preco do item: "))
    precoDesc = (preco * 5) / 100
    print(precoDesc - preco)

def precoCarro():
    kmPercorrio = float(input("km percorridos pelo carro: "))
    diasAlugados = int(input("dias com o carro alugado: "))
    precoKm = kmPercorrio * 0.2
    precoDia = diasAlugados * 90
    precoTotal = precoKm + precoDia
    print(precoTotal)

def diasPerdidoFumando():
    qtdDia = int(input("quantidade de cigarro por dia: "))
    qtdAnos = int(input("quantidade de anos fumando: "))
    anoBi = int(qtdAnos / 4)
    anosNormais = qtdAnos - anoBi
    dias = (anoBi * 366) + (anosNormais * 365)
    qtdTotal = dias * qtdDia
    totalPerdido = qtdTotal * 10
    print("quantidade de tempo perdido: ")
    print(totalPerdido)


numeroInt()
qtdLata()
precoDesconto()
precoCarro()
diasPerdidoFumando()