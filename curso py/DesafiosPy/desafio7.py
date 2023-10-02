distancia = float(input("Digite a distancia percorrida:"))
if distancia <= 200:
     passagem = 0.5 * distancia
else:
     passagem = 0.45 * distancia
print(f"Preço da passagem: R$ {passagem:7.2f}")