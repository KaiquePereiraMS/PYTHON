prato = 5
pilha = list(range(1, prato + 1))
while True:
       print(f"\nExistem {len(pilha)} pratos na pilha")
       print(f"Pilha atual: {pilha}")
       print("Digite E para ampliar um novo prato,")
       print("ou D para desempilhar. S para sair.")
       operação = input("Operação (E, D ou S):")
       if operação == "D":
           if len(pilha) > 0:
               lavado = pilha.pop(-1)
               print(f"prato {lavado} lavado")
           else:
               print("Pilha vazia! nada para lavar.")
       elif operação == "E":
           prato += 1 #novo preto
           pilha.append(prato)
       elif operação == "S":
           break
       else:
           print("Operação inválida! digite apenas E,D ou S!")