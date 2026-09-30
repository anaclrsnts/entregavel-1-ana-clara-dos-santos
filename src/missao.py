def verificar_missao():
    bateria_atual = float(input("Bateria atual (0 a 100%): "))
    duracao_missao = float(input("Duração prevista da missão (minutos): "))
    consumo_minuto = float(input("Consumo por minuto (pontos percentuais de bateria): "))

    if bateria_atual < 0 or bateria_atual > 100 or duracao_missao <= 0 or consumo_minuto <= 0:
        print("Valor inválido.")
        return

    consumo_total = duracao_missao * consumo_minuto
    bateria_restante = bateria_atual - consumo_total

    if bateria_restante >= 0:
        print(f"Bateria suficiente para executar a missão. \nBateria  restante: {bateria_restante:g}%.")
        return

    print(f"Bateria insuficiente. A missão não pode ser concluída.\nFaltam  {-bateria_restante:g} pontos percentuais de bateria.")


if __name__ == "__main__":
    verificar_missao()