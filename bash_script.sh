#!/bin/bash

#1-comando que mostre a pasta/diretório
#Para essa operação é preciso apenas utilizar o código pwd que já indica o diretório atual
pwd

#2-comando que gera uma lista da pasta HOME e redireciona para lista_HOME.txt
#Para isso é usado o codigo ls para listar arquivos e diretórios
#o -l para a visualização detalhada, $HOME para mapear a pasta principal
# e o > que redireciona para o arquivo que desejo.
ls -l $HOME > lista_HOME.txt

#3-apresentar a data
#utilizo o comando date para acessar e mostrar a data pelo sistema do
# computador
date
