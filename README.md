# 🛒Sistema de Gestão Inteligente de Perdas no Varejo

&gt; **Projeto Integrador — Senac**  
&gt; *Solução para prevenção de perdas em supermercados, controle de validade, recepção de notas fiscais (XML) e auditoria imutável de estoque.*

---

## 📌 Sobre o Projeto

É um sistema desenvolvido para o ambiente de supermercados e varejo alimentício com o objetivo de **reduzir perdas de produtos e maximizar a lucratividade** por meio do controle rigoroso de estoque, e conformidade com normas de segurança da informação e privacidade de dados.

A solução substitui cadastros manuais propensos a erros por um fluxo seguro de **Importação da NF-e via XML**, seguido por uma **Conferência Cega na Doca** executada pelo estoquista via leitor de código de /barras USB (EAN) ou digitação manual. O sistema aplica rigorosamente a regra **FEFO** (*First Expired, First Out*), mantendo uma **trilha de logs imutável (RN-09)** para auditoria antifraude e total adequação à **LGPD**.

---

## 🚀 Principais Funcionalidades (Escopo MVP)

* **📥 Recebimento Fiscal Automatizado:** Parser e importação do arquivo `.xml` da Nota Fiscal Eletrônica (NF-e) executados pelo setor fiscal/administrativo, cadastrando automaticamente produtos e quantidades esperadas sem expor custos ao operador de pátio.
* **📦 Conferência Cega na Doca:** Interface operacional limpa onde o estoquista bipa o código EAN do produto físico e registra a quantidade contida, lote e data de validade (FEFO), sem acesso a preços de custo ou margens de lucro (**RN-06 / RBAC**).
* **⚠️ Registro e Aprovação de Avarias (UC03 / UC05):** Lançamento simplificado de itens danificados ou vencidos com obrigatoriedade de justificativa e foto de evidência, encaminhando o registro para a fila de decisão e baixa do Gerente.
* **🔒 Trilha de Logs Imutáveis &amp; Segurança (RN-09):** Gravação em banco de dados de todas as movimentações, logins e alterações críticas com carimbo de tempo em milissegundos e ID do operador.
* **🛡️ Proteção de Senhas &amp; LGPD:** Criptografia de credenciais utilizando **Argon2id**, comunicação via HTTPS/TLS e rotinas de anonimização de PII em caso de desligamento de colaboradores.

---

## 🛠️ Arquitetura e Tecnologias

* **Frontend:** Web / PWA (HTML5, CSS3, JavaScript ES6) — Focado em usabilidade e responsividade para dispositivos móveis e desktops.
* **Backend:** API REST (Python / Node.js) — Processamento de rotas de autenticação (JWT), parser de XML e regras de negócio.
* **Banco de Dados:** Relacional (PostgreSQL / MySQL / SQLite) — Modelagem estruturada com segregação de tabelas de log e suporte a transações ACID.
* **Segurança:** Argon2id (hash de senhas), AES-256 (dados em repouso), RBAC (controle de acesso baseado em papéis) e diretrizes OWASP Top 10.

---

## 📁 Estrutura do Repositório


projeto-integrador-senac/
├── docs/                      # Especificações técnicas, Requisitos (RF/RNF), Casos de Uso e Guias
│   ├── requisitos/            # Matriz de rastreabilidade, RNF e especificações de segurança
│   └── seguranca/             # Guia conceitual OWASP Top 10 e adequação à LGPD
├── backend/                   # Código-fonte da API REST (Rotas, Controllers e Parser XML)
├── frontend/                  # Interfaces Web/PWA (Telas de Login, Conferência e Painel do Gerente)
├── database/                  # Scripts SQL 
└── README.md                  # Apresentação e documentação principal do projeto


### Passo a Passo

1. Clone o repositório:

```
git clone https://github.com/luismiguel-coder/projeto-integrador-senac.git
cd projeto-integrador-senac
```