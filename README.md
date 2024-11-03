# Crud Neo4j

Crud feito em Python usando o banco de dados Neo4j para fins da disciplina de Banco de Dados Não Relacionais da Faculdade Senac PE

Aluno: Renan Leite Vieira

## Instalação

Sistema utilizado: Ubuntu 22.04 LTS

## Usando Docker

Baixar a imagem e iniciar o Neo4j em docker:

    docker compose up -d

Acesse o Neo4j no seguinte endereço:

    http://localhost:7474/browser/

Para acessar o sistema, digite o usuário e a senha abaixo (disponível no arquivo `docker-compose.yml`): 

    user: neo4j
    password: password

Após, executar o script (`crud.py`) com o comando:

    python3 crud.py

## Usando Neo4j local

Instalar o Neo4j: https://neo4j.com/docs/operations-manual/current/installation/linux/debian/

Iniciar o Neo4j (http://localhost:7474/browser/): 

    sudo /usr/bin/neo4j start

Instalar o driver do Neo4j para Python: 
  
    sudo pip install neo4j

Alterar o arquivo de configuração `config.json` com a sua senha (padrão: `password`): 

    {"username":"neo4j","password":"password"}

Após, executar o script (`crud.py`) com o comando:

    python3 crud.py

## Observações

ATENÇÃO: O Neo4j exige uma senha de no mínimo 8 caracteres.

ATENÇÃO: A função deleteDB irá apagar todos os dados da base de dados Neo4j. Use apenas se estiver conectado a uma base de dados local. 

