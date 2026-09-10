---
title: Levantamento de Requisito
---

Este documento consolida o levantamento de requisitos para o
desenvolvimento do sistema de gerenciamento de supermercado, com foco na
**redução de perdas e integração de Inteligência Artificial (IA)** para
otimização de resultados.

------------------------------------------------------------------------

**1. Objetivo do Sistema**

O objetivo central é **reduzir as perdas de produtos**, minimizando
prejuízos por vencimento e aumentando a lucratividade através de um
controle de estoque eficiente. O sistema visa solucionar a falha atual
de cadastros incompletos, integrando a "bipagem" automática no
recebimento de mercadorias nas docas e a baixa em tempo real no Ponto de
Venda (PDV).

**2. Stakeholders Envolvidos**

O projeto envolve oito perfis principais que interagem com o ecossistema
do supermercado:

- **Proprietário/Gestor:** Decisor estratégico que aprova políticas e
  analisa resultados.

- **Administrador do Sistema:** Gerencia cadastros de produtos, usuários
  e configurações.

- **Operador de Estoque:** Realiza registros diários, conferência de
  validade e identifica itens danificados.

- **Controle de Qualidade:** Fiscaliza perdas e autoriza descartes.

- **Fornecedor:** Responsável pela entrega e emissão de notas fiscais.

> **(A frase está ambígua.)**

- **Cliente Final:** Beneficiário de produtos dentro do prazo e em bom
  estado.

> **(??**)

- **Auditor/Contador:** Valida a conformidade financeira e
  rastreabilidade.

- **TI/Segurança:** Garante a integridade dos dados e backups.

**3. Mapeamento de Processos**

- **Processos Atuais:** O cadastro é manual e muitas vezes incompleto,
  resultando em relatórios de prejuízo estimados que não refletem a
  realidade total do estoque.

- **Processos Futuros:** Implementação de automação total via "bipagem"
  na entrada e integração direta com o caixa (PDV) para atualização
  instantânea. O fluxo de perdas incluirá identificação (vencimento,
  dano, furto), registro detalhado, validação pelo gestor, baixa
  automática e análise de causas para ações corretivas.

**4. Regras de Negócio (RN)**

As diretrizes que regem o sistema incluem:

- **RN-01 (Estoque Inteligente):** O estoque nunca deve ser negativo e
  exige definição de quantidades mínimas e máximas.

- **RN-02 (Classificação):** Toda movimentação deve ser rotulada como
  Entrada, Saída ou Ajuste.

- **RN-03 (Dados Obrigatórios):** Todo registro exige data, hora, ID do
  usuário, lote, validade e justificativa.

- **RN-04 (Custo Médio):** Cálculo automático do custo médio ponderado a
  cada nova entrada.

> **(Melhorar a clareza da frase.)**

- **RN-05 (Alertas):** Notificações via Dashboard, E-mail e WhatsApp
  para anomalias.

> **( A frase pode ser escrita de forma mais clara.)**

- **RN-06 e RN-07:** Controle de acesso por perfil e suporte a multe
  estoque/transferências entre unidades.

- **RN-10 (Validade e Perdas):** Aplicação da regra **FEFO** (vende
  primeiro o que vence antes), bloqueio de itens vencidos e investigação
  imediata de divergências físicas superiores a 5%.

**5. Notificações e Alertas (Foco em IA)**

A Inteligência Artificial identificará padrões de perda e gerará alertas
preventivos:

- **Vencimentos:** Alertas programados para 7, 30, 60 e 90 dias antes do
  vencimento.

- **Risco Financeiro:** Priorização de alertas para produtos de alto
  valor perto de vencer.\
  ( **Melhorar a frase, pois ela está desconectada do que está sendo
  proposto.**)

- **Operacional:** Alertas de baixa rotatividade, excesso de estoque,
  estoque mínimo e queda anormal de vendas.

> **( Esse é um dos nossos principais objetivos.)**

- **Segurança:** Sinalização de saídas excessivas (possíveis furtos ou
  erros) e lotes críticos.

- **Promoções:** Sugestões automáticas de descontos para acelerar o giro
  de itens próximos ao vencimento.

**6. Integrações com Outros Sistemas**

O sistema deverá ser totalmente compatível e integrado com:

- **Sistemas ERP:** RMS e Totvs.

- **PDV (Ponto de Venda):** Para registro automático de saídas e
  atualização de estoque em tempo real.

**7. Permissões e Perfis de Acesso**

O acesso é segmentado conforme a função:

- **Gerente/Supervisor:** Acesso total, gerencia usuários, configura
  preços, aprova ocorrências e visualiza relatórios financeiros.\
  ( As informações não estão condizentes com o que foi proposto lá em
  cima.)

- **Analista de Prevenção:** Analisa dados de desempenho, identifica
  riscos e gera relatórios personalizados, mas não gerencia usuários.

- **Estoquista/Colaborador:** Registra entradas, saídas e ocorrências de
  perda, além de conferir validades.

> **( Esse é um dos nossos principais objetivos.)**

**8. Entradas de Dados e Saídas/Relatórios**

- **Entradas:** Código e nome do produto, quantidade, motivo da perda
  (vencimento, avaria, furto, etc.), setor, responsável, valor unitário
  e evidência fotográfica.

- **Saídas e Relatórios:** Dashboards em tempo real com indicadores
  gerais. Relatórios detalhados por período, produto, setor, motivo e
  financeiro. Inclui relatórios de auditoria para rastrear ações de
  usuários e exportação em PDF/Excel.

**9. Casos de Uso Principais**

O sistema é estruturado nos seguintes casos de uso:

- **UC01:** Autenticar usuário.

- **(Está faltando a parte referente ao cadastro dos produtos.)**

- **UC02:** Registrar ocorrência de perda.

- **UC03/UC04:** Analisar e Aprovar/Rejeitar ocorrências.

- **UC05/UC06/UC07:** Consultar histórico, visualizar indicadores e
  gerar relatórios.

- **UC08:** Receber alertas de risco (IA).

- **UC09:** Gerenciar usuários e permissões.

**10. Fluxo de Aprovação de Perdas**

O processo de validação segue cinco etapas:

1.  **Registro:** Colaborador insere a perda.

2.  **Validação:** Sistema verifica preenchimento de campos
    obrigatórios.

3.  **Análise:** Analista de prevenção revisa inconsistências.

4.  **Decisão:** Supervisor aprova, rejeita ou solicita correção.

5.  **Atualização:** Dados são contabilizados e os dashboards
    atualizados após a aprovação.

**11. Exceções e Tratamentos de Erro**

Para garantir a resiliência, o sistema prevê:

- **Falha na Bipagem:** Opção de cadastro manual com registro de
  justificativa e responsável.

- **Dados Inconsistentes:** Bloqueio de vencimentos retroativos,
  quantidades negativas ou valores inválidos.

- **Falhas Técnicas:** Registro de erros de integração com PDV, quedas
  de banco de dados e tentativas de acesso não autorizado.

- **Conectividade:** Salvamento temporário de informações durante perda
  de conexão com restauração automática.

- **Auditoria:** Histórico imutável de todas as inclusões, exclusões e
  ajustes.

**(A frase está ambígua.)**

**Minhas considerações**

Com base na minha análise, estes são alguns dos pontos que precisam ser
melhorados. Também é necessário acrescentar a informação de que os
registros das movimentações devem conter a **data e o horário exatos em
que a movimentação ocorreu**, garantindo maior rastreabilidade e
controle das operações.\
\
Os pontos destacados em **vermelho** devem ser corrigidos, enquanto os
pontos destacados em **laranja** devem ser melhor conectados ao contexto
do documento.
