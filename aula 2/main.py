# metodos
def areaCirculo():
    raio = float(input("digite o raio"))
    pi = float(3.14159)
    area = pi*(raio ** 2)
    print(area)

def nota():
    nota1 = float(input("digite nota1"))
    nota2 = float(input("digite nota2"))
    peso1 = 1
    peso2 = 2
    media = ((nota1*peso1) + (nota2 * peso2))/(peso1 + peso2)
    print(media)

def salario():
    salarioHora = float(input("digite o salario por hora : "))
    horasTrab = int(input("digite as horas trabalhadas: "))
    inss = 5
    salarioBruto = salarioHora * horasTrab
    salarioLiquido = salarioBruto * inss / 100
    salarioLiquido = salarioBruto - salarioLiquido
    print("Bruto - ")
    print(salarioBruto)
    print("Liquido - ")
    print(salarioLiquido)

#chamar os metodos
areaCirculo()
nota()
salario()













