# Levantamento de Requisito

Este documento consolida o levantamento de requisitos para o desenvolvimento do sistema de gerenciamento de supermercado, com foco na redução de perdas e integração de Inteligência Artificial (IA) para otimização de resultados.

---

## 1. Objetivo do Sistema

O objetivo central é **reduzir as perdas de produtos**, minimizando prejuízos por vencimento e aumentando a lucratividade através de um controle de estoque eficiente. O sistema visa solucionar a falha atual de cadastros incompletos, integrando a "bipagem" automática no recebimento de mercadorias nas docas e a baixa em tempo real no Ponto de Venda (PDV).

## 2. Stakeholders Envolvidos

O projeto envolve **oito perfis principais** que interagem com o ecossistema do supermercado:

- **Prioridade Alta** — **Proprietário/Gestor**: Decisor estratégico que aprova políticas e analisa resultados. — **porque** decide e aprova as perdas registradas.
- **Prioridade Alta** — **Administrador do Sistema**: Gerencia cadastros de produtos, usuários e configurações. — **porque** mantém a base de dados que todo o sistema usa.
- **Prioridade Alta** — **Operador de Estoque**: Realiza registros diários, conferência de validade e identifica itens danificados. — **porque** é quem registra as perdas no dia a dia.
- **Prioridade Média** — **Controle de Qualidade**: Fiscaliza perdas e autoriza descartes.
- **Prioridade Média** — **Fornecedor**: Responsável pela entrega e emissão de notas fiscais.
- **Prioridade Baixa** — **Cliente Final**: Beneficiário de produtos dentro do prazo e em bom estado.
- **Prioridade Média** — **Auditor/Contador**: Valida a conformidade financeira e rastreabilidade.
- **Prioridade Média** — **TI/Segurança**: Garante a integridade dos dados e backups.

## 3. Mapeamento de Processos

- **Prioridade Media** — **Processos Atuais**: O cadastro é **manual e muitas vezes incompleto**, resultando em relatórios de prejuízo estimados que não refletem a realidade total do estoque.

- **Prioridade Media** — **Processos Futuros**: Implementação de **automação total via "bipagem"** na entrada e integração direta com o caixa (**PDV**) para atualização instantânea. O fluxo de perdas incluirá **identificação** (vencimento, dano, furto), **registro detalhado**, **validação pelo gestor**, **baixa automática** e **análise de causas** para ações corretivas. — **porque** automatiza a entrada e mantém o estoque atualizado, base para reduzir perdas.

## 4. Regras de Negócio (RN)

As diretrizes que regem o sistema incluem:

- **Prioridade Alta** — **RN-01 (Estoque Inteligente)**: O estoque nunca deve ser negativo e exige definição de quantidades mínimas e máximas. — **porque** impede estoque negativo e evita divergências.
- **Prioridade Alta** — **RN-02 (Prioridade)**: Toda movimentação deve ser rotulada como Entrada, Saída ou Ajuste. — **porque** garante relatórios e cálculos corretos.
- **Prioridade Alta** — **RN-03 (Dados Obrigatórios)**: Todo registro exige data, hora, ID do usuário, lote, validade e justificativa. — **porque** resolve a falha atual de cadastro incompleto.
- **Prioridade Média** — **RN-04 (Custo Médio)**: Cálculo automático do custo médio ponderado a cada nova entrada.
- **Prioridade Média** — **RN-05 (Alertas)**: Notificações via Dashboard, E-mail e WhatsApp para anomalias.
- **Prioridade Alta** — **RN-06**: Controle de acesso por perfil. — **porque** garante que cada usuário faça só o que é permitido.
- **Prioridade Baixa** — **RN-07**: Suporte a multiestoque/transferências entre unidades.
- **Prioridade Alta** — **RN-10 (Validade e Perdas)**: Aplicação da regra FEFO (vende primeiro o que vence antes), bloqueio de itens vencidos e investigação imediata de divergências físicas superiores a 5%. — **porque** ataca diretamente a maior causa de perda, o vencimento.

## 5. Notificações e Alertas (Foco em IA)

A Inteligência Artificial identificará **padrões de perda** e gerará alertas preventivos:

- **Prioridade Alta** — **Vencimentos**: Alertas programados para 7, 30, 60 e 90 dias antes do vencimento. — **porque** evita a maior causa de perda, o produto vencido.
- **Prioridade Média** — **Risco Financeiro**: Priorização de alertas para produtos de alto valor perto de vencer.
- **Prioridade Média** — **Operacional**: Alertas de baixa rotatividade, excesso de estoque, estoque mínimo e queda anormal de vendas.
- **Prioridade Baixa** — **Segurança**: Sinalização de saídas excessivas (possíveis furtos ou erros) e lotes críticos.
- **Prioridade Baixa** — **Promoções**: Sugestões automáticas de descontos para acelerar o giro de itens próximos ao vencimento.

## 6. Integrações com Outros Sistemas

O sistema deverá ser **totalmente compatível e integrado** com:

- **Prioridade Média** — **Sistemas ERP**: RMS e Totvs.
- **Prioridade Alta** — **PDV (Ponto de Venda)**: Para registro automático de saídas e atualização de estoque em tempo real. — **porque** mantém o estoque sempre atualizado nas vendas.

## 7. Permissões e Perfis de Acesso

O acesso é **segmentado conforme a função**:

- **Prioridade Alta** — **Gerente/Supervisor**: Acesso total, gerencia usuários, configura preços, aprova ocorrências e visualiza relatórios financeiros. — **porque** aprova as perdas e administra o sistema.
- **Prioridade Média** — **Analista de Prevenção**: Analisa dados de desempenho, identifica riscos e gera relatórios personalizados, mas não gerencia usuários.
- **Prioridade Alta** — **Estoquista/Colaborador**: Registra entradas, saídas e ocorrências de perda, além de conferir validades. — **porque** é quem faz os registros diários de perdas.

## 8. Entradas de Dados e Saídas/Relatórios

- **Prioridade Alta** — **Entradas**: Código e nome do produto, quantidade, motivo da perda (vencimento, avaria, furto, etc.), setor, responsável, valor unitário e evidência fotográfica. — **porque** sem esses dados não há registro correto de perdas.
- **Prioridade Alta** — **Saídas e Relatórios**: Dashboards em tempo real com indicadores gerais. Relatórios detalhados por período, produto, setor, motivo e financeiro. Inclui relatórios de auditoria para rastrear ações de usuários e exportação em PDF/Excel. — **porque** mostram se as perdas estão caindo e ajudam na decisão.

## 9. Casos de Uso Principais

O sistema é estruturado nos seguintes casos de uso:

- **Prioridade Alta** — **UC01**: Autenticar usuário. — **porque** todo acesso ao sistema exige login seguro.
- **Prioridade Alta** — **UC02**: Registrar ocorrência de perda. — **porque** é a função principal do sistema.
- **Prioridade Alta** — **UC03/UC04**: Analisar e Aprovar/Rejeitar ocorrências. — **porque** garante controle e rastreabilidade das perdas.
- **Prioridade Alta** — **UC05/UC06/UC07**: Consultar histórico, visualizar indicadores e gerar relatórios. — **porque** mostram o histórico e os indicadores de perdas.
- **Prioridade Média** — **UC08**: Receber alertas de risco (IA).
- **Prioridade Média** — **UC09**: Gerenciar usuários e permissões.

## 10. Fluxo de Aprovação de Perdas

O processo de validação segue **cinco etapas**:

1. **Prioridade Alta** — **Registro**: Colaborador insere a perda. — **porque** é onde a perda entra no sistema.
2. **Prioridade Alta** — **Validação**: Sistema verifica preenchimento de campos obrigatórios. — **porque** impede registros incompletos.
3. **Prioridade Alta** — **Análise**: Analista de prevenção revisa inconsistências. — **porque** garante que só perdas reais sejam baixadas.
4. **Prioridade Alta** — **Decisão**: Supervisor aprova, rejeita ou solicita correção. — **porque** só com aprovação a perda é contabilizada.
5. **Prioridade Alta** — **Atualização**: Dados são contabilizados e os dashboards atualizados após a aprovação. — **porque** mantém os indicadores sempre corretos.

## 11. Exceções e Tratamentos de Erro

Para garantir a resiliência, o sistema prevê:

- **Prioridade Média** — **Falha na Bipagem**: Opção de cadastro manual com registro de justificativa e responsável.
- **Prioridade Alta** — **Dados Inconsistentes**: Bloqueio de vencimentos retroativos, quantidades negativas ou valores inválidos. — **porque** evita que erros corrompam todo o estoque.
- **Prioridade Média** — **Falhas Técnicas**: Registro de erros de integração com PDV, quedas de banco de dados e tentativas de acesso não autorizado.
- **Prioridade Baixa** — **Conectividade**: Salvamento temporário de informações durante perda de conexão com restauração automática.
- **Prioridade Média** — **Auditoria**: Histórico imutável de todas as inclusões, exclusões e ajustes.