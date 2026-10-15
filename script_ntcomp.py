import sys
 
#É usado input para pedir a sequência de DNA ao usuário usando .strip
#para remover espaços na ponta da sequência e .upper para tranformar a
#sequência em maiúscula caso o usuário digite em minúsculo. Em seguida
#armazeno resposta em "sequencia". 

sequencia = input("Digite uma sequência de DNA: ").strip().upper()
 
#Para validar a sequência é usado if e len para contar se a sequência tem
#0 caracteres e imprimir a mensagem de erro.
#É utilizado for e if para avaliar se o código de DNA apenas contem 
#"ATCG" e,caso contrário, imprimir a mensagem de erro indicando o
#caractere errado.
if len(sequencia) == 0:
    print("Erro: nenhuma sequência foi digitada.")
    sys.exit(1)
 
for caractere in sequencia:
    if caractere not in "ATCG":
        print(f"Erro: caractere inválido '{caractere}'. Use apenas A, T, C e G.")
        sys.exit(1)

#Aqui é atribuida uma váriavel para cada nucleotideo
#com a contagem começando em zero.
A = 0
T = 0
C = 0
G = 0

#Para contar é utilizado o for que repete o comando de baixo uma vez para
#cada digito da sequência.Os if e elif adicionam 1 para cada nucleotideo
#encontrado. Por fim o print com f imprimem os valores encontrados.

for nucleotideo in sequencia:
    if nucleotideo == "A":
        A += 1
    elif nucleotideo == "T":
        T += 1
    elif nucleotideo == "C":
        C += 1
    elif nucleotideo == "G":
        G += 1

print(f"A: {A}")
print(f"T: {T}")
print(f"C: {C}")
print(f"G: {G}")

