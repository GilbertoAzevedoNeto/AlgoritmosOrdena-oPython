from random import randint
import datetime

#Algoritmo de ordenação insertion sort.   
def algoritmo_ordenacao_insertion(A):
	for n in range(1, len(A)):
		m = n - 1
		while A[m] > A[m+1] and m >= 0:
			A[m],A[m+1] = A[m+1],A[m] 
			m -= 1
	return A	
	
#Algoritmo de ordenação heap sort.	
def algoritmo_ordenacao_heap(A):
		n = len(A)
		for i in range(n, -1, -1):
			algoritmo_ordenacao_heapify(A, n, i)
			
		for i in range(n - 1, 0, -1):
			A[i], A[0] = A[0], A[i]
			algoritmo_ordenacao_heapify(A, i, 0)		
		return A
			
def algoritmo_ordenacao_heapify(A, tamanho, indice_raiz):
		maior = indice_raiz
		filho_esquerda = (2 * indice_raiz) + 1
		filho_direita = (2 * indice_raiz) + 2
		
		if filho_esquerda < tamanho and A[filho_esquerda] > A[maior]:
			maior = filho_esquerda
			
		if filho_direita < tamanho and A[filho_direita] > A[maior]:
			maior = filho_direita
			
		if maior != indice_raiz:
			A[indice_raiz],A[maior] = A[maior], A[indice_raiz]
			algoritmo_ordenacao_heapify(A, tamanho, maior)
			

#Algoritmo de ordenação merge sort.	
def algoritmo_ordenacao_merge(A):
	if len(A) <= 1:
		return A
	
	metade = len(A) // 2
	
	lista_esquerda = algoritmo_ordenacao_merge(A[:metade])
	lista_direita = algoritmo_ordenacao_merge(A[metade:])
	
	return algoritmo_ordenacao_merge_agrupar(lista_esquerda, lista_direita)
	
def algoritmo_ordenacao_merge_agrupar(lista_esquerda, lista_direita):
	listaNumerosOrdenados = []
	indice_lista_esquerda = indice_lista_direita = 0
	tamanho_lista_esquerda, tamanho_lista_direita = len(lista_esquerda), len(lista_direita)
	for i in range(tamanho_lista_esquerda + tamanho_lista_direita):
		if indice_lista_esquerda < tamanho_lista_esquerda and indice_lista_direita < tamanho_lista_direita:
			if lista_esquerda[indice_lista_esquerda] <= lista_direita[indice_lista_direita]:
				listaNumerosOrdenados.append(lista_esquerda[indice_lista_esquerda])
				indice_lista_esquerda += 1
			else:
				listaNumerosOrdenados.append(lista_direita[indice_lista_direita])
				indice_lista_direita += 1
		elif indice_lista_esquerda == tamanho_lista_esquerda:
			listaNumerosOrdenados.append(lista_direita[indice_lista_direita])
			indice_lista_direita += 1
		elif indice_lista_direita == tamanho_lista_direita:
			listaNumerosOrdenados.append(lista_esquerda[indice_lista_esquerda])
			indice_lista_esquerda += 1
	return listaNumerosOrdenados

#Algoritmo de ordenação quick sort.	
def algoritmo_ordenacao_quick(A):
	def _algoritmo_ordenacao_quick(A, minimo, maximo):
		if minimo < maximo:
			indice_central = algoritmo_ordenacao_quick_particionamento(A, minimo, maximo)
			_algoritmo_ordenacao_quick(A, minimo, indice_central)
			_algoritmo_ordenacao_quick(A, indice_central+1, maximo)
			
	_algoritmo_ordenacao_quick(A, 0, len(A) - 1)
	return A
	
def algoritmo_ordenacao_quick_particionamento(A, minimo, maximo):
	pivot = A[(minimo + maximo) // 2]
	i = minimo - 1
	j = maximo + 1
	while True:
		i += 1
		while A[i] < pivot:
			i += 1
			
		j -= 1
		while A[j] > pivot:
			j -= 1
		
		if i >= j:
			return j
		
		A[i], A[j] = A[j], A[i]

#Algoritmo de ordenação quick sort hibrido com insertion sort.	
def algoritmo_ordenacao_quick_hibrido(A):
	def _algoritmo_ordenacao_quick_hibrido(A, minimo, maximo):
		if minimo < maximo:
			if (maximo - minimo < 10):
				algoritmo_ordenacao_quick_insertion(A, minimo, maximo)			
			else:
				indice_central = algoritmo_ordenacao_quick_particionamento(A, minimo, maximo)
				_algoritmo_ordenacao_quick_hibrido(A, minimo, indice_central)
				_algoritmo_ordenacao_quick_hibrido(A, indice_central+1, maximo)
				
			
	_algoritmo_ordenacao_quick_hibrido(A, 0, len(A) - 1)
	return A

def algoritmo_ordenacao_quick_insertion(A, minimo, maximo):
	for n in range(minimo + 1, maximo):
		m = n - 1
		while A[m] > A[m+1] and m >= 0:
			A[m],A[m+1] = A[m+1],A[m] 
			m -= 1
	return A	

#Algoritmo de ordenação merge sort hibrido.	
def algoritmo_ordenacao_merge_hibrido(A):
	if len(A) <= 1:
		return A
 
	metade = len(A) // 2
	
	if (metade <= 2):
		return algoritmo_ordenacao_merge_insertion(A)		
	else:
		lista_esquerda = algoritmo_ordenacao_merge_hibrido(A[:metade])
		lista_direita = algoritmo_ordenacao_merge_hibrido(A[metade:])
		return algoritmo_ordenacao_merge_agrupar(lista_esquerda, lista_direita)	
		
	return A

def algoritmo_ordenacao_merge_insertion(A):
	for n in range(1, len(A)):
		m = n - 1
		while A[m] > A[m+1] and m >= 0:
			A[m],A[m+1] = A[m+1],A[m] 
			m -= 1
	return A	

	
#Função para calcular o tempo em milliseconds	
def calculando_tempo_algoritmo_nanosegundos (a, b):
	delta = b - a
	return int((delta.total_seconds() * 1000)*1000000) # nanosegundos
		

#Preparando ambiente	
listaNumerosOrdenar = []
listaNumerosOrdenados = []
quantosArranjosCriar = int(input("Informe quantos arranjos quer criar: "))
maiorNumero = int(input("Informe até qual número deseja colocar no arranjo: "))
quantasVezesExecutarOrdenacao = int(input("Informe quantas vezes quer executar a ordenação do array com mesmo algoritmo: "))
f= open("resultadoExecucoes.txt","w+")

for arranjo in range(quantosArranjosCriar):
	listaNumerosOrdenar = []
	quantidadeNumeros = randint(30000,30000)
	for x in range(quantidadeNumeros):
		listaNumerosOrdenar.append(randint(0,maiorNumero))
#executando a ordenação com o algoritmo insertion sort
	for quantidadeVezes in range(quantasVezesExecutarOrdenacao):
		datahorainicial = datetime.datetime.now()
		listaNumerosOrdenados = algoritmo_ordenacao_insertion(listaNumerosOrdenar)
		datahorafinal = datetime.datetime.now()
		f.write("insertionSort;" + str(len(listaNumerosOrdenados)) + ";" + str(calculando_tempo_algoritmo_nanosegundos (datahorainicial, datahorafinal)) + "\r\n")
		listaNumerosOrdenados = []
#executando a ordenação com o algoritmo heap sort		
	for quantidadeVezes in range(quantasVezesExecutarOrdenacao):
		datahorainicial = datetime.datetime.now()
		listaNumerosOrdenados = algoritmo_ordenacao_heap(listaNumerosOrdenar)
		datahorafinal = datetime.datetime.now()
		f.write("heapSort;" + str(len(listaNumerosOrdenados)) + ";" + str(calculando_tempo_algoritmo_nanosegundos (datahorainicial, datahorafinal)) + "\r\n")
		listaNumerosOrdenados = []	
#executando a ordenação com o algoritmo merge sort		
	for quantidadeVezes in range(quantasVezesExecutarOrdenacao):
		datahorainicial = datetime.datetime.now()
		listaNumerosOrdenados = algoritmo_ordenacao_merge(listaNumerosOrdenar)
		datahorafinal = datetime.datetime.now()
		f.write("mergeSort;" + str(len(listaNumerosOrdenados)) + ";" + str(calculando_tempo_algoritmo_nanosegundos (datahorainicial, datahorafinal)) + "\r\n")
		listaNumerosOrdenados = []	
#executando a ordenação com o algoritmo quick sort		
	for quantidadeVezes in range(quantasVezesExecutarOrdenacao):
		datahorainicial = datetime.datetime.now()
		listaNumerosOrdenados = algoritmo_ordenacao_quick(listaNumerosOrdenar)
		datahorafinal = datetime.datetime.now()
		f.write("quickSort;" + str(len(listaNumerosOrdenados)) + ";" + str(calculando_tempo_algoritmo_nanosegundos (datahorainicial, datahorafinal)) + "\r\n")
		listaNumerosOrdenados = []			
#executando a ordenação com o algoritmo quick sort	hibrido
	for quantidadeVezes in range(quantasVezesExecutarOrdenacao):
		datahorainicial = datetime.datetime.now()
		listaNumerosOrdenados = algoritmo_ordenacao_quick_hibrido(listaNumerosOrdenar)
		datahorafinal = datetime.datetime.now()
		f.write("quickSortHibrido;" + str(len(listaNumerosOrdenados)) + ";" + str(calculando_tempo_algoritmo_nanosegundos (datahorainicial, datahorafinal)) + "\r\n")
		listaNumerosOrdenados = []			
#executando a ordenação com o algoritmo merge sort	hibrido
	for quantidadeVezes in range(quantasVezesExecutarOrdenacao):
		datahorainicial = datetime.datetime.now()
		listaNumerosOrdenados = algoritmo_ordenacao_merge_hibrido(listaNumerosOrdenar)
		datahorafinal = datetime.datetime.now()
		f.write("mergeSortHibrido;" + str(len(listaNumerosOrdenados)) + ";" + str(calculando_tempo_algoritmo_nanosegundos (datahorainicial, datahorafinal)) + "\r\n")
		listaNumerosOrdenados = []			
		
f.close()