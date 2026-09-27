import json
import os

def generate_html():
    json_path = os.path.join("projects_workspace", "porsche-sales-dashboard", "porsche_vendas.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    json_str = json.dumps(data, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Porsche Sales Intelligence Dashboard | Wendel Vieira</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    :root {{
      --bg-dark: #0a0b0e;
      --bg-card: #13151c;
      --bg-card-hover: #1a1d27;
      --porsche-red: #d5001c;
      --porsche-red-hover: #b00017;
      --porsche-gold: #c5a059;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(213, 0, 28, 0.4);
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Outfit', sans-serif;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* HEADER */
    header {{
      background: linear-gradient(180deg, #161822 0%, var(--bg-dark) 100%);
      border-bottom: 1px solid var(--border-color);
      padding: 24px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .logo-area h1 {{
      font-family: 'Montserrat', sans-serif;
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-area h1 span {{
      color: var(--porsche-red);
    }}

    .logo-area p {{
      color: var(--text-muted);
      font-size: 13px;
      margin-top: 4px;
    }}

    .badge-author {{
      background: rgba(197, 160, 89, 0.12);
      border: 1px solid var(--porsche-gold);
      color: var(--porsche-gold);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}

    .container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 32px;
      width: 100%;
      flex: 1;
    }}

    /* FILTERS PANEL */
    .filter-section {{
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }}

    .filter-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}

    .filter-header h3 {{
      font-size: 15px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-reset {{
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 6px 16px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-reset:hover {{
      background: var(--porsche-red);
      color: #fff;
      border-color: var(--porsche-red);
    }}

    .filters-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
    }}

    .filter-group label {{
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .filter-group select, .filter-group input {{
      width: 100%;
      background-color: #0e1017;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
    }}

    .filter-group select:focus, .filter-group input:focus {{
      border-color: var(--porsche-gold);
    }}

    /* METRIC CARDS */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
      margin-bottom: 28px;
    }}

    .metric-card {{
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 22px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
      transition: transform 0.2s, border-color 0.2s;
    }}

    .metric-card:hover {{
      transform: translateY(-2px);
      border-color: var(--border-accent);
    }}

    .metric-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--porsche-red);
    }}

    .metric-card.gold::before {{
      background: var(--porsche-gold);
    }}

    .metric-title {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-muted);
      margin-bottom: 8px;
    }}

    .metric-value {{
      font-family: 'Montserrat', sans-serif;
      font-size: 26px;
      font-weight: 700;
      color: #fff;
    }}

    .metric-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 6px;
    }}

    /* CHARTS GRID */
    .charts-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-bottom: 32px;
    }}

    @media (max-width: 1024px) {{
      .charts-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .chart-box {{
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 24px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
    }}

    .chart-box-header {{
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 12px;
    }}

    .question-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--porsche-gold);
      margin-bottom: 4px;
    }}

    .chart-box-header h2 {{
      font-size: 16px;
      font-weight: 600;
      color: #fff;
    }}

    .chart-container {{
      position: relative;
      flex: 1;
      min-height: 280px;
    }}

    /* TABLE SECTION */
    .table-section {{
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 32px;
    }}

    .table-header-area {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .table-header-area h3 {{
      font-size: 16px;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}

    .search-box {{
      background-color: #0e1017;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      min-width: 260px;
      outline: none;
    }}

    .table-wrapper {{
      overflow-x: auto;
      max-height: 480px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }}

    thead th {{
      background-color: #1a1d27;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-size: 11px;
      padding: 12px 16px;
      position: sticky;
      top: 0;
      z-index: 10;
      border-bottom: 2px solid var(--border-color);
    }}

    tbody tr {{
      border-bottom: 1px solid var(--border-color);
      transition: background-color 0.15s;
    }}

    tbody tr:hover {{
      background-color: rgba(255, 255, 255, 0.03);
    }}

    tbody td {{
      padding: 12px 16px;
      color: #e2e8f0;
    }}

    .prop-badge {{
      display: inline-block;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
    }}

    .prop-eletrico {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .prop-hibrido {{
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }}

    .prop-combustao {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}

    footer {{
      background-color: #08090b;
      border-top: 1px solid var(--border-color);
      padding: 20px 32px;
      text-align: center;
      font-size: 13px;
      color: var(--text-muted);
    }}

    footer strong {{
      color: var(--text-main);
    }}
  </style>
</head>
<body>

  <header>
    <div class="logo-area">
      <h1>PORSCHE <span>INTELLIGENCE</span></h1>
      <p>Dashboard Executivo de Inteligência de Vendas (Base Sanitizada de 100 Registros)</p>
    </div>
    <div class="badge-author">
      Autor: Wendel Vieira | Desafio DIO
    </div>
  </header>

  <div class="container">

    <!-- FILTERS -->
    <div class="filter-section">
      <div class="filter-header">
        <h3>🔍 Filtros Interativos Multidimensionais</h3>
        <button class="btn-reset" onclick="resetFilters()">Limpar Filtros</button>
      </div>
      <div class="filters-grid">
        <div class="filter-group">
          <label for="filterModel">Modelo:</label>
          <select id="filterModel" onchange="applyFilters()">
            <option value="">Todos os Modelos</option>
          </select>
        </div>
        <div class="filter-group">
          <label for="filterProp">Propulsão:</label>
          <select id="filterProp" onchange="applyFilters()">
            <option value="">Todas</option>
            <option value="Combustão">Combustão</option>
            <option value="Elétrico">Elétrico</option>
            <option value="Híbrido">Híbrido</option>
          </select>
        </div>
        <div class="filter-group">
          <label for="filterState">Estado (UF):</label>
          <select id="filterState" onchange="applyFilters()">
            <option value="">Todos os Estados</option>
          </select>
        </div>
        <div class="filter-group">
          <label for="filterPayment">Método de Pagamento:</label>
          <select id="filterPayment" onchange="applyFilters()">
            <option value="">Todos</option>
          </select>
        </div>
      </div>
    </div>

    <!-- METRICS -->
    <div class="metrics-grid">
      <div class="metric-card">
        <div class="metric-title">Faturamento Total</div>
        <div class="metric-value" id="kpiTotalRevenue">R$ 0,00</div>
        <div class="metric-sub" id="kpiRevenueSub">100% da base filtrada</div>
      </div>
      <div class="metric-card">
        <div class="metric-title">Volume de Vendas</div>
        <div class="metric-value" id="kpiTotalVolume">0 unidades</div>
        <div class="metric-sub" id="kpiVolumeSub">Veículos comercializados</div>
      </div>
      <div class="metric-card gold">
        <div class="metric-title">Ticket Médio por Veículo</div>
        <div class="metric-value" id="kpiAverageTicket">R$ 0,00</div>
        <div class="metric-sub">Preço médio por transação</div>
      </div>
      <div class="metric-card">
        <div class="metric-title">Modelo Líder em Vendas</div>
        <div class="metric-value" id="kpiTopModel">-</div>
        <div class="metric-sub" id="kpiTopModelVal">R$ 0,00 faturados</div>
      </div>
    </div>

    <!-- BUSINESS QUESTIONS CHARTS -->
    <div class="charts-grid">
      
      <!-- PERGUNTA 1 -->
      <div class="chart-box">
        <div class="chart-box-header">
          <span class="question-badge">Pergunta de Negócio 1</span>
          <h2>Qual modelo lidera em faturamento bruto e volume de vendas?</h2>
        </div>
        <div class="chart-container">
          <canvas id="chartModels"></canvas>
        </div>
      </div>

      <!-- PERGUNTA 2 -->
      <div class="chart-box">
        <div class="chart-box-header">
          <span class="question-badge">Pergunta de Negócio 2</span>
          <h2>Como se distribui a receita entre os estados e praças?</h2>
        </div>
        <div class="chart-container">
          <canvas id="chartRegions"></canvas>
        </div>
      </div>

      <!-- PERGUNTA 3 -->
      <div class="chart-box">
        <div class="chart-box-header">
          <span class="question-badge">Pergunta de Negócio 3</span>
          <h2>Qual a correlação entre método de pagamento e eletrificação?</h2>
        </div>
        <div class="chart-container">
          <canvas id="chartPaymentProp"></canvas>
        </div>
      </div>

      <!-- PERGUNTA 4: SÉRIE TEMPORAL -->
      <div class="chart-box">
        <div class="chart-box-header">
          <span class="question-badge">Análise Temporal</span>
          <h2>Evolução Mensal do Faturamento ao Longo do Ano</h2>
        </div>
        <div class="chart-container">
          <canvas id="chartTimeline"></canvas>
        </div>
      </div>

    </div>

    <!-- TABLE -->
    <div class="table-section">
      <div class="table-header-area">
        <h3>📄 Base Transacional Sanitizada (<span id="tableRecordCount">0</span> registros)</h3>
        <input type="text" id="searchInput" class="search-box" placeholder="Buscar por ID, modelo, cidade..." oninput="renderTable()">
      </div>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Data</th>
              <th>Modelo</th>
              <th>Propulsão</th>
              <th>Cor</th>
              <th>Cidade / UF</th>
              <th>Ano</th>
              <th>Método de Pagamento</th>
              <th style="text-align: right;">Preço (R$)</th>
            </tr>
          </thead>
          <tbody id="salesTableBody">
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <footer>
    <p>Projeto de Dashboard Interativo da Porsche | Desenvolvido por <strong>Wendel Vieira</strong> para o Desafio DIO & Reclame AQUI.</p>
  </footer>

  <script>
    const RAW_DATA = {json_str};

    let filteredData = [...RAW_DATA];

    let chartModelsInstance = null;
    let chartRegionsInstance = null;
    let chartPaymentPropInstance = null;
    let chartTimelineInstance = null;

    function formatBRL(val) {{
      return new Intl.NumberFormat('pt-BR', {{ style: 'currency', currency: 'BRL' }}).format(val);
    }}

    function populateFilterOptions() {{
      const models = [...new Set(RAW_DATA.map(d => d.modelo))].sort();
      const states = [...new Set(RAW_DATA.map(d => d.estado))].sort();
      const payments = [...new Set(RAW_DATA.map(d => d.metodo_pagamento))].sort();

      const modelSelect = document.getElementById('filterModel');
      models.forEach(m => {{
        const opt = document.createElement('option');
        opt.value = m;
        opt.textContent = m;
        modelSelect.appendChild(opt);
      }});

      const stateSelect = document.getElementById('filterState');
      states.forEach(s => {{
        const opt = document.createElement('option');
        opt.value = s;
        opt.textContent = s;
        stateSelect.appendChild(opt);
      }});

      const paySelect = document.getElementById('filterPayment');
      payments.forEach(p => {{
        const opt = document.createElement('option');
        opt.value = p;
        opt.textContent = p;
        paySelect.appendChild(opt);
      }});
    }}

    function applyFilters() {{
      const selModel = document.getElementById('filterModel').value;
      const selProp = document.getElementById('filterProp').value;
      const selState = document.getElementById('filterState').value;
      const selPay = document.getElementById('filterPayment').value;

      filteredData = RAW_DATA.filter(item => {{
        if (selModel && item.modelo !== selModel) return false;
        if (selProp && item.propulsao !== selProp) return false;
        if (selState && item.estado !== selState) return false;
        if (selPay && item.metodo_pagamento !== selPay) return false;
        return true;
      }});

      updateDashboard();
    }}

    function resetFilters() {{
      document.getElementById('filterModel').value = '';
      document.getElementById('filterProp').value = '';
      document.getElementById('filterState').value = '';
      document.getElementById('filterPayment').value = '';
      filteredData = [...RAW_DATA];
      updateDashboard();
    }}

    function updateKPIs() {{
      const totalRev = filteredData.reduce((acc, d) => acc + d.preco, 0);
      const totalVol = filteredData.length;
      const avgTicket = totalVol > 0 ? totalRev / totalVol : 0;

      const modelRev = {{}};
      filteredData.forEach(d => {{
        modelRev[d.modelo] = (modelRev[d.modelo] || 0) + d.preco;
      }});
      let topModel = '-';
      let topModelVal = 0;
      for (const [m, v] of Object.entries(modelRev)) {{
        if (v > topModelVal) {{
          topModelVal = v;
          topModel = m;
        }}
      }}

      document.getElementById('kpiTotalRevenue').textContent = formatBRL(totalRev);
      document.getElementById('kpiTotalVolume').textContent = `${{totalVol}} unidades`;
      document.getElementById('kpiAverageTicket').textContent = formatBRL(avgTicket);
      document.getElementById('kpiTopModel').textContent = topModel;
      document.getElementById('kpiTopModelVal').textContent = topModelVal > 0 ? `${{formatBRL(topModelVal)}} faturados` : '-';
    }}

    function updateCharts() {{
      // CHART 1: MODELOS (FATURAMENTO)
      const modelStats = {{}};
      filteredData.forEach(d => {{
        if (!modelStats[d.modelo]) modelStats[d.modelo] = {{ rev: 0, qtd: 0 }};
        modelStats[d.modelo].rev += d.preco;
        modelStats[d.modelo].qtd += 1;
      }});

      const sortedModels = Object.entries(modelStats).sort((a, b) => b[1].rev - a[1].rev);
      const modelLabels = sortedModels.map(s => s[0]);
      const modelRevs = sortedModels.map(s => s[1].rev);

      if (chartModelsInstance) chartModelsInstance.destroy();
      const ctxModels = document.getElementById('chartModels').getContext('2d');
      chartModelsInstance = new Chart(ctxModels, {{
        type: 'bar',
        data: {{
          labels: modelLabels,
          datasets: [{{
            label: 'Faturamento (R$)',
            data: modelRevs,
            backgroundColor: '#d5001c',
            borderRadius: 4
          }}]
        }},
        options: {{
          indexAxis: 'y',
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                label: ctx => ` Faturamento: ${{formatBRL(ctx.raw)}}`
              }}
            }}
          }},
          scales: {{
            x: {{
              ticks: {{ color: '#94a3b8', callback: val => 'R$ ' + (val/1000000).toFixed(1) + 'M' }},
              grid: {{ color: 'rgba(255,255,255,0.05)' }}
            }},
            y: {{
              ticks: {{ color: '#f8fafc', font: {{ size: 11 }} }},
              grid: {{ display: false }}
            }}
          }}
        }}
      }});

      // CHART 2: ESTADOS
      const stateStats = {{}};
      filteredData.forEach(d => {{
        stateStats[d.estado] = (stateStats[d.estado] || 0) + d.preco;
      }});
      const stateLabels = Object.keys(stateStats);
      const stateRevs = Object.values(stateStats);

      if (chartRegionsInstance) chartRegionsInstance.destroy();
      const ctxReg = document.getElementById('chartRegions').getContext('2d');
      chartRegionsInstance = new Chart(ctxReg, {{
        type: 'doughnut',
        data: {{
          labels: stateLabels,
          datasets: [{{
            data: stateRevs,
            backgroundColor: ['#d5001c', '#c5a059', '#3b82f6', '#10b981', '#8b5cf6', '#f59e0b', '#ec4899'],
            borderWidth: 2,
            borderColor: '#13151c'
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'right', labels: {{ color: '#e2e8f0', font: {{ size: 11 }} }} }},
            tooltip: {{
              callbacks: {{
                label: ctx => ` ${{ctx.label}}: ${{formatBRL(ctx.raw)}}`
              }}
            }}
          }}
        }}
      }});

      // CHART 3: MÉTODO DE PAGAMENTO X PROPULSÃO
      const payMethods = ['À Vista (TED/PIX)', 'Financiamento Bancário', 'Carta de Crédito / Consórcio'];
      const combustao = payMethods.map(p => filteredData.filter(d => d.metodo_pagamento === p && d.propulsao === 'Combustão').length);
      const eletrico = payMethods.map(p => filteredData.filter(d => d.metodo_pagamento === p && d.propulsao === 'Elétrico').length);
      const hibrido = payMethods.map(p => filteredData.filter(d => d.metodo_pagamento === p && d.propulsao === 'Híbrido').length);

      if (chartPaymentPropInstance) chartPaymentPropInstance.destroy();
      const ctxPay = document.getElementById('chartPaymentProp').getContext('2d');
      chartPaymentPropInstance = new Chart(ctxPay, {{
        type: 'bar',
        data: {{
          labels: ['À Vista', 'Financiamento', 'Consórcio'],
          datasets: [
            {{ label: 'Combustão', data: combustao, backgroundColor: '#f59e0b' }},
            {{ label: 'Elétrico', data: eletrico, backgroundColor: '#10b981' }},
            {{ label: 'Híbrido', data: hibrido, backgroundColor: '#3b82f6' }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'top', labels: {{ color: '#e2e8f0' }} }}
          }},
          scales: {{
            x: {{ ticks: {{ color: '#e2e8f0' }}, grid: {{ display: false }} }},
            y: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
          }}
        }}
      }});

      // CHART 4: LINHA MENSAL
      const monthlyRev = new Array(12).fill(0);
      filteredData.forEach(d => {{
        const m = parseInt(d.data_venda.split('-')[1], 10) - 1;
        if (m >= 0 && m < 12) monthlyRev[m] += d.preco;
      }});
      const monthNames = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];

      if (chartTimelineInstance) chartTimelineInstance.destroy();
      const ctxLine = document.getElementById('chartTimeline').getContext('2d');
      chartTimelineInstance = new Chart(ctxLine, {{
        type: 'line',
        data: {{
          labels: monthNames,
          datasets: [{{
            label: 'Faturamento Mensal (R$)',
            data: monthlyRev,
            borderColor: '#c5a059',
            backgroundColor: 'rgba(197, 160, 89, 0.15)',
            borderWidth: 3,
            fill: true,
            tension: 0.3,
            pointBackgroundColor: '#fff',
            pointRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                label: ctx => ` ${{formatBRL(ctx.raw)}}`
              }}
            }}
          }},
          scales: {{
            x: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ display: false }} }},
            y: {{
              ticks: {{ color: '#94a3b8', callback: val => 'R$ ' + (val/1000000).toFixed(1) + 'M' }},
              grid: {{ color: 'rgba(255,255,255,0.05)' }}
            }}
          }}
        }}
      }});
    }}

    function renderTable() {{
      const tbody = document.getElementById('salesTableBody');
      const search = (document.getElementById('searchInput').value || '').toLowerCase();

      const searched = filteredData.filter(d => {{
        if (!search) return true;
        return (
          d.id_venda.toLowerCase().includes(search) ||
          d.modelo.toLowerCase().includes(search) ||
          d.cidade.toLowerCase().includes(search) ||
          d.estado.toLowerCase().includes(search) ||
          d.metodo_pagamento.toLowerCase().includes(search) ||
          d.cor.toLowerCase().includes(search)
        );
      }});

      document.getElementById('tableRecordCount').textContent = searched.length;

      tbody.innerHTML = searched.map(d => {{
        let badgeClass = 'prop-combustao';
        if (d.propulsao === 'Elétrico') badgeClass = 'prop-eletrico';
        if (d.propulsao === 'Híbrido') badgeClass = 'prop-hibrido';

        return `
          <tr>
            <td><strong>${{d.id_venda}}</strong></td>
            <td>${{d.data_venda}}</td>
            <td><strong>${{d.modelo}}</strong></td>
            <td><span class="prop-badge ${{badgeClass}}">${{d.propulsao}}</span></td>
            <td>${{d.cor}}</td>
            <td>${{d.cidade}} / ${{d.estado}}</td>
            <td>${{d.ano_modelo}}</td>
            <td>${{d.metodo_pagamento}}</td>
            <td style="text-align: right; font-weight: 600; color: #fff;">${{formatBRL(d.preco)}}</td>
          </tr>
        `;
      }}).join('');
    }}

    function updateDashboard() {{
      updateKPIs();
      updateCharts();
      renderTable();
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      populateFilterOptions();
      updateDashboard();
    }});
  </script>
</body>
</html>
'''

    out_file = os.path.join("projects_workspace", "porsche-sales-dashboard", "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] index.html gerado com sucesso em: {out_file}")

if __name__ == "__main__":
    generate_html()
