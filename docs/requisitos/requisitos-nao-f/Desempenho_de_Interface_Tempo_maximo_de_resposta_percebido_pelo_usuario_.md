**Nome: Luiz Carlos**

**O que estou entregando**

**Funcionalidade de Backup Automático dos Dados do Sistema de Gestão de
Perdas**, garantindo a segurança das informações registradas sobre
perdas, desperdícios, avarias e vencimentos de produtos.

**Como isso funciona na prática**

O sistema realiza um **backup automático diariamente às 03h00 da
manhã**. Todas as informações cadastradas durante o dia são copiadas e
armazenadas em um local seguro.

Exemplo:

- Se durante o dia forem registrados **500 lançamentos de perdas**,
  todos esses dados serão salvos automaticamente no backup noturno.

- Em caso de falha no sistema, os dados podem ser restaurados a partir
  da última cópia de segurança realizada.

**Regra de Negócio**

**Regra 8 – Segurança e Integridade dos Dados**

Todos os registros de perdas devem ser preservados e protegidos por meio
de backups automáticos, garantindo que nenhuma informação crítica seja
perdida em casos de falhas, erros ou indisponibilidade do sistema.

**Desempenho de Interface (Tempo máximo de resposta percebido pelo
usuário)**

- Consulta de registros: até **2 segundos**.

- Cadastro de perdas: até **3 segundos**.

- Geração de relatórios: até **5 segundos**.

- O processo de backup ocorre em segundo plano, sem impactar a
  utilização do sistema pelos usuários.

**Resultado esperado:** o usuário consegue registrar e consultar
informações de perdas rapidamente, enquanto os dados permanecem
protegidos por backups automáticos diários.
