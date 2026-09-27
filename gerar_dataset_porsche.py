"""
Gerador e Sanitizador do Dataset de Vendas Porsche (100 Registros)
Autor: Wendel Vieira
Projeto: Dashboard Interativo da Porsche com Agentes de IA
"""

import json
import csv
import random
from datetime import datetime

MODELOS_PORSCHE = [
    {"modelo": "911 Carrera S", "preco_base": 1150000.0, "tipo": "Combustão"},
    {"modelo": "911 Turbo S", "preco_base": 1790000.0, "tipo": "Combustão"},
    {"modelo": "911 GT3 RS", "preco_base": 1950000.0, "tipo": "Combustão"},
    {"modelo": "Taycan 4S", "preco_base": 780000.0, "tipo": "Elétrico"},
    {"modelo": "Taycan Turbo S", "preco_base": 1180000.0, "tipo": "Elétrico"},
    {"modelo": "Panamera 4 E-Hybrid", "preco_base": 790000.0, "tipo": "Híbrido"},
    {"modelo": "Cayenne V6", "preco_base": 730000.0, "tipo": "Combustão"},
    {"modelo": "Cayenne Turbo E-Hybrid", "preco_base": 1120000.0, "tipo": "Híbrido"},
    {"modelo": "Macan GTS", "preco_base": 650000.0, "tipo": "Combustão"},
    {"modelo": "Macan EV", "preco_base": 620000.0, "tipo": "Elétrico"},
    {"modelo": "718 Cayman GTS 4.0", "preco_base": 690000.0, "tipo": "Combustão"},
    {"modelo": "718 Boxster Style Edition", "preco_base": 560000.0, "tipo": "Combustão"},
]

CIDADES_ESTADOS = [
    {"cidade": "São Paulo", "estado": "SP", "peso": 40},
    {"cidade": "Campinas", "estado": "SP", "peso": 10},
    {"cidade": "Rio de Janeiro", "estado": "RJ", "peso": 15},
    {"cidade": "Curitiba", "estado": "PR", "peso": 12},
    {"cidade": "Belo Horizonte", "estado": "MG", "peso": 10},
    {"cidade": "Porto Alegre", "estado": "RS", "peso": 8},
    {"cidade": "Brasília", "estado": "DF", "peso": 5},
]

METODOS_PAGAMENTO = [
    {"metodo": "À Vista (TED/PIX)", "peso": 45},
    {"metodo": "Financiamento Bancário", "peso": 35},
    {"metodo": "Carta de Crédito / Consórcio", "peso": 20},
]

CORES_EXTERIOR = ["Preto GT", "Branco Carrara", "Prata GT", "Vermelho Carmim", "Azul Gentian", "Cinza Giz", "Verde Python"]

def gerar_dataset_porsche():
    random.seed(42)
    registros = []

    cidades_pop = [c for c in CIDADES_ESTADOS]
    cidades_pesos = [c["peso"] for c in CIDADES_ESTADOS]

    metodos_pop = [m["metodo"] for m in METODOS_PAGAMENTO]
    metodos_pesos = [m["peso"] for m in METODOS_PAGAMENTO]

    for i in range(1, 101):
        car = random.choice(MODELOS_PORSCHE)
        loc = random.choices(cidades_pop, weights=cidades_pesos)[0]
        metodo = random.choices(metodos_pop, weights=metodos_pesos)[0]
        ano_fab = random.choices([2021, 2022, 2023, 2024], weights=[15, 25, 35, 25])[0]

        # Variação realista de opcionais (-5% a +15% sobre o preço base)
        fator_opcional = round(random.uniform(0.95, 1.15), 4)
        preco_final = round((car["preco_base"] * fator_opcional) / 1000.0) * 1000.0

        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        data_venda = f"2024-{mes:02d}-{dia:02d}"

        reg = {
            "id_venda": f"POR-{i:03d}",
            "data_venda": data_venda,
            "ano_modelo": ano_fab,
            "modelo": car["modelo"],
            "propulsao": car["tipo"],
            "cor": random.choice(CORES_EXTERIOR),
            "cidade": loc["cidade"],
            "estado": loc["estado"],
            "preco": preco_final,
            "metodo_pagamento": metodo,
        }
        registros.append(reg)

    return registros

def salvar_arquivos(registros, pasta_destino):
    import os
    os.makedirs(pasta_destino, exist_ok=True)

    # 1. JSON
    json_path = os.path.join(pasta_destino, "porsche_vendas.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=2, ensure_ascii=False)

    # 2. CSV
    csv_path = os.path.join(pasta_destino, "porsche_vendas_sanitizado.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(registros[0].keys()))
        writer.writeheader()
        writer.writerows(registros)

    print(f"[OK] 100 registros gerados e salvos em JSON e CSV em: {pasta_destino}")

if __name__ == "__main__":
    import os
    destino = os.path.join("projects_workspace", "porsche-sales-dashboard")
    regs = gerar_dataset_porsche()
    salvar_arquivos(regs, destino)
