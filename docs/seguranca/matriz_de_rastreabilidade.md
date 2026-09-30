# Matriz de Rastreabilidade (Telas / Requisitos vs. Banco de Dados)

**Projeto:** Sistema de Registro de Perdas para Supermercado  
**Documento:** Matriz de Rastreabilidade de Requisitos de Software  
**Responsável Técnico:** Luis Miguel  
**Data:** 29/09/2026  

---

## 1. Visão Geral
Esta Matriz de Rastreabilidade vincula cada **Requisito de Tela / Interface (Frontend PWA/Mobile e Web)** diretamente às **Tabelas, Campos e Chaves do Banco de Dados Relacional (PostgreSQL/MySQL)** no backend Python, garantindo 100% de cobertura técnica e ausência de dados órfãos.

---

## 2. Matriz de Mapeamento (Tela vs. Banco de Dados)

| ID Tela | Nome da Tela / Funcionalidade | Elementos de Entrada / Exibição na Tela | Tabela do Banco de Dados | Campos e Atributos Vinculados | Tipo & Regras de Banco |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TEL-01** | **Tela de Login / Autenticação** | - Campo Usuário / Matrícula<br>- Campo Senha<br>- Botão Entrar | `tb_usuarios` | `id`<br>`login`<br>`senha_hash`<br>`nome`<br>`cargo`<br>`perfil_id`<br>`status` | `PK, Serial`<br>`VARCHAR(50), UNIQUE`<br>`VARCHAR(255) (Bcrypt)`<br>`VARCHAR(100)`<br>`VARCHAR(50)`<br>`FK -> tb_perfis(id)`<br>`BOOLEAN (DEFAULT True)` |
| **TEL-01B** | **Gestão de Perfis (RBAC)** | - Seleção dos 3 Perfis:<br>  1. Operador de Loja<br>  2. Supervisor de Setor<br>  3. Gerente/Admin | `tb_perfis` | `id`<br>`nome_perfil`<br>`descricao`<br>`nivel_permissao` | `PK, Integer`<br>`VARCHAR(30) (Operador/Supervisor/Gerente)`<br>`TEXT`<br>`INTEGER` |
| **TEL-02** | **Cadastro de Produtos** | - Código do Produto (SKU/EAN)<br>- Nome/Descrição<br>- Categoria (Dropdown)<br>- Preço Custo / Venda<br>- Unidade de Medida | `tb_produtos` | `id`<br>`codigo_barras`<br>`nome`<br>`categoria_id`<br>`preco_custo`<br>`unidade_medida`<br>`status` | `PK, Serial`<br>`VARCHAR(50), UNIQUE`<br>`VARCHAR(150)`<br>`FK -> tb_categorias(id)`<br>`DECIMAL(10,2)`<br>`VARCHAR(10) (UN, KG, L)`<br>`BOOLEAN (Soft Delete)` |
| **TEL-03** | **Cadastro de Setores** | - Nome do Setor<br>- Responsável pelo Setor | `tb_setores` | `id`<br>`nome_setor`<br>`responsavel`<br>`status` | `PK, Serial`<br>`VARCHAR(100)`<br>`VARCHAR(100)`<br>`BOOLEAN (Soft Delete)` |
| **TEL-04** | **Cadastro de Motivos de Perda** | - Título do Motivo<br>- Status (Ativo/Inativo) | `tb_motivos_perda` | `id`<br>`titulo_motivo`<br>`status` | `PK, Serial`<br>`VARCHAR(100)`<br>`BOOLEAN (Preserva Histórico)` |
| **TEL-05** | **Formulário de Lançamento de Perda** | - Data e Hora (Automático)<br>- Produto (Busca/Scanner)<br>- Setor (Dropdown)<br>- Quantidade Perdida<br>- Preço Unitário<br>- Valor Total (Calculado)<br>- Motivo (Dropdown)<br>- Descrição "Outro"<br>- Anexo de Foto (Câmera)<br>- Responsável (Sessão) | `tb_lancamentos_perda` | `id`<br>`data_hora`<br>`produto_id`<br>`setor_id`<br>`quantidade`<br>`preco_unitario`<br>`valor_total`<br>`motivo_id`<br>`descricao_outro`<br>`foto_url`<br>`usuario_id`<br>`status_registro` | `PK, Serial`<br>`TIMESTAMP (DEFAULT NOW())`<br>`FK -> tb_produtos(id)`<br>`FK -> tb_setores(id)`<br>`DECIMAL(10,3) CHECK (>0)`<br>`DECIMAL(10,2)`<br>`DECIMAL(10,2)`<br>`FK -> tb_motivos_perda(id)`<br>`TEXT (Obrigatório se motivo=Outro)`<br>`VARCHAR(255) (Path da Imagem)`<br>`FK -> tb_usuarios(id)`<br>`VARCHAR(20) (Ativo/Cancelado)` |
| **TEL-06** | **Dashboard / Painel Principal** | - Total de Perdas físicas<br>- Valor acumulado R$<br>- Top 10 Produtos em Perda<br>- Gráfico Perdas por Setor<br>- Gráfico Perdas por Motivo<br>- Comparativo Mês Atual vs Anterior | `vw_dashboard_perdas` *(View SQL SQL Agregada)* | Consultas dinâmicas sobre:<br>`tb_lancamentos_perda`<br>`tb_produtos`<br>`tb_setores`<br>`tb_motivos_perda` | Views agregadas com `SUM()`, `COUNT()`, `GROUP BY` filtradas por `data_hora` e `status_registro = 'Ativo'` |
| **TEL-07** | **Relatórios de Saída (PDF/Excel)** | - Filtros (Data, Setor, Produto)<br>- Tabela consolidada<br>- Exportar PDF / Excel / CSV | `vw_relatorios_consolidados` *(View SQL)* | Joins de `tb_lancamentos_perda` com `tb_produtos`, `tb_setores`, `tb_motivos_perda` e `tb_usuarios` | Agrupamento por filtros de período e geração de arquivos no Python (`Pandas` / `ReportLab`) |
| **TEL-08** | **Relatório de Auditoria** | - Histórico de Ações (C.R.U.D)<br>- Usuário / Perfil<br>- Data/Hora Exata<br>- Ação Realizada<br>- Registro Afetado<br>- IP / Dispositivo | `tb_logs_auditoria` | `id`<br>`usuario_id`<br>`acao`<br>`tabela_afetada`<br>`registro_id`<br>`data_hora`<br>`ip_origem`<br>`dispositivo`<br>`dados_anteriores`<br>`dados_novos` | `PK, BigSerial`<br>`FK -> tb_usuarios(id)`<br>`VARCHAR(20) (INSERT/UPDATE/DELETE)`<br>`VARCHAR(50)`<br>`BIGINT`<br>`TIMESTAMP (Com Milissegundos)`<br>`VARCHAR(45)`<br>`VARCHAR(255)`<br>`JSONB (Dump antes)`<br>`JSONB (Dump depois)` |

---

## 3. Regras de Integridade Referencial e Chaves
1. **Exclusão Lógica (*Soft Delete*):** Nenhuma tabela principal (`tb_produtos`, `tb_setores`, `tb_motivos_perda`, `tb_usuarios`) possui comando `DELETE` liberado. A exclusão altera apenas a coluna `status = False`.
2. **Histórico Imutável:** A tabela `tb_logs_auditoria` é de escrita única (*Append-Only*). Nem mesmo o usuário Gerente possui permissão de `UPDATE` ou `DELETE` nesta tabela.
