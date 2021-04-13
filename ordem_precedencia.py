materia = input("Digite o nome da materia: ")
nota1 = float(input("Digite a PRIMERA nota: "))
nota2 = float(input("Digite a SEGUNDA nota: "))
nota3 = float(input("Digite a TERCEIRA nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Na materia {materia} sua media final é {media:.2}")
