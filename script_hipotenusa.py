#Uso o import para importar o módulo sys.
import sys

#Depois são usados os códigos if e len para ter certeza que foram
# digitados apenas 2 numeros depois do nome. 
#Caso não haja dois números após o nome,
#mostra a mensagem de erro e o sys.exit(1) encerra o programa.

if len(sys.argv) != 3:
    print("Erro: passe dois números inteiros. Exemplo: python3 script_hipotenusa.py 3 4")
    sys.exit(1)
 
#O 1º e o 2º número digitados são armazenados em variáveis.

txt_a = sys.argv[1]
txt_b = sys.argv[2]
 
#Para conferir se são inteiros é usado isdigit para retornar
#apenas se o texto tiver só dígitos. Caso não sejam inteiros
#if not faz o bloco de erro rodar.

if not (txt_a.isdigit() and txt_b.isdigit()):
    print("Erro: a e b devem ser números inteiros positivos.")
    sys.exit(1)
 
#O int tranforma os números digitados que estão 
#em texto em um número e armazeno em a e b.
a = int(txt_a)
b = int(txt_b)
 
#Uso if not para garantir que os números estejam entre o e 500
#caso não estejam, uso print para mostrar a mensagem de erro.
if not (0 < a < 500 and 0 < b < 500):
    print("Erro: a e b devem ser maiores que 0 e menores que 500.")
    sys.exit(1)
 
#Faço o teorema de pitágoras com os números sendo a resposta o z
#e uso print para imprimir o resulta com f para usar os valores
#das variáveis.
z = a ** 2 + b ** 2
 
print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a={a} e b={b}, é {z}")
