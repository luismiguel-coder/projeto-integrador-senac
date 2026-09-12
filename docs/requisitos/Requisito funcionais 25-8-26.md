------------------------------------------------------------------------

**1. Objetivo do Sistema**

- **Prioridade Alta:** **Reduzir as perdas de produtos** e aumentar a
  lucratividade através de um controle de estoque rigoroso.

- **Ajuste Lógico:** O sistema substitui a falha do cadastro manual pela
  **integração da "bipagem" automática** nas docas e a baixa em tempo
  real via **integração com o PDV utilizando nota fiscal por xml**.

**2. Stakeholders Envolvidos**

**Prioridade Alta (Impacto Direto):**

- **Proprietário/Gestor:** Patrocinador e decisor estratégico; aprova
  políticas e analisa o ROI.

- **Administrador do Sistema:** Gerencia a base de dados, usuários e
  configurações globais.

- **Operador de Estoque (Estoquista):** Executa a "bipagem" e o registro
  diário de movimentações e avarias.

**Prioridade Média (Suporte e Auditoria):**

- **Analista de Prevenção de Perdas:** Analisa dados, identifica riscos
  e acompanha o desempenho.

- **Fornecedor:** Responsável pela entrega física e emissão de Notas
  Fiscais (dados de entrada).

- **Controle de Qualidade:** Fiscaliza fisicamente e autoriza os
  descartes.

- **Auditor/Contador:** Valida a conformidade financeira e
  rastreabilidade.

- **TI/Segurança:** Garante a infraestrutura, backups e integridade dos
  dados.

**Prioridade Alta:**

- **Cliente Final:** Beneficiário com produtos em bom estado e dentro da
  validade.

**3. Mapeamento de Processos**

- **Prioridade Média — Processo Atual:** Cadastro manual incompleto,
  resultando em relatórios imprecisos e perdas não rastreadas.

- **Prioridade Alta — Processo Futuro:** Automação via bipagem na
  entrada e integração PDV na saída, com fluxo estruturado de
  identificação, registro e aprovação.

**4. Regras de Negócio (RN)**

**Prioridade Alta:**

- **RN-01:** Estoque Inteligente (proibição de saldo negativo e
  definição de limites).

- **RN-02:** Classificação obrigatória como Entrada, Saída ou Ajuste.

- **RN-03:** Dados obrigatórios (Data e hora exata, ID do usuário, lote,
  validade e justificativa).

- **RN-06:** Controle de acesso rígido por perfil de usuário.

- **RN-10:** Regra **FEFO**, bloqueio de itens vencidos no PDV e
  investigação de divergências \> 5%.

**Prioridade Média:**

- **RN-04:** Cálculo automático de Custo Médio Ponderado.

- **RN-05:** Notificações via Dashboard, E-mail e WhatsApp para
  anomalias.

**Prioridade Baixa:**

- **RN-07:** Suporte a multiestoque e transferências entre depósitos.

**5. Notificações e Alertas (IA)**

- **Prioridade Alta — Vencimentos:** Alertas proativos de 5, 15, 20 e 30
  dias.

- **Prioridade Média — Risco Financeiro:** IA prioriza alertas para
  produtos de alto valor agregado próximos ao vencimento.

- **Prioridade Média — Operacional e Promoções:** Baixa rotatividade,
  excesso de estoque e queda anormal de vendas. Com sugestões
  automáticas de descontos para acelerar o giro.

- **Prioridade Baixa — Segurança:** Identificação de saídas excessivas
  (desvios/furtos) e lotes críticos.

**6. Integrações com Outros Sistemas**

- **Prioridade Alta — PDV (Caixa):** Registro automático de saídas para
  estoque em tempo real.

- **Prioridade Média — ERP Corporativo:** Integração com os sistemas RMS
  e Totvs.

**7. Permissões e Perfis de Acesso**

- **Prioridade Alta — Gerente/Supervisor:** Acesso total, incluindo
  gestão de usuários, preços e aprovações.

- **Prioridade Alta — Estoquista:** Registro de entradas
  (bipagem),alteração saídas e conferência de validade.

- **Prioridade Média — Analista:** Visualização de relatórios
  financeiros, desempenho e análise de riscos.

**8. Entradas de Dados e Saídas/Relatórios**

- **Prioridade Alta — Entradas:** Código, nome, quantidade, motivo,
  setor, responsável, valor e evidência fotográfica.

- **Prioridade Alta — Saídas:** Dashboards em tempo real e **Relatórios
  de Auditoria** com log de ações por usuário e horário.

**9. Casos de Uso Principais (UC)**

**Prioridade Alta:**

- **UC01:** Autenticar usuário.

- **UC02:** Registrar entrada automática via bipagem (Novo processo
  sugerido).

- **UC03:** Registrar ocorrência de perda (Manual/IA).

- **UC04:** Analisar ocorrência de perda.

- **UC05:** Aprovar ou Rejeitar ocorrência.

- **UC06:** Consultar histórico de perdas com filtros detalhados.

- **UC07:** Visualizar indicadores de desempenho e dashboards.

- **UC08:** Gerar relatórios (PDF/Excel).

**Prioridade Média:**

- **UC09:** Receber alertas de risco (IA/Sistema).

- **UC10:** Gerenciar usuários e permissões (Administrador).

**10. Fluxo de Aprovação de Perdas**

**Prioridade Alta:**

1.  **Registro:** Colaborador identifica e insere a perda.

2.  **Validação:** Sistema verifica obrigatoriedade dos campos e
    evidências.

3.  **Análise:** Analista de prevenção revisa os dados em busca de
    inconsistências.

4.  **Decisão:** Supervisor aprova, rejeita ou solicita correção.

5.  **Atualização:** Baixa definitiva no estoque e atualização
    financeira nos indicadores.

**11. Exceções e Tratamentos de Erro**

- **Prioridade Alta:** Bloqueio de dados inconsistentes (vencimento
  retroativo, quantidade negativa).

- **Prioridade Média:** Falha na "bipagem" (opção de cadastro manual com
  justificativa).

- **Prioridade Média:** Auditoria de todas as exclusões ou ajustes via
  histórico imutável.

- **Prioridade Baixa:** Resiliência de conexão (salvamento local e
  restauração automática).
