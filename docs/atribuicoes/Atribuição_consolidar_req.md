# 📢 DIRETRIZES DE COMUNICAÇÃO E FLUXO DE REPORTES

Para garantir que o nosso projeto ande rápido e ninguém fique travado ou sobrecarregado, estabelecemos uma regra de comunicação direta. Se você tiver alguma dúvida, precisar de dados ou for entregar a sua atividade, siga **estritamente** os caminhos abaixo:

A partir de agora, não aceitaremos mais arquivos DOCX (Word), apenas arquivos MD (Markdown)
---

### 🚨 1. CANAIS DE REPORTE PARA INTEGRANTES DE APOIO (QUEM FALA COM QUEM?)

*   **WILLIAM** ➡️ Deve se comunicar **única e exclusivamente** com o **LUIS MIGUEL** (Líder do Backend e Líder Geral).
    *   *O que tratar:* Tirar dúvidas sobre os termos de segurança (NIST, OWASP) e enviar o arquivo de Word do guia teórico de segurança para a validação do Luis Miguel antes de juntar ao documento final.
*   **ARTHUR** ➡️ Deve se comunicar **única e exclusivamente** com a **KAMILA** (Líder de Qualidade). 
    *   *O que tratar:* Tirar dúvidas sobre a montagem do dicionário de Termos do projeto e enviar o arquivo parcial/final para ela revisar e formatar.
*   **LUIZ CARLOS** ➡️ Deve se comunicar **única e exclusivamente** com o **EDIGELSON** ou com a **KAMILA**.
    *   *O que tratar:* Solicitar ao **YURI** os códigos de cores das telas para ajudar fazer os testes de contraste no Coolors, mas enviar as dúvidas e a tabela final de testes apenas para o **EDIGELSON** ou para a **KAMILA** revisarem. 
    (EM CASO DE AUSÊNCIA DE YURI O PAPEL PODE SER INVESTIDO LUIZ CARLOS MANDAR AS OPÇÕES DE CORES JÁ ACESSÍVEL PARA O YURI)
---

### 💼 2. INTEGRAÇÃO E APOIO ENTRE GRUPOS

*   **YURI** ➡️ Deve passar os códigos hexadecimais das cores que usou nas telas do sistema para o **LUIZ CARLOS** realizar a verificação de acessibilidade.
*   **ALAÍDE** e **EMILLI** ➡️ Trabalham em contato direto com o **LUIS MIGUEL** para alinhar as tabelas, as regras reais de funcionamento do mercado e o preenchimento do dicionário de dados do banco.
*   **PEDRO** e **YURI** ➡️ Trabalham pareados e em contato direto para amarrar os Casos de Uso com o que vai aparecer visualmente em cada tela.

---


📢 **DIVISÃO OFICIAL DE TAREFAS — CONSOLIDAÇÃO DE REQUISITOS**

Pessoal, segue a nossa divisão de tarefas para a entrega de **Consolidação de Requisitos**, com as atividades ajustadas e focadas em ferramentas diretas. 

Lembrando da nossa **Regra de Acompanhamento Diário**: cada um deve apresentar uma pequena evidência de progresso a cada dia útil para o seu respectivo contato de reporte (pode ser um rascunho, print de tela ou as dúvidas que surgirem).

---

### 👥 **GRUPO 1: NEGÓCIOS & QUALIDADE (Não-Técnico)**

*   **Kamila (Líder de Qualidade)**
    *   **O que fazer:** Organizar todos os requisitos levantados por categorias, numerar cada um na ordem padrão (**RF001, RF002, RNF001, RNF002**) e acompanhar os prazos e reportes diários dos membros do Grupo 1.
*   **Emilli (Vice-Líder de Documentação)**
    *   **O que fazer:** Listar todos os stakeholders (envolvidos) do projeto (dono do mercado, estoquista, gerente de prevenção, TI, etc.) e explicar em uma frase simples qual é o papel e a necessidade de cada um deles em relação ao sistema.
*   **Alaíde**
    *   **O que fazer:** Escrever e consolidar as regras de negócio do mercado (explicar o vencimento FEFO, o que o gerente deve fazer se houver furos de estoque acima de 5%, e os dados obrigatórios na hora de registrar um descarte).
*   **Arthur**
    *   **Tarefa de Apoio:** **Glossário de Termos e Definições do Projeto.**
    *   **Como fazer na prática:** Você vai montar uma tabela listando e explicando de forma simples e clara cada termo técnico e de varejo que usamos no projeto (ex: *FEFO, XML de Nota Fiscal, Logs Imutáveis, RTO, RPO, SLA, Timeout, RBAC, Bipagem, Avarias, Divergência de Estoque, RMS, Totvs*). Você deve escrever um parágrafo para cada termo explicando o que ele significa e como ele é aplicado na prática no nosso sistema.

---

### 👥 **GRUPO 2: FRONT-END (Telas & Usabilidade)**

*   **Pedro (Vice-Líder do Front-End)**
    *   **O que fazer:** Escrever os Casos de Uso ou Histórias de Usuário, explicando o caminho exato que o operador e o gerente fazem na tela para registrar e aprovar perdas (garantindo o limite de no máximo **3 cliques** a partir da tela inicial).
*   **Yuri**
    *   **O que fazer:** Listar tudo o que cada tela do sistema precisa ter obrigatoriamente (campos de digitação, botões de ação, avisos de carregamento visual e as travas físicas para evitar duplo clique no botão de salvar).
*   **Luiz Carlos**
    *   **Tarefa de Apoio:** **Teste e Verificação de Contraste Visual de Telas.**
    *   **Ferramenta:** **Coolors Contrast Checker** (site gratuito e simples online).
    *   **Como fazer na prática:** Você vai abrir o site `coolors.co/contrast-checker`. vai passar as cores de fundo e de texto para que serão utilizada nas telas. Você vai colar esses códigos de cores lá e o site vai te dar uma nota automática dizendo se o contraste passou ou não (**Aprovado** ou **Reprovado**). Registre esses testes em um arquivo **MD** mostrando as 20 combinações testadas com suas respectivas notas.

---

### 👥 **GRUPO 3: BACK-END & BANCO DE DADOS**

*   **Luis Miguel (Líder Geral do Projeto / Líder do Backend)**
    *   **O que fazer:** Criar a Matriz de Rastreabilidade (a tabela que conecta os requisitos de tela com as tabelas do banco de dados), consolidar os requisitos técnicos de segurança/criptografia do backend e validar o documento final unificado com o orientador do Senac.
*   **Edigelson (Líder Técnico)**
    *   **O que fazer:** Analisar toda a lista de requisitos e definir as prioridades (Alta, Média ou Baixa de acordo com o que é essencial para o desenvolvimento) e detalhar a integração técnica de APIs com os sistemas RMS e Totvs.
*   **William**
    *   **Tarefa de Apoio:** **Guia Conceitual Teórico de Segurança e LGPD.**
    *   **Como fazer na prática:** Escrever um texto explicativo simples e teórico definindo as principais vulnerabilidades de segurança de sistemas (padrão OWASP Top 10) aplicáveis ao mercado, e como as leis da LGPD exigem que os dados de login e CPFs dos funcionários sejam armazenados de forma protegida.

---