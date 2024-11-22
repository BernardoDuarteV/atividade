nome = input("Digite seu nome completo: ")
palavras = nome.split()
sobrenome = nome.split()[1:]

print("Primeiro nome: " + str(palavras[0]))
print("Sobrenome completo: " + str(sobrenome))
print("Último sobrenome: " + str(palavras[-1]))