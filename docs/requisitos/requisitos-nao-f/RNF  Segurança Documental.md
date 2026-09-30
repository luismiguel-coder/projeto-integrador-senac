# Especificação de Requisitos Não Funcionais (RNF) - Segurança Documental, LGPD e Rastreabilidade

**Projeto:** Sistema de Registro e Gestão de Perdas – Supermercado  
**Documento:** Especificação de Requisitos Não Funcionais (RNF - Segurança Documental)  
**Equipe Responsável:** Grupo 1 (Documentação, Segurança e Regras Legais)  
**Responsável Técnico:** Luis Miguel  
**Data de Atualização:** 29/09/2026  

---

### 1. Introdução e Objetivo
Este documento estabelece as diretrizes de **Segurança Documental, Rastreabilidade e Conformidade com a LGPD** para o **Sistema de Registro de Perdas**. Como o sistema opera de forma autônoma e independente (*standalone*, em Python), o objetivo principal é garantir um **histórico imutável de todas as ações**, proteger os dados de acesso e mídias anexadas, e impedir lançamentos anônimos ou fraudulentos, fornecendo suporte completo para auditorias internas e governança.

---

### 2. Tabela Detalhada de Requisitos Não Funcionais (RNF)

| Requisito (RNF) | Descrição do Funcionamento Técnico | Métrica / Indicador de Sucesso |
| :--- | :--- | :--- |
| **Auditoria e Rastreabilidade (Logs Imutáveis)** | Gravação automática e imutável no banco de dados de qualquer operação (C.R.U.D) realizada em lançamentos de perdas, usuários ou cadastros base. | Registro inviolável contendo: ID e login do usuário, perfil/cargo, IP, dispositivo, data/hora exata com milissegundos e dados antes/depois da alteração. |
| **Conformidade LGPD e Proteção de Dados** | Proteção dos dados de identificação dos funcionários/operadores e das fotos de comprovação armazenadas. | Criptografia de senhas com hash forte (Bcrypt/Argon2); criptografia AES-256 em repouso para dados sensíveis; controle estrito de acesso baseado em funções (RBAC). |
| **Integridade de Registro e Validações** | Validação automática no backend (Python) para impedir entradas incorretas ou que corrompam a lógica financeira/operacional. | Bloqueio de 100% das tentativas de salvar quantidades zeradas/negativas, datas futuras, motivos inativos ou arquivos de foto superiores a 5MB. |
| **Preservação Histórica (*Soft Delete*)** | Proibição de exclusão física permanente de dados no banco para evitar perda de rastro financeiro ou de auditoria. | Implementação do campo `status (Ativo/Inativo)` em cadastros de motivos, setores e usuários, garantindo 100% de consistência nos relatórios passados. |

---

### 3. Mapeamento de Regras de Negócio (RN)
* **RN (Autenticação e Rastreio Obrigatório):** O sistema captura automaticamente a sessão do usuário logado e o carimbo de data/hora do servidor. Nenhum registro de perda pode ser realizado de forma anônima.
* **RN (Segurança e Controle de Edições):** Qualquer edição ou cancelamento de lançamento de perda exige permissão de perfil elevado (Supervisor/Gerente) e o preenchimento de uma justificativa obrigatória, que fica salva permanentemente no log de auditoria.
* **RN (Investigação de Divergências):** O módulo de auditoria fornece a base de dados necessária para investigar divergências entre a contagem física e os registros, permitindo ao gerente filtrar ações por operador, setor ou período.

---

### 4. Arquitetura de Segurança e Níveis de Acesso (RBAC)
Como o sistema opera sem dependência de ERPs externos (RMS/Totvs), as barreiras de segurança e visibilidade de dados são geridas nativamente pela aplicação Python:

1. **Perfil Operador de Loja / Fiscal:**
   * Permissão para registrar novas perdas (com foto).
   * Visualização restrita apenas aos seus próprios lançamentos do dia.
   * Sem acesso a valores de custos acumulados ou relatórios consolidados da loja.

2. **Perfil Supervisor de Setor:**
   * Permissão para cadastrar, revisar e solicitar correções de lançamentos do seu setor.
   * Visualização de relatórios quantitativos do seu departamento.

3. **Perfil Gerente / Administrador:**
   * Acesso total aos Dashboards financeiros, relatórios comparativos e exportações (PDF/Excel).
   * Acesso exclusivo ao **Relatório de Auditoria** e gerenciamento de status de usuários e motivos.

