### DOCUMENTO: RNF - INFRAESTRUTURA

**RNF- INFRAESTRUTURA: Luis Miguel**
*   **Projeto:** Sistema de Gestão de Perdas – Supermercado
*   **Documento:** Especificação de Requisitos Não Funcionais (RNF)
*   **Equipe Responsável:** Grupo 3 (Infraestrutura, Integrações e Segurança Técnica)
*   **Líder de Área:** Ed
*   **Data de Emissão:** 11/08/2026

---

#### 1. INTRODUÇÃO E OBJETIVO
Este documento especifica a infraestrutura necessária para suportar a **integração em tempo real** e o armazenamento de grandes volumes de dados. O foco é garantir que a "bipagem" automática e o envio de fotos de evidência não degradem a performance sistêmica, garantindo a confiabilidade dos relatórios gerados.

#### 2. DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)

| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Capacidade de Armazenamento** | Dimensionamento do servidor para banco de dados e arquivos de evidência fotográfica. | Suporte para armazenamento de fotos comprimidas vinculadas ao ID da perda por até 90 dias antes do arquivamento. |
| **Escalabilidade (RN-07)** | Capacidade de suportar o crescimento do volume de dados e multiestoques. | Arquitetura capaz de adicionar novas lojas/depósitos via configuração, sem necessidade de novo deploy de código. |
| **Resiliência e Conexão** | Mecanismo de salvamento temporário durante perda de conectividade com o servidor. | Salvar dados localmente e realizar a sincronização automática em até 2 segundos após a volta do sinal. |
| **Recuperação de Desastres** | Plano de backup automático para evitar perda de dados financeiros e operacionais. | Backups diários (às 03:00h) com tempo de restauração (RTO) máximo de 4 horas em caso de falha crítica. |

#### 3. MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
*   **RN-01 (Estoque Inteligente):** A infraestrutura suporta a atualização em tempo real, impedindo que o estoque fique negativo devido a atrasos de processamento na integração.
*   **RN-07 (Multiestoque):** Garante a separação lógica de saldos independentes por loja ou depósito dentro do mesmo banco de dados, permitindo transferências rastreáveis.

#### 4. INTEGRAÇÃO E SEGURANÇA
*   **Sistemas Externos:** O banco de dados de fotos e logs deve estar integrado via APIs com os fluxos do **PDV (Caixa)** e dos sistemas ERP legados **RMS/Totvs**.
*   **Privacidade:** O acesso aos servidores e às imagens de evidência é restrito à equipe de **TI/Segurança** e gestores autorizados, garantindo a integridade e proteção dos dados conforme perfis de acesso.

#### 5. VALIDAÇÃO DO LÍDER DE ÁREA
*   **Revisão técnica realizada por:** Ed
*   **Parecer:** ( ) Aprovado | ( ) Necessita Ajustes
*   **Notas do Líder:** __________________________________________________________________
```
