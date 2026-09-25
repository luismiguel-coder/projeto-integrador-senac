# CASOS DE USO E FLUXOS DE NAVEGAÇÃO

**Projeto:** Sistema de Gestão e Eficiência de Perdas - GEP  
**Grupo:** Grupo 2 — Front-End (Telas & Usabilidade)  
**Tarefa:** Elaboração dos Casos de Uso e Fluxos de Navegação  
**Responsável:** João Pedro de Menezes Almeida  
**Função:** Vice-Líder do Front-End  

## UC01 — Autenticar usuário

**Ator:** Todos os Usuários  
**Tela:** Autenticação

**Objetivo:** Permitir o acesso ao sistema de acordo com o perfil de usuário.

### Fluxo

1. O usuário acessa a tela de Login.
2. Informa usuário.
3. Informa senha.
4. Clica em **Entrar**.
5. O sistema valida os dados.
6. O usuário é direcionado ao Dashboard correspondente ao seu perfil.

---

## UC02 — Registrar ocorrência de perda

**Ator:** Operador / Administrador  
**Tela:** Registrar Perda

**Objetivo:** Registrar uma ocorrência de perda no sistema.

### Dados da ocorrência

- Código
- Nome
- Quantidade
- Motivo
- Setor
- Responsável
- Valor
- Evidência fotográfica

### Fluxo

**Dashboard → Registrar Perda → preencher informações → registrar**

### Contagem de cliques

- **Clique 1:** Registrar Perda
- **Clique 2:** Registrar/Salvar perda

**Total:** 2 cliques principais.

O sistema deve validar os campos obrigatórios e a evidência antes de concluir o registro.

---

## UC03 — Analisar ocorrência de perda

**Ator:** Analista  
**Tela:** Analisar Perdas

**Objetivo:** Avaliar uma ocorrência registrada e verificar se as informações estão corretas.

### Fluxo

1. O usuário acessa o Dashboard.
2. O sistema apresenta as ocorrências pendentes.
3. O usuário acessa **Analisar Perdas**.
4. Seleciona a ocorrência desejada.
5. O sistema apresenta os detalhes da ocorrência:
   - Produto
   - Quantidade
   - Motivo
   - Setor
   - Responsável
   - Valor
   - Data/hora
   - Evidência fotográfica
   - Observações
6. O analista registra sua análise.
7. O analista envia a ocorrência para aprovação.

### Contagem de cliques

- **Clique 1:** Analisar Perdas
- **Clique 2:** Selecionar ocorrência
- **Clique 3:** Enviar para Aprovação

**Total:** 3 cliques principais.

---

## UC04 — Aprovar ou Rejeitar ocorrência

**Ator:** Administrador  
**Tela:** Aprovar / Rejeitar

**Objetivo:** Tomar a decisão final sobre uma ocorrência de perda.

### Fluxo

**Dashboard → Aprovar/Rejeitar → selecionar ocorrência → Aprovar / Rejeitar / Solicitar correção**

### Contagem de cliques

- **Clique 1:** Aprovar/Rejeitar
- **Clique 2:** Selecionar ocorrência
- **Clique 3:** Aprovar / Rejeitar / Solicitar correção

**Total:** 3 cliques.

### Possíveis decisões

**Aprovar**
- A ocorrência é aprovada.
- O sistema registra a decisão.

**Rejeitar**
- A ocorrência é rejeitada.
- O administrador informa a justificativa da decisão.

**Solicitar correção**
- A ocorrência retorna para correção.
- O administrador informa o motivo da correção.

---

## UC05 — Consultar histórico de perdas

**Ator:** Todos os Usuários, conforme a permissão  
**Tela:** Histórico

**Objetivo:** Consultar ocorrências já registradas.

### Fluxo

**Dashboard → Histórico → Aplicar Filtros → Consultar Registros**

### Filtros

- Período
- Produto
- Setor
- Motivo
- Responsável
- Status

O usuário aplica os filtros e visualiza os registros.

O histórico deve utilizar paginação para facilitar a consulta de grandes quantidades de dados.

### Contagem de cliques

- **Clique 1:** Histórico
- **Clique 2:** Aplicar Filtros
- **Clique 3:** Consultar Registros

**Total:** 3 cliques.

---

## UC06 — Gerar relatórios

**Ator:** Administrador / Analista  
**Tela:** Relatórios

**Objetivo:** Gerar relatórios em Excel ou PDF para análise das perdas.

### Fluxo

**Dashboard → Relatórios → Selecionar relatório/filtros → Gerar Relatório → Exportar PDF/Excel**

### Exemplos

- Relatório de perdas por período
- Perdas por setor
- Perdas por motivo
- Produtos vencidos
- Relatório de auditoria

### Contagem de cliques

- **Clique 1:** Relatórios
- **Clique 2:** Gerar Relatório
- **Clique 3:** Exportar PDF/Excel

**Total:** 3 cliques.

---

## UC07 — Receber alertas de risco

**Ator:** Todos os Usuários  
**Disponibilidade:** Todas as telas do sistema

**Objetivo:** Permitir que o usuário visualize alertas relacionados a riscos e ocorrências relevantes.

### Alertas previstos

- Produtos próximos do vencimento
- Risco financeiro
- Baixa rotatividade
- Excesso de estoque
- Queda anormal nas vendas
- Saídas excessivas

### Fluxo

**Sino de notificações → visualizar alerta**

### Contagem de cliques

- **Clique 1:** Sino de notificações

**Total:** 1 clique principal.

> Os alertas são apresentados pelo ícone de notificações, não como uma página própria na navegação principal.

---

## UC08 — Acessar Menu do Usuário

**Ator:** Todos os Usuários  
**Disponibilidade:** Todas as telas do sistema

**Objetivo:** Permitir acesso rápido às opções relacionadas ao usuário.

### Fluxo

1. O usuário está em qualquer tela do sistema.
2. Clica na área com seu nome e perfil, localizada no canto superior direito.
3. O sistema abre o menu do usuário.
4. O sistema apresenta as opções disponíveis de acordo com o perfil.

### Opções por perfil

**Administrador**
- Gerenciar Usuários
- Configurações
- Sair

**Analista**
- Configurações
- Sair

**Operador**
- Configurações
- Sair

### Contagem de cliques

**Total:** 2 cliques para acessar uma opção do menu.

---

## UC09 — Gerenciar Usuários

**Ator:** Administrador  
**Tela:** Gerenciar Usuários

**Objetivo:** Permitir ao Administrador visualizar e administrar os usuários e seus perfis de acesso ao sistema.

### Fluxo

**Perfil → Gerenciar Usuários**

1. O Administrador acessa qualquer tela do sistema.
2. Clica na área do próprio perfil.
3. Clica em **Gerenciar Usuários**.
4. O sistema exibe a tela de gerenciamento.
5. O Administrador pode pesquisar, visualizar e selecionar um usuário.
6. O Administrador pode acessar as ações disponíveis para o usuário.

### Ações de gerenciamento

- Editar usuário
- Alterar perfil
- Redefinir senha
- Desativar usuário

### Perfis disponíveis

- Administrador
- Analista
- Operador

### Contagem de cliques

- **Clique 1:** Abrir Menu do Usuário
- **Clique 2:** Gerenciar Usuários

**Total:** 2 cliques.

### Acesso ao cadastro

A tela **Gerenciar Usuários** possui o botão **+ Cadastrar Usuário**, que direciona o Administrador para a tela de cadastro de um novo usuário.

---

## UC10 — Cadastrar Usuário

**Ator:** Administrador  
**Tela:** Cadastrar Usuário

**Objetivo:** Permitir ao Administrador cadastrar um novo usuário no sistema.

### Fluxo

**Menu do Usuário → Gerenciar Usuários → Cadastrar Usuário**

1. O Administrador abre o Menu do Usuário.
2. Acessa **Gerenciar Usuários**.
3. Clica em **+ Cadastrar Usuário**.
4. O sistema abre a tela **Cadastrar Usuário**.
5. O Administrador preenche os dados do novo usuário.
6. Seleciona o perfil de acesso.
7. Clica em **Cadastrar Usuário**.
8. O sistema valida os dados e conclui o cadastro.

### Dados do cadastro

- Nome
- E-mail
- Senha
- Confirmar senha
- Perfil

### Perfis disponíveis

- Administrador
- Analista
- Operador

### Navegação principal

**Gerenciar Usuários → + Cadastrar Usuário**

A tela de gerenciamento funciona como ponto central para consultar usuários existentes e acessar o cadastro de novos usuários.

---

## UC12 — Sair

**Ator:** Todos os Usuários  
**Disponibilidade:** Todas as telas do sistema

**Objetivo:** Encerrar a sessão do usuário e retornar à tela de login.

### Fluxo

**Menu do Usuário → Sair → Confirmar**

1. O usuário acessa o Menu do Usuário.
2. Seleciona a opção **Sair**.
3. O sistema exibe um pop-up de confirmação.
4. O pop-up apresenta a mensagem:

> **“Você realmente deseja encerrar a sessão?”**

5. O sistema apresenta as opções:
   - **Cancelar**
   - **Sair**
6. Caso o usuário selecione **Sair**, o sistema encerra a sessão atual.
7. O sistema direciona o usuário para a Tela de Login.

### Fluxo alternativo — Cancelar

1. O usuário seleciona **Cancelar**.
2. O pop-up é fechado.
3. O usuário permanece na tela em que estava.

### Contagem de cliques

- **Clique 1:** Abrir Menu do Usuário
- **Clique 2:** Sair
- **Clique 3:** Confirmar Sair

**Total:** 3 cliques.

---

# Fluxo geral do sistema

```text
LOGIN
  ↓
DASHBOARD
  ├── Registrar Perda
  │     ↓
  │   Validação
  │     ↓
  │   Analisar Perdas
  │     ↓
  │   Aprovar / Rejeitar
  │     ├── Aprovar
  │     ├── Rejeitar
  │     └── Solicitar Correção
  │
  ├── Histórico
  │
  ├── Relatórios
  │
  └── Menu do Usuário
        ├── Administrador
        │     ├── Gerenciar Usuários
        │     │      └── Cadastrar Usuário
        │     ├── Configurações
        │     └── Sair
        │
        ├── Analista
        │     ├── Configurações
        │     └── Sair
        │
        └── Operador
              ├── Configurações
              └── Sair
```
