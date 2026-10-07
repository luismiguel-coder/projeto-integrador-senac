## 1. O que é Controle de Acesso?

Controle de acesso é a forma de decidir quem pode entrar em cada parte do sistema e qual pessoa pode fazer lá dentro.
O controle de acesso serve para impedir que uma pessoa veja ou faça algo que não deveria.

## 2. Perfis de Usuário

Cada pessoa que usa o sistema terá um perfil. O perfil define as permissões dela.

| Perfil | O que pode fazer | O que não pode fazer |
|---|---|---|
| Operador / Repositor | Registrar perdas, preencher quantidade, preço, motivo, destinação e anexar foto | Ver relatórios financeiros, valores acumulados, dashboards e dados de outros usuários |
| Analista / Validador | Conferir, revisar, validar e assinar os registros de perda | Aprovar definitivamente perdas ou acessar relatórios financeiros completos |
| Gerente | Aprovar ou rejeitar perdas, acessar dashboards financeiros | Editar ou apagar logs de auditoria |

## 3. Regras de Controle de Acesso

### 3.1 Operador / Repositor

O Operador e o Repositor são responsáveis por coletar as informações da perda no momento em que ela acontece.

Eles podem:

- Criar um novo registro de perda.
- Informar o produto, quantidade e preço.
- Selecionar o motivo da perda.
- Escolher a destino do produto.
- Tirar e anexar a foto obrigatória, exceto quando o motivo for Furto Constatado.
- Visualizar apenas os próprios registros criados no dia.
- Consultar o Guia de Descarte gerado pela IA.

Eles **não podem**:

- Ver valores financeiros acumulados.
- Ver relatórios consolidados da loja.
- Ver relatórios de outros operadores.
- Aprovar ou rejeitar perdas.
- Acessar dashboards gerenciais.
- Exportar dados em PDF ou Excel.
- Alterar registros já validados.

### 3.2 Analista 

O Analista é a pessoa que confere se a perda foi registrada corretamente.

Ele pode:

- Visualizar registros criados pelos Operadores.
- Conferir as informações preenchidas.
- Solicitar correção, quando necessário.
- Enviar o registro para análise gerencial.
- Visualizar relatórios quantitativos do seu setor.

Ele **não pode**:

- Aprovar definitivamente uma perda.
- Acessar relatórios financeiros completos.
- Ver valores de custo acumulado da loja.
- Alterar registros já aprovados.
- Excluir registros do sistema.

### 3.3 Gerente

O Gerente é responsável por aprova as perdas e acompanhar o impacto financeiro.

Ele pode:

- Aprovar ou rejeitar registros com status EM_ANALISE.
- Acessar o painel de aprovação final.
- Visualizar todos os dashboards financeiros.
- Ver relatórios comparativos mensais.
- Exportar relatórios em PDF ou Excel.
- Visualizar o Relatório de Auditoria.
- Gerenciar status de usuários e motivos de perda.
- Ter acesso total à área financeira.

Ele **não pode**:

- Editar ou apagar logs de auditoria.
- Alterar registros já finalizados sem deixar rastro de auditoria.
- Conceder permissões financeiras para perfis sem autorização.

## 4. Política de Autenticação

Política de autenticação é o conjunto de regras que define como o sistema vai confirmar que a pessoa é realmente quem ela diz ser antes de deixar entrar isso é antes de usar o sistema, cada usuário precisa provar sua identidade.

### 4.1 Quem precisa se autenticar

Todos os usuários do sistema devem passar pela autenticação:

- Operador
- Repositor
- Analista / Validador
- Gerente


Nenhum usuário pode acessar o sistema sem se identificar.

### 4.2 Forma de autenticação

O sistema deve usar usuário e senha como forma principal de autenticação.

Para acessar o sistema, o usuário deverá informar:

- Login.
- Senha pessoal.

Após o login, o sistema identifica o perfil do usuário e mostra apenas as telas e funções permitidas para ele.

### 4.3 Senha segura

Cada usuário deve criar uma senha segura, seguindo estas regras:

- Ter no mínimo 14 caracteres.
- Conter letras maiúsculas, minúsculas, nomeros e caractere especial, como `!`, `@`, `#` ou `*`.
- Não usar nome, data de nascimento, telefone ou sequências fáceis, como `123456`.
- Não compartilhar a senha com outra pessoa.
- Trocar a senha a cada 6 meses.

### 4.4 Bloqueio de conta

Para evitar tentativas de invasão, o sistema deve bloquear temporariamente a conta após várias tentativas erradas.

- Após **3 tentativas incorretas**, a conta fica bloqueada.
- Após o bloqueio, o usuário deve criar uma nova senha para entra na conta.
- Cada tentativa de acesso incorreta deve ser registrada no log de auditoria.

### 4.5 Sessão do usuário

Depois de entrar no sistema, o usuário fica em uma sessão.

O sistema deve:

- Encerrar a sessão automaticamente após **15 segundos sem uso**.
- Encerrar a sessão quando o usuário clicar em “Sair”.
- Impedir que duas pessoas usem a mesma conta ao mesmo tempo, quando possível.

### 4.6 Autenticação para ações importantes

Algumas ações são mais sensíveis e exigem confirmação extra.

- O Validador deve inserir a senha para salvar e assinar registro da perda.
- O Gerente deve estar autorizado para aprovar ou rejeitar uma perda.
Isso ajuda a garantir que cada ação importante possa ser rastreada até a pessoa responsável.

## 5. Relação entre Autenticação e Controle de Acesso

Autenticação e controle de acesso trabalham juntos.

1. Primeiro, o sistema pergunta: “Quem é você?”
   Isso é a autenticação.

2. Depois, o sistema pergunta: “O que você pode fazer?”  
   Isso é o controle de acesso.

### Exemplo prático

O Operador João entra com login e senha.

O sistema confirma que João é realmente o Operador João.

Depois, o sistema verifica o perfil dele e permite apenas:

- Registrar perdas.
- Ver seus próprios lançamentos.
- Anexar fotos.

João não consegue acessar relatórios financeiros, pois seu perfil não tem essa permissão.

## 6. Regras de Visibilidade por Perfil

| Informação | Operador / Repositor | Analista / Validador | Gerente |
|---|---:|---:|---:|
| Registrar perda | Sim | Não | Não |
| Ver próprios registros | Sim | Sim | Sim |
| Aprovar ou rejeitar perda | Não | Não | Sim |
| Ver valores financeiros acumulados | Não | Não | Sim |
| Ver dashboards financeiros | Não | Não | Sim |
| Exportar relatórios | Não | Não | Sim |
| Ver relatório de auditoria | Não | Não | Sim |
| Gerenciar usuários e permissões | Não | Não | Sim |
| Editar ou apagar logs | Não | Não | Não |

## 7. Registro de Tentativas Não Autorizadas

Sempre que alguém tentar acessar uma área sem permissão, o sistema deve gravar um log de segurança.

- Um Repositor tenta abrir um relatório financeiro.
- O sistema bloqueia o acesso.
- O sistema registra: quem tentou acessar, qual tela foi acessada, horário e endereço IP do equipamento.
Isso ajuda a identificar tentativas de fraude, erro de configuração ou uso indevido do sistema.

