# Entregável 1 — Verificação de bateria

**Nome:** Ana Clara dos Santos

## Objetivo

A ideia deste programa é descobrir se a bateria disponível é suficiente para uma missão de um robô.

Para isso, são informados a quantidade de bateria disponível, o tempo que a missão deve durar e quanto de bateria é gasto a cada minuto. 

A partir desses valores, o programa calcula o gasto total da missão e verifica se a bateria é suficiente para realizá-la. Se houver bateria suficiente, informa quanto restará ao final. Caso contrário, mostra quantos pontos percentuais faltariam para completar a missão.

## Como executar

É necessário ter o Python 3 instalado.

A execução deve ser feita a partir da pasta principal do projeto com o comando:

    python3 src/missao.py

## Exemplo

### Entrada

    Bateria atual (0 a 100%): 80
    Duração prevista da missão (minutos): 10
    Consumo por minuto (pontos percentuais de bateria): 3

### Saída

    Bateria suficiente para executar a missão. 
    Bateria  restante: 50%.