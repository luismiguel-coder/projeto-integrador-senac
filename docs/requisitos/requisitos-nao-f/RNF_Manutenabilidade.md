**ENTREGA: RNF – MANUTENIBILIDADE**

- **Projeto:** Sistema de Gestão de Perdas – Supermercado

# 📑 DOCUMENTAÇÃO TÉCNICA DO SISTEMA

## 1. Mapeamento de Processo e Fluxo de Dados

O processo de registro de perda é dividido em três fases críticas: **Coleta, Validação em Campo e Homologação Gerencial**. O fluxo abaixo garante a conformidade com as regras de visibilidade e duplo fator.

[Operador/Repositor]
│
▼
1. Coleta física do produto
2. Preenche Volumetria e Preço Manual
3. Seleciona Motivo Padronizado e Destinação
4. Tira Foto Obrigatória (RN09) *Exceto Furto Constatado
5. IA exibe Guia de Descarte na tela
│
▼
[Validador em Campo] ──> Insere senha para salvar o rascunho (RN02)
│
▼
[Gerente / Analista] ──> Painel de Aprovação Final (Aprova/Rejeita)
│
▼
[Banco de Dados] ───> Processamento dos Relatórios (RN11: Cenário A ou B)
### 1.1. Estados da Ocorrência de Perda
Para garantir que a perda só entre oficialmente no sistema após o crivo da gestão, cada registro passará pelos seguintes status:

* **EM_ANALISE:** Criado pelo Operador e assinado pelo Validador. Aguarda ação gerencial. Não computa nos relatórios mensais.
* **APROVADO:** Homologado pelo Gerente/Analista. O valor é contabilizado no prejuízo e o estoque é baixado.
* **REJEITADO:** Descartado pelo Gerente/Analista (ex: erro de digitação). O log é guardado, mas o registro é invalidado.

---

## 2. Guia de Suporte e Resolução de Problemas (Troubleshooting)

Este guia serve para a equipe de TI local e suporte de Nível 1 resolverem incidentes comuns na operação física.

### 2.1. Problemas Frequentes e Ações de Suporte

* **Incidente: IA não exibe o Guia de Descarte**
  * **Causa Provável:** Perda de conexão com o serviço de IA local ou falha no processador do terminal.
  * **Procedimento de Suporte:** Verificar o status do contêiner/serviço `ia-descarte-service`. O sistema deve possuir um *fallback* (plano B) textual pré-cadastrado no banco de dados local para não travar a tela do operador caso a IA fique fora do ar.
* **Incidente: Erro "Câmera não detectada" ao tentar anexar evidência**
  * **Causa Provável:** Falha de hardware no coletor de dados/tablet ou permissão de aplicativo negada.
  * **Procedimento de Suporte:** Se o motivo selecionado for `FURTO_CONSTATADO`, o sistema deve ignorar o bloqueio da foto. Para os demais motivos, o suporte deve resetar as permissões de mídia do dispositivo ou liberar o upload de arquivo local como contingência.
* **Incidente: Colunas de comparação sumiram do painel gerencial**
  * **Causa Provável:** Comportamento normal da RN11 (Cenário B).
  * **Procedimento de Suporte:** Validar no banco de dados se existem perdas com o status `APROVADO` no mês anterior. Se for o primeiro mês de uso do sistema, instruir o gerente que os gráficos comparativos só aparecerão a partir do dia 1º do próximo mês.

---

## 3. Arquitetura de Gerenciamento de Logs (A "Caixa-Preta" das Perdas)

Os logs deste sistema são imutáveis e estruturados para auditoria forense de estoque e prevenção de fraudes internas.

### 3.1. Estrutura do Log de Auditoria (Payload JSON)
Toda criação, validação ou aprovação de perda deve gerar um log no seguinte formato:

```json
{
  "timestamp": "2026-10-01T15:58:32.123Z",
  "level": "INFO",
  "facility": "AUDIT_LOSS_SYSTEM",
  "event": "LOSS_REGISTRATION_SUBMITTED",
  "terminal_id": "PDV_COLETA_04",
  "users": {
    "operator_id": "USR_9942",
    "validator_id": "USR_1105",
    "approver_id": null
  },
  "data": {
    "product_sku": "7891000123456",
    "quantity": 4.35,
    "unit": "KG",
    "declared_value": 87.00,
    "reason": "QUEBRA_CADEIA_FRIO",
    "status_assigned": "EM_ANALISE"
  }
}
```

### 3.2. Rastreabilidade de Eventos Críticos (Matriz de Logs)

| Nível de Log | Evento / Ação Sistêmica | Gatilho de Negócio | Dados Obrigatórios no Log |
| :--- | :--- | :--- | :--- |
| **INFO** | `LOSS_PENDING_APPROVAL` | Validador assinou e enviou para a fila do gerente (RN02). | IDs do Operador e Validador, SKU, Qtd, Valor Declarado. |
| **INFO** | `LOSS_APPROVED_FINALIZE` | Gerente/Analista aprovou a perda inserindo-a no balanço final. | ID do Aprovador, ID da Ocorrência, Impacto Financeiro. |
| **WARN** | `UNAUTHORIZED_ACCESS_ATTEMPT` | Usuário com perfil Repositor tentou acessar relatórios monetários (RN01). | ID do Repositor, IP da máquina, URL tentada. |
| **WARN** | `BYPASS_PHOTO_FURTO` | Registro de perda finalizado sem foto por motivo de furto (RN07). | ID do Operador, Justificativa automática do sistema. |
| **ERROR** | `IA_INFERENCE_FAILURE` | Falha ao carregar as instruções da IA local (RN10). | Código do Erro, SKU do produto, tempo de timeout. |
| **FATAL** | `LOSS_INTEGRATION_TIMEOUT` | Ocorrências aprovadas travadas localmente sem conseguir sincronizar com o ERP central. | Volume de registros retidos na fila local, erro do banco de dados. |

---

## 4. Requisitos Não Funcionais (RNF)

### 4.1. Segurança e Privacidade
* **RNF-SEC-01 (Mascaramento de Dados):** O sistema deve aplicar mascaramento ou omitir por completo elementos de interface (DOM elements) que contenham dados monetários quando o token de autenticação pertencer ao perfil Repositor/Operador (RN01).
* **RNF-SEC-02 (Imutabilidade dos Logs):** Os logs de auditoria de perdas devem ser gravados em um banco de dados do tipo *Append-Only* ou direcionados em tempo real para um servidor de logs centralizado (ex: OpenSearch/Splunk). Nem mesmo o perfil de Gerente ou Administrador de TI pode ter permissão para deletar ou editar registros da tabela de logs.

### 4.2. Desempenho e Eficiência
* **RNF-PERF-01 (IA Local Edge):** O modelo de Inteligência Artificial para o Guia de Descarte (RN10) deve rodar localmente no servidor da loja (Edge Computing) para garantir que o tempo de resposta da instrução na tela não ultrapasse 1.5 segundos após a seleção do produto, operando sem dependência da internet externa.
* **RNF-PERF-02 (Processamento Analítico):** A consulta dinâmica de comparação mensal (RN11) deve ser calculada por meio de views indexadas ou tabelas agregadas atualizadas na madrugada, garantindo que o carregamento do dashboard gerencial aconteça em menos de 3 segundos.

### 4.3. Confiabilidade e Disponibilidade
* **RNF-REL-01 (Armazenamento de Evidências):** As fotos anexadas (RN09) devem passar por um processo automático de compressão no dispositivo de coleta antes do envio, limitando cada imagem a no máximo 500 KB no formato WebP, evitando o esgotamento rápido do armazenamento local da loja.
* **RNF-REL-02 (Resiliência do Fluxo de Aprovação):** Caso a conexão entre o caixa/coletor e o servidor caia após a assinatura do Validador (RN02), o rascunho com o status EM_ANALISE e a foto acoplada devem ficar guardados em um banco de dados local (SQLite/IndexedDB) e transmitidos de forma assíncrona assim que a rede restabelecer, impedindo a perda da auditoria física da quebra.
