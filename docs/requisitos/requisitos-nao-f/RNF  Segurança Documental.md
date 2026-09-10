**DOCUMENTO: ENTREGA RNF**

RNF Segurança Documental: Luis Miguel

- **Projeto:** Sistema de Gestão de Perdas – Supermercado

- **Documento:** Especificação de Requisitos Não Funcionais (RNF)

- **Equipe Responsável:** Grupo 1 (Documentação e Regras Legais)

- **Líder de Área:** Emilly

- **Data de Emissão:** 11/08/2026

------------------------------------------------------------------------

1.  **INTRODUÇÃO E OBJETIVO**

Este documento estabelece as diretrizes de **Segurança Documental e
Rastreabilidade**. O objetivo é garantir que o sistema opere em
conformidade com a LGPD e mantenha um histórico imutável de todas as
ações, eliminando a falha atual de cadastros incompletos e protegendo a
empresa contra fraudes.

**2. DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)**

| **Requisito (RNF)** | **Descrição do Funcionamento** | **Métrica/Indicador de Sucesso** |
|----|----|----|
| **Auditoria e Rastreabilidade** | Registro automático de qualquer transação (C.R.U.D) realizada no banco de dados. | Gravação imutável de: ID do usuário, IP, Data e Hora exata (milisegundos) de cada alteração. |
| **Conformidade LGPD** | Proteção de dados sensíveis e controle de acesso baseado em funções (RBAC). | Criptografia (AES-256) em repouso para dados de identificação; Acesso restrito a Gerentes e Administradores. |
| **Integridade de Registro** | Bloqueio de entradas de dados que corrompam a lógica do negócio. | Impedir salvamento de vencimentos retroativos ou quantidades negativas em 100% das tentativas. |

**3. MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)**

- **RN-03 (Dados Obrigatórios):** O sistema captura automaticamente o
  carimbo de tempo e o autor da ação, garantindo que nenhum registro de
  perda seja "anônimo".

- **RN-09 (Segurança):** Criação de um histórico imutável onde ajustes
  de estoque só podem ser feitos mediante justificativa e registro de
  log.

- **RN-10 (Investigação):** Fornece a base de dados para investigar
  imediatamente qualquer divergência física superior a 5% detectada
  entre o sistema e o balanço.

**4. INTEGRAÇÃO E SEGURANÇA**

- **Sistemas Externos:** Os logs de auditoria são estruturados para
  permitir cruzamento com os relatórios de saída dos ERPs **RMS/
  Totvs**.

- **Privacidade:** O sistema implementa uma barreira onde o
  **Estoquista** visualiza apenas o estoque, enquanto o **Gerente**
  visualiza o custo financeiro total das perdas.

**5. VALIDAÇÃO DO LÍDER DE ÁREA**

- **Revisão técnica realizada por:** Emilli

- **Parecer:** ( ) Aprovado \| ( ) Necessita Ajustes

- **Notas do Líder:**
  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
