# RNF - CARGA E RESILIÊNCIA

## Cabeçalho

*   **Projeto:** Sistema de Gestão de Perdas – Supermercado
*   **Documento:** Carga e ResiliÊncia
*   **Equipe Responsável:** Grupo 3
*   **Líder de Área:** Ed
*   **Data de Emissão:** 24/08/2026

---

#### 1. INTRODUÇÃO E OBJETIVO

Este documento detalha a capacidade de suporte a múltiplos usuários simultâneos, o volume de dados tratado pelo sistema e o plano de backup/recuperação para garantir continuidade operacional.

#### 2. DETALHAMENTO DOS REQUISITOS

| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Quantidade de Usuários Simultâneos** | Suporte a múltiplos operadores registrando perdas ao mesmo tempo em diferentes caixas. | Sistema deve suportar 20 usuários simultâneos com tempo de resposta abaixo de 2 segundos. |
| **Volume de Dados** | Suporte ao crescimento do banco de dados ao longo do tempo. | Armazenamento de até 500GB de dados operacionais e 2TB de evidências fotográficas de produtos por ano. |
| **Plano de Backup** | Cópia de segurança dos dados do sistema em intervalos regulares. | Backups completos diários às 03:00h; backups incrementais a cada 4 horas. |
| **Plano de Recuperação** | Restauração do sistema em caso de falha crítica ou perda de dados. | Tempo máximo de restauração de 4 horas; ponto de restauração máximo de 1 hora. |
| **Performance Sob Carga** | Manutenção da resposta do sistema em horários de pico. | Tempo de resposta abaixo de 3 segundos para 95% das requisições com 80% da capacidade máxima. |
| **Tolerância a Falhas** | Continuidade do serviço mesmo com falhas parciais de componentes. | Disponibilidade de 99,5% do sistema durante horário comercial (08h às 22h). |

#### 3. MAPEAMENTO DE REGRAS DE NEGÓCIO

*   **RN-01 (Estoque Inteligente):** A capacidade de múltiplos usuários simultâneos garante que perdas sejam registradas em tempo real sem atrasos, mantendo estoque atualizado.
*   **RN-06 (Relatórios):** A resiliência assegura que dados de relatórios gerenciais estejam disponíveis mesmo após falhas, preservando informações financeiras.
*   **RN-08 (Multi-usuário):** O suporte a 20 usuários simultâneos atende a operação de múltiplos caixas e depósitos em horário de pico.
*   **RN-09 (Auditoria):** O backup diário garante preservação de logs e registros para auditoria conforme política de retenção.

#### 4. INTEGRAÇÃO E SEGURANÇA

*   **Sistemas Externos:** O backup dos dados deve incluir integrações com RMS/Totvs, garantindo consistência entre sistemas em caso de restauração.
*   **Privacidade:** Backups criptografados com o padrao de criptografia AES-256 e armazenados em local seguro com acesso restrito à equipe de TI, conforme LGPD.
*   **Testes de Restauração:** Restauração simulada realizada mensalmente para validar integridade dos backups e cumprimento do RTO.

#### 5. VALIDAÇÃO DO LÍDER DE ÁREA

*   **Revisão técnica realizada por:** Ed
*   **Parecer:** ( ) Aprovado | ( ) Necessita Ajustes
*   **Notas do Líder:** Parcialmente aprovado.
lider geral:
tá ok
