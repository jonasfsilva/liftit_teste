# Liftit Teste

Liftit Teste

# Como Testar a Aplicação

    - docker-compose -f docker-compose.test.yaml up
    - docker-compose -f docker-compose.test.yaml down

# Como Executar o Projeto

    - docker-compose up
    - Acessar o swagger em http://localhost:5000/
    
    - Requisição Valida:
        ``` "curl -X POST "http://localhost:5000/users/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"nome\": \"string\",  \"email\": \"string\",  \"telefone\": \"989529891\",  \"pais\": \"string\",  \"cidade\": \"string\",  \"endereco\": \"string\",  \"senha\": \"string\",  \"verificado\": true}" ```

    - Requisição Invalida:
        ``` "curl -X POST "http://localhost:5000/users/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"nome\": \"string\",  \"email\": \"string\",  \"telefone\": \"9895comletras29891\",  \"pais\": \"string\",  \"cidade\": \"string\",  \"endereco\": \"string\",  \"senha\": \"string\",  \"verificado\": true}" ```


# Tecnologias Utilizadas

    - Python
    - Flask, FlaskRestplus
    - RabbitMQ
    - Docker
    - Docker-compose

# Fluxo da Aplicação
![alt text](./fluxo.jpg)
