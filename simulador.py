print("=== SISTEMA DE GESTÃO DA PANIFICADORA ===")

preco = float(input("Preço de venda do pão: R$ "))
custo = float(input("Custo de produção por pão: R$ "))
qtd = int(input("Pães vendidos por dia: "))
despesas = float(input("Despesas fixas diárias: R$ "))
taxa = float(input("Crescimento a cada 30 dias (%): ")) / 100
periodos = int(input("Quantos períodos de 30 dias deseja simular? "))

for periodo in range(periodos + 1):
    vendas = round(qtd * (1 + taxa) ** periodo)

    faturamento = preco * vendas
    custo_total = custo * vendas + despesas
    lucro = faturamento - custo_total

    print(f"\nPeríodo {periodo}")
    print(f"Pães vendidos por dia: {vendas}")
    print(f"Faturamento diário: R$ {faturamento:.2f}")
    print(f"Custo total diário: R$ {custo_total:.2f}")
    print(f"Lucro diário: R$ {lucro:.2f}")