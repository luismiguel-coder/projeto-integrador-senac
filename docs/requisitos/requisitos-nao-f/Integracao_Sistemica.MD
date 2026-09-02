# RNF - INTEGRAÇÃO SISTÊMICA

## Cabeçalho

*   **Projeto:** Sistema de Gestão de Perdas – Supermercado
*   **Documento:** Integração Sistêmica
*   **Equipe Responsável:** Grupo 3
*   **Líder de Área:** Ed
*   **Data de Emissão:** 21/08/2026

---

#### 1. INTRODUÇÃO E OBJETIVO

Este documento detalha o mapeamento de APIs do sistema de gestão de perdas e como ele se conecta com os sistemas RMS e Totvs.

#### 2. DETALHAMENTO DOS REQUISITOS

| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Mapeamento de APIs** | Documentação completa dos endpoints REST do sistema (métodos, parâmetros, respostas). Inclui especificação de cada rota, autenticação necessária, dados de entrada e saída, e exemplos de uso. |
| **Conexão com RMS** | Integração com o sistema RMS para consulta e atualização de estoque. | Sincronização de dados em até 3 segundos; 99,5% de disponibilidade do serviço. |
| **Conexão com Totvs** | Integração com o Totvs para consulta de preços de custo e venda dos produtos. | Tempo de retorno da API abaixo de 1 segundo; tratamento de erro. |
| **Autenticação entre Sistemas** | Comunicação segura entre sistemas via tokens OAuth 2.0 e HTTPS/TLS 1.3. | Tokens expirando em 1 hora; renovação automática sem intervenção manual. |
| **Logs de Integração** | Registro de todas as chamadas de API entre sistemas com status e timestamp. | Logs retidos por 12 meses; consulta de histórico abaixo de 2 segundos. |


#### 3. MAPEAMENTO DE REGRAS DE NEGÓCIO

*   **RN-01 (Estoque Inteligente):** A conexão com RMS garante atualização automática de estoque quando uma perda é registrada, evitando estoque negativo.
*   **RN-03 (Registro de Perdas):** O mapeamento de APIs permite que o PDV registre perdas diretamente, sem acesso separado ao sistema de gestão.
*   **RN-05 (Relatórios Gerenciais):** A conexão com Totvs fornece dados de preço de custo para cálculo correto do impacto financeiro das perdas.
*   **RN-09 (Auditoria):** Os logs de integração mantêm registro imutável de todas as movimentações entre sistemas para auditoria.

#### 4. INTEGRAÇÃO E SEGURANÇA

*   **Sistemas Externos:**
    *   **RMS:** Integração via API REST para consulta de estoque, produtos e movimentações. Formato de dados: JSON.
    *   **Totvs:** Integração via API REST para consulta de preços (custo e venda) e dados cadastrais de produtos. Formato de dados: JSON.
    *   **PDV (Caixa):** Integração via API REST para envio automático de dados de perda registrados no caixa.
*   **Privacidade:** Acesso às APIs restrito a servidores autorizados via whitelist de IPs. Dados sensíveis (preços, custos) criptografados conforme LGPD.
*   **Perfis de Acesso:** Integrações executadas por conta de serviço dedicada. Logs de acesso registrados separadamente dos logs de integração.

#### 5. VALIDAÇÃO DO LÍDER DE ÁREA

*   **Revisão técnica realizada por:** Ed
*   **Parecer:** (x) Aprovado | ( ) Necessita Ajustes
*   **Notas do Líder:** Documento aprovado. Todas as integrações estão de acordo com os requisitos do projeto.

lider geral:
tá ok