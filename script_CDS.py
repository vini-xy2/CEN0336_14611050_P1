import sys
 
#Para garantir que sejam aceitos 7 argumentos na linha de comentos 
#é usado o comando if com o len para contar os argumentos. 
#Caso não sejam oito argumentos contando com o nome do script aparece 
#a mensagem de erro e o exemplo de como fazer.
if len(sys.argv) != 8:
    print("Erro: forneça a sequência de DNA e 6 números inteiros.")
    print("Use: python3 script_CDS.py sequencia n1 n2 n3 n4 n5 n6")
    sys.exit(1)
 
#Agora é armazenada a sequência tranformando ela em maiúscula e os números.
sequencia = sys.argv[1].upper()
numeros_texto = sys.argv[2:8]

#Para garantir que a sequência tenha caracteres é feita  a contagem usando
#if e len para que ela não seja zero e imprima uma mensagem de erro
#caso seja. Para avaliar que tem apenas "ATCG" é uso o comando
#for e if para analalizar cada caractere e impimir o erro indicado
#qual caractere está errado.
if len(sequencia) == 0:
    print("Erro: a sequência de DNA está vazia.")
    sys.exit(1)
 
for caractere in sequencia:
    if caractere not in "ATCG":
        print(f"Erro: a sequência contém o caractere inválido '{caractere}'. Use apenas A, T, C e G.")
        sys.exit(1)
 
#Para os números é criado uma lista vazia para armazena-los. Depois
#é usado for para analizar cada número digitado e if not com isdigt
# para garantir que são números inteiros.Caso haja problema imprimi
#a mensagem de erro com o numero não permitido. Depois os números em
#texto são convertido em números pelo int e o append adiciona o número
#a lista crianda anteriormente. Por fim a lista é desempacotda para
#n1, n2... 
numeros = []
for texto in numeros_texto:
    if not texto.isdigit():
        print(f"Erro: '{texto}' não é um número inteiro positivo.")
        sys.exit(1)
    numeros.append(int(texto))
 
n1, n2, n3, n4, n5, n6 = numeros
 
#Aqui é armazenado quantos nucleotideos tem a sequência, em seguida
#é analizado se os números digitados estão no intervalo entre 0 e o 
#tamanho da sequência. Por fim é analizado se os números estão em ordem
#crescente.
tamanho = len(sequencia)
 
for n in numeros:
    if n < 1 or n > tamanho:
        print(f"Erro: o número {n} deve estar entre 1 e {tamanho}.")
        sys.exit(1)
 
if not (n1 < n2 < n3 < n4 < n5 < n6):
    print("Erro: os números devem estar em ordem crescente.")
    sys.exit(1)
 
#Aqui é feito a separação dos cds e dos introns com base nos números
#dados.
cds1 = sequencia[n1 - 1:n2]
intron1 = sequencia[n2:n3 - 1]
cds2 = sequencia[n3 - 1:n4]
intron2 = sequencia[n4:n5 - 1]
cds3 = sequencia[n5 - 1:n6]
 
#Aqui startswith e endswit avaliam se o intron começa com "GT" e
#termina com "AG".
intron1_verdadeiro = intron1.startswith("GT") and intron1.endswith("AG")
intron2_verdadeiro = intron2.startswith("GT") and intron2.endswith("AG")
 
#Aqui se os dois introns forem validados, imprime a junção cds1,cds2 e 
#cds3. Caso um não for verdadeiro irá imprimir a mensagem de erro. 
if intron1_verdadeiro and intron2_verdadeiro:
    print(cds1 + cds2 + cds3)
else:
    if not intron1_verdadeiro:
        print(f"Erro: o íntron entre a CDS 1 e a CDS 2 ({intron1}) não começa com GT e termina com AG.")
    if not intron2_verdadeiro:
        print(f"Erro: o íntron entre a CDS 2 e a CDS 3 ({intron2}) não começa com GT e termina com AG.")

