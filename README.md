# Script de Criação de Serviços :robot:

Esse projeto tem como função automatizar a criação de serviço no ambiente Linux

## Tecnologias :computer:
- python 3
- shellscript

## Rodando o script
1. Clone o projeto:
```bash
  $ git clone git@github.com:j0n4t45d3v/create-service-script.git
```
2. Mova os arquivos pra /usr/local/bin/:
- mande a pasta para /usr/local/bin:
```bash
  $ mv ./create-service-script/ /usr/local/bin/
```
- crie um link simbólico na raiz do /usr/local/bin
```bash 
  $ ln -s /usr/local/bin/create-service-script/create-service /usr/local/bin/create-service 
``` 
- de a permição para o link simbolico executar:
```bash
  $ chmod +x /usr/local/bin/create-service
```
4. Agora é so executar o script e criar seus serviços:
```bash
  $ create-service
```