a = float(input('Digite um valor:'))
b =  float(input('Digite outro:'))
operação = input("Digite a operação a realizar (+, -, * ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
    print("operação invalida")
    resultado = 0
print("resultado:",resultado)
