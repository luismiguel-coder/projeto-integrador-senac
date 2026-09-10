# 

# Luis Miguel 

# **Atribuições:**

# Levantar casos de uso principais e Definir fluxos de aprovação

# Casos de Uso Principais (Levantamento)

**UC01 – Autenticar usuário**

Permitir que usuários cadastrados acessem o sistema conforme seu nível
de permissão.

Ator: Administrador, Supervisor, Analista, Colaborador.

**UC02 – Registrar ocorrência de perda**

Permitir o registro de perdas informando:

produto;

quantidade perdida;

categoria;

motivo da perda;

setor/local;

data;

evidências (quando necessário).

Ator: Colaborador, Analista de Prevenção.

---

**UC03 – Analisar ocorrência de perda**

Permitir que responsáveis avaliem os registros realizados, verificando
informações e classificando a ocorrência.

Ator: Analista de Prevenção, Supervisor.

---

UC04 – Aprovar ou rejeitar ocorrência

Permitir que o responsável aprove, solicite ajustes ou rejeite uma
ocorrência registrada.

Ator: Supervisor/Gerente.

---

UC05 – Consultar histórico de perdas

Permitir a consulta das ocorrências registradas utilizando filtros como:

período;

produto;

categoria;

setor;

motivo.

Ator: Todos os usuários autorizados.

**UC06 – Visualizar indicadores de perdas**

Apresentar informações gerenciais através de gráficos e métricas, como:

quantidade de perdas;

produtos com maior índice de perda;

principais motivos;

setores com maior ocorrência.

Ator: Supervisor/Gerente, Analista.

**UC07 – Gerar relatórios**

Permitir a geração de relatórios para acompanhamento e tomada de
decisão.

Ator: Supervisor/Gerente, Analista.

---

**UC08 – Receber alertas de risco**

Permitir que o sistema identifique padrões de perda e gere alertas
preventivos.

Ator: IA/Sistema.

---

**UC09 – Gerenciar usuários e permissões**

Permitir cadastro, edição e controle dos níveis de acesso dos usuários.

Ator: Administrador.

---

# Fluxo de Aprovação de Perdas

**1. Registro da ocorrência**

Colaborador identifica uma perda e registra no sistema.

**2. Validação dos dados**

O sistema verifica se as informações obrigatórias foram preenchidas:

produto;

quantidade;

motivo;

data;

evidências (quando necessário).

**3. Análise da ocorrência**

O analista ou responsável pela prevenção avalia o registro e verifica
possíveis inconsistências.

**4. Aprovação**

O supervisor decide:

Aprovar: ocorrência confirmada e registrada nos indicadores.

l

Solicitar correção: devolve para ajuste das informações.

Rejeitar: ocorrência não reconhecida.

**5. Atualização dos indicadores**

Após aprovação:

a perda é contabilizada;

os dashboards são atualizados;

relatórios passam a considerar a ocorrência.

---

Atores do Sistema

Administrador: gerencia usuários e permissões.

Supervisor/Gerente: acompanha indicadores e aprova ocorrências.

Analista de Prevenção de Perdas: analisa registros e acompanha riscos.

Colaborador: registra ocorrências.

Sistema/IA: auxilia na identificação de padrões e alertas.
