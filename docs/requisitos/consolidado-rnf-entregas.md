# 📋 CONSOLIDADO DAS ENTREGAS ORIGINAIS DE RNFs 

Este documento reúne todas as especificações de Requisitos Não Funcionais (RNF) do Projeto Salvus exatamente como foram entregues pelos seus respectivos titulares, cada seção está devidamente identificada com o nome do integrante responsável.

---

## 🔒 1. SEGURANÇA DOCUMENTAL
* **Responsável pela Entrega:** Luis Miguel
* **Documento de Origem:** `RNF Segurança Documental.docx`
* **Data de Emissão:** 11/08/2026

### INTRODUÇÃO E OBJETIVO
Este documento estabelece as diretrizes de Segurança Documental e Rastreabilidade. O objetivo é garantir que o sistema opere em conformidade com a LGPD e mantenha um histórico imutável de todas as ações, eliminando a falha atual de cadastros incompletos e protegendo a empresa contra fraudes.

### DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)
| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Auditoria e Rastreabilidade** | Registro automático de qualquer transação (C.R.U.D) realizada no banco de dados. | Gravação imutável de: ID do usuário, IP, Data e Hora exata (milisegundos) de cada alteração. |
| **Conformidade LGPD** | Proteção de dados sensíveis e controle de acesso baseado em funções (RBAC). | Criptografia (AES-256) em repouso para dados de identificação; Acesso restrito a Gerentes e Administradores. |
| **Integridade de Registro** | Bloqueio de entradas de dados que corrompam a lógica do negócio. | Impedir salvamento de vencimentos retroativos ou quantidades negativas em 100% das tentativas. |

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-03 (Dados Obrigatórios):** O sistema captura automaticamente o carimbo de tempo e o autor da ação, garantindo que nenhum registro de perda seja "anônimo".
* **RN-09 (Segurança):** Criação de um histórico imutável onde ajustes de estoque só podem ser feitos mediante justificativa e registro de log.
* **RN-10 (Investigação):** Fornece a base de dados para investigar imediatamente qualquer divergência física superior a 5% detectada entre o sistema e o balanço.

### INTEGRAÇÃO E SEGURANÇA
* **Sistemas Externos:** Os logs de auditoria são estruturados para permitir cruzamento com os relatórios de saída dos ERPs RMS/ Totvs.
* **Privacidade:** O sistema implementa uma barreira onde o Estoquista visualiza apenas o estoque, enquanto o Gerente visualiza o custo financeiro total das perdas.

---

## 🛠️ 2. MANUTENIBILIDADE & PROCESSO DE SUPORTE
* **Responsável pela Entrega:** Alaíde
* **Documento de Origem:** `RNF_DONA_ALAIDE.docx`

### INTRODUÇÃO E OBJETIVO
* **Pergunta:** Pensando no dono do mercado, por que é importante ter um manual que ensine a usar o sistema e um plano para quando algo der erro? Como isso ajuda a não perder dinheiro?
* **Resposta da Alaíde:** *Ter um manual que ensine todos a usarem o sistema corretamente evitando erros por desconhecimento, já o plano garante que se algo falhar o trabalho não pare e as operações continue, assim não há interrupção no controle do estoque e de perdas evitando prejuízo e mantendo controle eficiente para proteger o lucro do marcado.*

### DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)
* **Processo e Suporte:**
  * *Pergunta:* Se o "bipado" de produtos estragar ou a internet cair, o que o sistema deve deixar o funcionário fazer para o trabalho não parar?
  * *Resposta da Alaíde:* **O funcionário cadastre e registre os produtos e perdas de forma manual informando o motivo da digitação manual com justificativa obrigatória, toda vez que alguém registrar uma perda, o sistema deve gravar quem fez, qual o produto foi, quantidade motivo da perda além de data, hora e IP de forma que não possa ser alterado depois**
  * *Métrica:* Opção de cadastro manual com justificativa obrigatória.
* **Monitoramento Logs:**
  * *Pergunta:* Para o dono do mercado ter certeza de que ninguém está mentindo sobre os produtos, que informações o sistema deve gravar toda vez que alguém registrar uma perda?
  * *Resposta da Alaíde:* **Registro imutável ID do usuário, Data, Hora e IP.**
  * *Métrica:* Registro imutável de: ID do usuário, Data, Hora e IP.
* **Documentação Técnica:**
  * *Pergunta:* Como o manual deve ser feito para que, daqui a um ano, outro técnico consiga consertar o sistema rápido?
  * *Resposta da Alaíde:* **O manual deve ser claro organizado e completo, com explicações simples passo a passo, diagramas e informações sobre como o sistema funciona, onde ficam os arquivos e como é o banco de dados.**
  * *Métrica:* Documentação organizada detalhando a estrutura do banco de dados.

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-09 (Segurança e Confiabilidade):** O registro de quem fez a operação (Logs) garante que as informações não sejam apagadas para esconder erros.
* **RN-10 (Investigação de Divergências):** Se houver uma diferença maior que 5% no estoque, os registros ajudam o gerente a descobrir quem foi o último a mexer no produto.

### INTEGRAÇÃO E SEGURANÇA
* *Pergunta:* Quem você acha que deve ter o poder de ver esses relatórios de erros e quem mexeu no estoque? (O Gerente ou qualquer funcionário?)
* *Resposta da Alaíde:* **Apenas o gerente e o dono de mercado** (O acesso deve ser restrito conforme o perfil, protegendo dados sensíveis de custos).

---

## ⏱️ 3. DISPONIBILIDADE & REGRAS DE SLA
* **Responsável pela Entrega:** Kamila
* **Documento de Origem:** `Disponibilidade_Regras_de_SLA_e_Horario_de_Funcionamento_1.docx`
* **Data de Emissão:** 23/08/2026

### INTRODUÇÃO E OBJETIVO
Este documento define os requisitos de disponibilidade, horário de funcionamento e regras de SLA do Sistema de Gestão de Perdas. O objetivo é garantir que o sistema permaneça disponível durante o período de operação do supermercado, reduzindo impactos nas atividades e evitando perdas causadas por indisponibilidade.

### DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)
* **Disponibilidade do Sistema:** O sistema deverá permanecer disponível continuamente, permitindo o registro e acompanhamento das perdas.
  * *Métrica:* Disponibilidade de 24 horas por dia, 7 dias por semana.
* **Disponibilidade no Horário do Cliente:** O sistema deverá garantir prioridade de funcionamento durante todo o horário de operação do supermercado.
  * *Métrica:* 100% de disponibilidade durante o horário de funcionamento do cliente, exceto em situações emergenciais.
* **Manutenção Programada:** Atualizações e manutenções que possam afetar o funcionamento ou desempenho deverão ser realizadas fora do horário de funcionamento do cliente.
  * *Métrica:* 100% das manutenções programadas realizadas fora do horário de funcionamento.
* **Manutenção Emergencial:** Em caso de falha grave ou situação que comprometa a estabilidade e segurança do sistema, a manutenção deverá ser iniciada imediatamente.
  * *Métrica:* Início da intervenção em até 15 minutos após a identificação de uma falha crítica.
* **Comunicação de Indisponibilidade:** Sempre que possível, o cliente deverá ser informado previamente sobre manutenções programadas e seus possíveis impactos.
  * *Métrica:* Comunicação realizada com no mínimo 24 horas de antecedência para manutenções programadas.
* **Continuidade do Serviço:** O sistema deverá priorizar a estabilidade e a continuidade da operação, principalmente durante o horário de funcionamento do supermercado.
  * *Métrica:* Interrupções não planejadas devem ser tratadas imediatamente após sua identificação.

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-05:** [Notificações via Dashboard, E-mail e WhatsApp para anomalias.] – Relaciona-se ao requisito de comunicação de indisponibilidades e intervenções, permitindo que informações importantes sobre anomalias e possíveis impactos sejam comunicadas aos responsáveis.

---

## 📱 4. USABILIDADE & COMPATIBILIDADE MULTIPLATAFORMA
* **Responsável pela Entrega:** Yuri
* **Documento de Origem:** `Requisitos_de_Usabilidade_Sistema_de_Gestao_de_Perdas_1.docx`
* **Data de Emissão:** 24/08/2026

### DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)
* **Interface intuitiva:** A interface deve permitir que o estoquista registre uma perda, entrada ou ajuste de estoque de forma simples, com campos obrigatórios claramente identificados e acesso rápido às funções principais. O operador deve conseguir registrar uma perda com no máximo 3 cliques a partir da tela inicial.
* **Acessibilidade:** A interface deve utilizar textos legíveis, contraste adequado, identificação clara dos campos, mensagens de erro compreensíveis e navegação que não dependa exclusivamente de cores. Todas telas principais devem possuir contraste adequado e todos os campos obrigatórios devem apresentar identificação textual e simbolica (um asterisco “*”).
* **Compatibilidade multiplataforma:** O sistema deve funcionar corretamente em computadores, tablets e celulares, mantendo as funções principais de estoque e consulta de informações, operando em Windows, Android e ios e navegadores modernos, sem perda de funcionalidade.

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **Classificação obrigatória como Entrada, Saída ou Ajuste:** A interface intuitiva deve apresentar de forma clara as opções de classificação, reduzindo erros no registro das movimentações.
* **Dados obrigatórios:** A acessibilidade e a organização dos campos devem facilitar a identificação e o preenchimento dos dados obrigatórios, como data, usuário, lote, validade e justificativa.
* **Controle de acesso rígido por perfil de usuário:** A interface deve apresentar somente as funcionalidades compatíveis com o perfil do usuário, facilitando a utilização e evitando acesso indevido.

### INTEGRAÇÃO E SEGURANÇA
* A usabilidade deve respeitar os diferentes perfis de acesso definidos para o sistema. Gerentes/Supervisores possuem acesso amplo, enquanto estoquistas realizam operações como registro de entradas, saídas e conferência de validade. A interface deve apresentar as funções de acordo com as permissões de cada perfil.
* Quanto às integrações, o sistema deve manter suas funções principais de estoque mesmo quando utilizado em diferentes dispositivos e navegadores, considerando a integração com o PDV e os sistemas corporativos previstos no levantamento de requisitos.

---

## ⚡ 5. DESEMPENHO DE INTERFACE (NOVA ENTREGA - SEM CORREÇÕES)
* **Responsável pela Entrega:** Luiz Carlos
* **Documento de Origem:** `desempenho_interface (1).md`
* **Data de Emissão:** 01/09/2026

### 1. INTRODUÇÃO E OBJETIVO
Objetivo deste documento é identificar e definir requisitos para garantir maior desempenho da interface do sistema.

### 2. DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)
* **RNF-01: Tempo de carregamento de página**
  * Quando o usuário clicar em um link, a página deverá ser aberta em até 3 segundos.
* **RNF-02: Tempo de resposta em formulários**
  * Quando o usuário salvar um cadastro ou edição, o sistema deverá responder em até 10 segundos e exibir um ícone de carregamento durante o processamento.
* **RNF-03: Tempo de carregamento de dados**
  * Relatórios e gráficos deverão ser carregados em até 15 segundos. Caso haja grande volume de dados, o sistema deverá exibir as informações gradualmente.
* **RNF-04: Feedback visual**
  * Sempre que o usuário realizar uma ação que demande processamento, o sistema deverá exibir uma mensagem ou ícone de carregamento em até 200 milissegundos.

### 3. MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-01: Dados Obrigatórios**
  * Formulários rápidos incentivam o funcionário a preencher todos os campos obrigatórios (data, hora, lote, validade e justificativa) sem pular etapas.
* **RN-02: Controle de Acesso**
  * Telas com carregamento rápido estimulam o uso do sistema pelos funcionários, contribuindo para a eficiência do controle de acesso.
* **RN-03: Notificações**
  * Dashboards com bom desempenho devem exibir notificações de anomalias (e-mail e WhatsApp) de forma imediata ao gerente.

---

## 🔑 6. SEGURANÇA TÉCNICA E RASTREABILIDADE
* **Responsável pela Entrega:** William
* **Documento de Origem:** `Segurança_Técnica_William_Ajustado.md`
* **Data de Emissão:** 25/08/2026

### 1. INTRODUÇÃO E OBJETIVO
Este documento estabelece os Requisitos Não Funcionais de Segurança Técnica e Rastreabilidade para o Sistema de Gestão de Perdas. Em total conformidade com a tríade de Segurança da Informação — Confidencialidade, Integridade e Disponibilidade (CID) —, as especificações aqui descritas visam garantir que apenas pessoas e processos autorizados executem ações no sistema, protegendo as informações financeiras de perdas e gerando um histórico de auditoria imutável contra fraudes e erros de lançamento.

### 2. CONTROLE DE ACESSO BASEADO EM FUNÇÕES (RBAC)
O sistema implementará restrições físicas e lógicas de visualização, custos e menus, divididos estritamente em quatro perfis oficiais de usuários e fontes de dados:
1. **Estoquista (Operador de Estoque):**
   * *Acesso Permitido:* Executa o registro diário de entradas (bipagem de produtos estragados/avarias - UC02) e alteração de saídas (atualização física do estoque).
   * *Restrição Absoluta:* **Bloqueio de 100% de visualização de custos financeiros** das perdas ou relatórios consolidados de rentabilidade corporativa. Não possui permissão para excluir registros de perdas ou aprovar descartes.
2. **Analista de Prevenção de Perdas:**
   * *Acesso Permitido:* Visualização de relatórios gerenciais, dashboards de risco, desempenho de gôndolas e análise financeira de custos de perdas (UC07 e UC08).
   * *Restrição Absoluta:* Perfil estritamente de leitura analítica. Bloqueado de registrar perdas manuais, alterar preços ou gerenciar permissões de usuários.
3. **Gerente / Supervisor (Controle de Qualidade):**
   * *Acesso Permitido:* Acesso total às funcionalidades operacionais e gerenciais. Responsável pela validação do fluxo, aprovação ou rejeição de descartes físicos de perdas (UC05), visualização de custos e auditoria.
4. **Administrador do Sistema:**
   * *Acesso Permitido:* Gerenciamento técnico de base de dados, manutenção de tabelas, configurações globais e gestão de usuários e permissões (UC10).

#### Resposta de Ajuste (William):
> *Pergunta: Como a interface do sistema (front-end) e as travas de dados do banco de dados (back-end) bloquearão fisicamente o Estoquista de visualizar os custos financeiros das perdas em todas as tabelas e relatórios? Detalhe teoricamente como o sistema garantirá essa segregação de telas.*
>
> *Resposta do William:* **No front-end, o sistema vai ler o perfil do usuário e, com base nesse perfil, o sistema não irá mostrar o restante dos menus, como Relatório Financeiro. Esconde ou desabilita colunas de valor ou custo que o usuário pode abrir, bloqueia URLs diretas. Se o usuário tentar procurar no navegador, o front-end vai checar a permissão e responder com acesso negado. Já o back-end se aplica ao princípio do mínimo privilégio, onde as permissões no banco de dados já são limitadas. O usuário só pode fazer SELECT apenas em views em tabelas que não incluam outros setores. Com as regras de negócio no back-end, o código também protege os usuários cadastrados, que retornam apenas relatórios necessários do perfil do usuário.**

### 3. POLÍTICA DE AUTENTICAÇÃO E SESSÃO SEGURA
* **Padrão de Credenciais:** Exigência de senha robusta com no mínimo 8 caracteres, contendo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial (símbolo).
* **Bloqueio por Tentativas:** Bloqueio temporário e automático da conta de usuário após 5 tentativas de login consecutivas inválidas. O desbloqueio ocorrerá automaticamente após o tempo de resiliência de 15 minutos, ou manualmente por um Administrador.
* **Sessão Segura e Timeout:** Expiração automática da sessão de login ativa por inatividade física do operador após 30 minutos. Dados sensíveis de autenticação não devem ser armazenados em cache local de navegadores.
* **Desempenho de Autenticação:** Tempo máximo de validação e carregamento das permissões do usuário limitado a 2 segundos em conexões de rede locais.

### 4. LOGS DE AUDITORIA E RASTREABILIDADE (REQUISITO CRÍTICO - RN-09)
* **Trilha de Auditoria C.R.U.D (Ações de Dados):** Toda inserção, alteração de saída ou exclusão de perda de estoque deve gravar um registro automático e imutável.
* **Identificação de Fontes Inteligentes:** Quando um alerta de risco ou sugestão de perda/desconto for disparado automaticamente pelo Agente de IA do sistema (UC09), o log de auditoria registrará o evento no histórico gravando o autor como `ID_USUARIO = "SISTEMA_IA"`.
* **Retenção e Consulta de Histórico:** Logs de auditoria serão protegidos fisicamente e retidos por no mínimo 12 meses. O tempo de resposta para consultas de logs pelo perfil Gerente deve ser inferior a 3 segundos.

#### Resposta de Ajuste (William):
> *Pergunta: Quais são os dados exatos que a tabela de Log de Auditoria gravará automaticamente a cada clique de alteração ou exclusão?*
>
> *Resposta do William:* **Dados gravados automaticamente no Log de Auditoria: A tabela log_auditoria vai registra, de forma unica e automática, a cada introdução, alteração ou exclusão de perda de estoque. Esses dados permitem reconstruir inteiramente a trilha de auditoria de C.R.U.D. que significa Criar, Ler, Atualizar e Deletar identificar ações autônomas com IA, e garantir que nenhuma alteração ou exclusão de perda seja feita de forma anônima**

---

## 🌐 7. INTEGRAÇÃO SISTÊMICA
* **Responsável pela Entrega:** Ed
* **Documento de Origem:** `Integracao_Sistemica.MD`
* **Data de Emissão:** 21/08/2026

### DETALHAMENTO DOS REQUISITOS
| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Mapeamento de APIs** | Documentação completa dos endpoints REST do sistema (métodos, parâmetros, respostas). Inclui especificação de cada rota, autenticação necessária, dados de entrada e saída, e exemplos de uso. | |
| **Conexão com RMS** | Integração com o sistema RMS para consulta e atualização de estoque. | Sincronização de dados em até 3 segundos; 99,5% de disponibilidade do serviço. |
| **Conexão com Totvs** | Integração com o Totvs para consulta de preços de custo e venda dos produtos. | Tempo de retorno da API abaixo de 1 segundo; tratamento de erro. |
| **Autenticação entre Sistemas** | Comunicação segura entre sistemas via tokens OAuth 2.0 e HTTPS/TLS 1.3. | Tokens expirando em 1 hora; renovação automática sem intervenção manual. |
| **Logs de Integração** | Registro de todas as chamadas de API entre sistemas com status e timestamp. | Logs retidos por 12 meses; consulta de histórico abaixo de 2 segundos. |

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-01 (Estoque Inteligente):** A conexão com RMS garante atualização automática de estoque quando uma perda é registrada, evitando estoque negativo.
* **RN-03 (Registro de Perdas):** O mapeamento de APIs permite que o PDV registre perdas diretamente, sem acesso separado ao sistema de gestão.
* **RN-05 (Relatórios Gerenciais):** A conexão com Totvs fornece dados de preço de custo para cálculo correto do impacto financeiro das perdas.
* **RN-09 (Auditoria):** Os logs de integração mantêm registro imutável de todas as movimentações entre sistemas para auditoria.

---

## 🏗️ 8. INFRAESTRUTURA
* **Responsável pela Entrega:** Luis Miguel
* **Documento de Origem:** `Levantamento de RNF Infraestrutura.MD`
* **Data de Emissão:** 11/08/2026

### INTRODUÇÃO E OBJETIVO
Este documento especifica a infraestrutura necessária para suportar a integração em tempo real e o armazenamento de grandes volumes de dados. O foco é garantir que a "bipagem" automática e o envio de fotos de evidência não degradem a performance sistêmica, garantindo a confiabilidade dos relatórios gerados.

### DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)
| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Capacidade de Armazenamento** | Dimensionamento do servidor para banco de dados e arquivos de evidência fotográfica. | Suporte para armazenamento de fotos comprimidas vinculadas ao ID da perda por até 90 dias antes do arquivamento. |
| **Escalabilidade (RN-07)** | Capacidade de suportar o crescimento do volume de dados e multiestoques. | Arquitetura capaz de adicionar novas lojas/depósitos via configuração, sem necessidade de novo deploy de código. |
| **Resiliência e Conexão** | Mecanismo de salvamento temporário durante perda de conectividade com o servidor. | Salvar dados localmente e realizar a sincronização automática em até 2 segundos após a volta do sinal. |
| **Recuperação de Desastres** | Plano de backup automático para evitar perda de dados financeiros e operacionais. | Backups diários (às 03:00h) with RTO máximo de 4 horas em caso de falha crítica. |

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-01 (Estoque Inteligente):** A infraestrutura suporta a atualização em tempo real, impedindo que o estoque fique negativo devido a atrasos de processamento na integração.
* **RN-07 (Multiestoque):** Garante a separação lógica de saldos independentes por loja ou depósito dentro do mesmo banco de dados, permitindo transferências rastreáveis.

---

## 📊 9. CARGA E RESILIÊNCIA
* **Responsável pela Entrega:** Arthur
* **Documento de Origem:** `Carga_e_Resiliencia_1.MD`
* **Data de Emissão:** 24/08/2026

### DETALHAMENTO DOS REQUISITOS
| Requisito (RNF) | Descrição do Funcionamento | Métrica/Indicador de Sucesso |
| :--- | :--- | :--- |
| **Quantidade de Usuários Simultâneos** | Suporte a múltiplos operadores registrando perdas ao mesmo tempo em diferentes caixas. | Sistema deve suportar 20 usuários simultâneos com tempo de resposta abaixo de 2 segundos. |
| **Volume de Dados** | Suporte ao crescimento do banco de dados ao longo do tempo. | Armazenamento de até 500GB de dados operacionais e 2TB de evidências fotográficas de produtos por ano. |
| **Plano de Backup** | Cópia de segurança dos dados do sistema em intervalos regulares. | Backups completos diários às 03:00h; backups incrementais a cada 4 horas. |
| **Plano de Recuperação** | Restauração do sistema em caso de falha crítica ou perda de dados. | Tempo máximo de restauração de 4 horas; ponto de restauração máximo de 1 hora. |
| **Performance Sob Carga** | Manutenção da resposta do sistema em horários de pico. | Tempo de resposta abaixo de 3 segundos para 95% das requisições com 80% da capacidade máxima. |
| **Tolerância a Falhas** | Continuidade do serviço mesmo com falhas parciais de componentes. | Disponibilidade de 99,5% do sistema durante horário comercial (08h às 22h). |

### MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)
* **RN-01 (Estoque Inteligente):** A capacidade de múltiplos usuários simultâneos garante que perdas sejam registradas em tempo real sem atrasos, mantendo estoque atualizado.
* **RN-06 (Relatórios):** A resiliência assegura que dados de relatórios gerenciais estejam disponíveis mesmo após falhas, preservando informações financeiras.
* **RN-08 (Multi-usuário):** O suporte a 20 usuários simultâneos atende a operação de múltiplos caixas e depósitos em horário de pico.
* **RN-09 (Auditoria):** O backup diário garante preservação de logs e registros para auditoria conforme política de retenção.

### INTEGRAÇÃO E SEGURANÇA
* **Sistemas Externos:** O backup dos dados deve incluir integrações com RMS/Totvs, garantindo consistência entre sistemas em caso de restauração.
* **Privacidade:** Backups criptografados com o padrão de criptografia AES-256 e armazenados em local seguro com acesso restrito à equipe de TI, conforme LGPD.
* **Testes de Restauração:** Restauração simulada realizada mensalmente para validar integridade dos backups e cumprimento do RTO.
