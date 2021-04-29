vetor = [ 1, 2, 2, 8, 8, 5, 2, 3, 2, 3, 5, 1, 10, 11, 120, 100, 1, 3, 11]

vetor.sort()

print(vetor)
novo_vetor = []
valor_anterior = None

for i in vetor:
	if i == valor_anterior:
		novo_vetor.append(i)
		novo_vetor.append(i)
		vetor.remove(i)
	valor_anterior = i

vetor.extend(novo_vetor)

print(vetor)
