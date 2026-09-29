---
title: Identificação das Saídas, Relatórios e Registros
data_modificacao: 29/09/2026
Nome do Responsavel : Luis Miguel
escopo_sistema: Sistema de Registro de Perdas para Supermercado

---

# Identificação das Saídas e Relatórios

As principais saídas e relatórios que o sistema deverá fornecer para o acompanhamento e controle das perdas de produtos já existentes no estoque são:

- **Dashboard** com indicadores gerais de perdas em tempo real.
- **Lista de registros** de perdas cadastradas.
- **Alertas** de produtos com alto índice de perdas.
- **Consulta detalhada** das perdas por produto.
- **Gráficos comparativos** das perdas por período.
- **Comprovação visual** através de upload e visualização de fotos.
- **Exportação de relatórios** em PDF, Excel (.xlsx) e CSV.
- **Histórico completo** de perdas registradas.
- **Resumo financeiro** detalhado das perdas.

> **Regra de Comparação Temporal:** As consultas e comparativos serão realizados com base no mês anterior do sistema. Caso não haja dados para o mês anterior, o sistema focará exclusivamente no mês vigente.

---

## Detalhamento dos Relatórios de Saída

### 1. Relatório Geral de Perdas
* **Objetivo:** Apresentar todas as perdas registradas em um período de forma consolidada.
* **Informações Exibidas:**
  - Data e hora do registro
  - Produto
  - Categoria
  - Quantidade perdida
  - Preço unitário da mercadoria
  - Valor total da perda
  - Motivo da perda
  - Setor
  - Responsável pelo registro
  - **Evidência Fotográfica** (Miniatura/Link para foto de comprovação)

### 2. Relatório de Perdas por Produto
* **Objetivo:** Identificar quais produtos apresentam maior índice de perdas financeiras e quantitativas.
* **Informações Exibidas:**
  - Nome do produto
  - Quantidade total de perdas
  - Valor total perdido
  - Frequência das ocorrências
  - Motivos mais recorrentes por item

### 3. Relatório de Perdas por Setor
* **Objetivo:** Verificar quais setores do supermercado geram mais perdas para direcionar ações preventivas.
* **Exemplos de Setores:**
  - Hortifruti
  - Açougue
  - Padaria
  - Frios
  - Mercearia
  - Bebidas
* **Informações Exibidas:**
  - Total de perdas em quantidade
  - Valor total perdido
  - Produtos mais afetados no setor

### 4. Relatório por Motivo da Perda
* **Objetivo:** Identificar as principais causas raiz das perdas operacionais.
* **Exemplos de Motivos:**
  - Produto vencido
  - Avaria
  - Quebra
  - Furto
  - Armazenamento incorreto
  - **Outro** (Campo obrigatório com descrição textual detalhada)
* **Informações Exibidas:**
  - Quantidade de ocorrências por motivo
  - Valor financeiro perdido
  - Percentual de impacto de cada motivo no total geral

### 5. Relatório Financeiro
* **Objetivo:** Demonstrar o impacto financeiro direto das perdas na operação.
* **Informações Exibidas:**
  - Valor perdido por período
  - Valor perdido por setor
  - Valor perdido por categoria
  - Comparativo financeiro entre períodos (mês atual vs. mês anterior)
  - Percentual de redução ou aumento financeiro das perdas

### 6. Relatório de Auditoria
* **Objetivo:** Permitir o rastreamento rigoroso das ações realizadas pelos usuários no sistema, garantindo segurança, transparência e controle sobre os lançamentos de perdas (visto que o sistema não possui integração automática com o estoque).
* **Informações Exibidas:**
  - Nome do usuário
  - Cargo ou perfil de acesso
  - Data e hora da ação
  - Tipo de ação realizada (cadastro, edição ou exclusão)
  - Produto envolvido
  - Registro afetado
  - Endereço IP ou dispositivo (opcional)
* **Benefícios:**
  - Identificar exatamente quem registrou ou alterou uma perda
  - Evitar inserções ou alterações indevidas
  - Facilitar investigações internas em caso de divergências
  - Atender a processos internos de governança e auditoria

### 7. Relatório Comparativo por Período
* **Objetivo:** Comparar o desempenho e a evolução das perdas do supermercado ao longo do tempo.
* **Filtros Disponíveis:**
  - Diário
  - Semanal
  - Mensal
  - Trimestral
  - Anual
* **Informações Exibidas:**
  - Total geral de perdas
  - Valor financeiro acumulado
  - Produtos com maior incidência de perda no filtro selecionado
  - Setores mais críticos no período

---

## Dashboard (Painel Principal)

O sistema deverá apresentar um painel visual unificado com indicadores em tempo real:

- Total de perdas físicas do período.
- Valor financeiro total das perdas.
- Top 10 produtos com maior índice de perdas.
- Setores com maior volume financeiro de perdas.
- Principais motivos de perdas destacados em gráficos.
- Evolução das perdas por mês (gráfico de linhas comparativo).
- Distribuição percentual das perdas por categoria (gráfico de pizza).
- Comparativo direto entre as perdas do mês atual e do mês anterior.
- Percentual de redução ou aumento das perdas em relação ao ciclo anterior.

---

## Requisitos de Exportação e Comprovação

Para garantir a confiabilidade dos registros manuais de perdas (já que o sistema opera de forma independente do estoque):

1. **Comprovação por Foto:** 
   - Todo registro de perda deve obrigatório ou opcionalmente (conforme parametrização) exigir o upload de uma **foto do produto avariado/descartado** como forma de comprovação física.
   - A foto deve ficar visível na consulta detalhada e nos relatórios em PDF.
2. **Opções de Saída e Exportação:**
   - Visualização fluida na própria aplicação web.
   - Exportação estruturada em **PDF** (ótimo para impressão e reuniões de diretoria).
   - Exportação em **Excel (.xlsx) ou CSV** (ideal para análises avançadas em planilhas).
   - Funcionalidade de **impressão direta** de relatórios individuais e comprovantes.