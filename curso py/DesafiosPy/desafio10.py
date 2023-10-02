expressão = input("Digite a sequnecia de parenteses a validar:")
x = 0
pilha = []
while x < len(expressão):
      if expressão[x] == "(":
          pilha.append("(")
      if expressão[x] == ")":
          if len(pilha) > 0:
              topo = pilha.pop(-1)
              topo.append(")") #Força a mensagem de erro
              break
      x = x + 1
if len(pilha) == 0:
    print("ok")
else:
    print("erro")
