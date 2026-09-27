"""
Testes Unitários do Dashboard Porsche e Dataset Sanitizado
Autor: Wendel Vieira
"""

import unittest
import os
import json


class TestPorscheDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_dir = os.path.dirname(__file__)
        cls.json_path = os.path.join(cls.base_dir, "porsche_vendas.json")
        cls.csv_path = os.path.join(cls.base_dir, "porsche_vendas_sanitizado.csv")
        cls.html_path = os.path.join(cls.base_dir, "index.html")

        with open(cls.json_path, "r", encoding="utf-8") as f:
            cls.data = json.load(f)

    def test_quantidade_registros(self):
        """O dataset sanitizado deve conter exatamente 100 vendas."""
        self.assertEqual(len(self.data), 100, "Dataset deve possuir 100 registros.")

    def test_campos_obrigatorios(self):
        """Cada registro deve conter todos os campos de auditoria e negócio."""
        campos_esperados = {
            "id_venda", "data_venda", "ano_modelo", "modelo",
            "propulsao", "cor", "cidade", "estado", "preco", "metodo_pagamento"
        }
        for item in self.data:
            self.assertTrue(campos_esperados.issubset(item.keys()))
            self.assertGreater(item["preco"], 0)

    def test_pergunta_negocio_1_modelo_lider(self):
        """Pergunta 1: Deve ser possível apurar o modelo com maior faturamento."""
        receita_por_modelo = {}
        for item in self.data:
            m = item["modelo"]
            receita_por_modelo[m] = receita_por_modelo.get(m, 0.0) + item["preco"]
        
        self.assertGreater(len(receita_por_modelo), 0)
        lider = max(receita_por_modelo.items(), key=lambda x: x[1])
        self.assertIsInstance(lider[0], str)
        self.assertGreater(lider[1], 0)

    def test_pergunta_negocio_2_geografia(self):
        """Pergunta 2: Estados devem ter faturamento e ticket médio calculáveis."""
        estados = {}
        for item in self.data:
            uf = item["estado"]
            if uf not in estados:
                estados[uf] = {"rev": 0.0, "qtd": 0}
            estados[uf]["rev"] += item["preco"]
            estados[uf]["qtd"] += 1
        
        self.assertIn("SP", estados)
        self.assertGreater(estados["SP"]["rev"], 0)

    def test_pergunta_negocio_3_propulsao_pagamento(self):
        """Pergunta 3: Correlação entre método de pagamento e eletrificação."""
        tipos_prop = {item["propulsao"] for item in self.data}
        self.assertIn("Combustão", tipos_prop)
        self.assertIn("Elétrico", tipos_prop)
        self.assertIn("Híbrido", tipos_prop)

    def test_html_integridade(self):
        """O arquivo index.html deve conter os elementos do dashboard e Chart.js."""
        self.assertTrue(os.path.exists(self.html_path))
        with open(self.html_path, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn("chartModels", html)
        self.assertIn("chartRegions", html)
        self.assertIn("chartPaymentProp", html)
        self.assertIn("chartTimeline", html)
        self.assertIn("Wendel Vieira", html)


if __name__ == "__main__":
    unittest.main()
