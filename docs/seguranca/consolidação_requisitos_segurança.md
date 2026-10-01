# Consolidação dos Requisitos Técnicos de Segurança e Criptografia Backend

**Projeto:** Sistema de Registro de Perdas para Supermercado  

**Documento:** Consolidação Técnica de Segurança, Criptografia

**Linguagem & Ambiente:** Python (FastAPI) 

**Responsável Técnico:** Luis Miguel  
**Data:** 29/09/2026  

---

### 1. Introdução e Diretrizes de Arquitetura
Este documento consolida os **requisitos técnicos de segurança, criptografia e proteção de dados** aplicados no desenvolvimento do backend em Python e na hospedagem no servidor, atendendo rigorosamente à **LGPD (Lei Geral de Proteção de Dados)** e garantindo controle contra fraudes operacionais.

---

### 2. Autenticação e Controle de Acesso Baseado em Perfil (RBAC)
O sistema implementa o modelo de segurança **RBAC (Role-Based Access Control)** com exatamente **3 perfis de usuários**:

1. **Perfil 1: Operador de Loja / Fiscal**
   * *Escopo:* Acesso via celular/PWA.
   * *Permissões:* Lançamento de novas perdas, anexo de fotos, consulta apenas das suas próprias digitações do dia.
   * *Restrições:* Sem acesso a valores financeiros consolidados, relatórios globais ou logs de auditoria.

2. **Perfil 2: Supervisor de Setor**
   * *Escopo:* Acesso via Celular e PC.
   * *Permissões:* Leitura e validação de perdas do seu setor de atuação, emissão de relatórios quantitativos.
   * *Restrições:* Não pode alterar logs ou gerenciar usuários do sistema.

3. **Perfil 3: Gerente / Administrador**
   * *Escopo:* Acesso via PC (Web App).
   * *Permissões:* Acesso total aos Dashboards financeiros, relatórios comparativos, exportações (PDF/Excel), cadastro de parâmetros e consulta ao **Relatório de Auditoria**.

---

### 3. Requisitos Técnicos de Criptografia no Backend (Python)

#### 3.1. Proteção de Credenciais e Senhas
* **Algoritmo de Hash:** As senhas dos usuários nunca são armazenadas em texto simples. O backend utiliza  **Argon2** com fator de custo (*salt*) individual configurado em no mínimo 12 rounds.
* **Autenticação Stateless:** Emissão de tokens seguros **JWT (JSON Web Tokens)** assinados com chave secreta forte (HMAC SHA-256) com tempo de expiração curto (ex.: 8 horas) e rotação de refresh token.

#### 3.2. Criptografia em Trânsito e em Repouso (LGPD)
* **Em Trânsito (HTTPS):** Toda a comunicação entre o navegador/celular e o servidor é obrigatoriamente criptografada via **TLS 1.3 / HTTPS** configurado no servidor web.
* **Em Repouso (Banco de Dados):** Dados sensíveis de identificação e logs de auditoria utilizam criptografia de coluna via algoritmo **AES-256**.

---

### 4. Segurança no Upload e Armazenamento de Fotos de Comprovação
Como o sistema exige o anexo de fotos de produtos avariados tiradas pelo celular, o backend Python aplica as seguintes travas de segurança no arquivo recebido:

1. **Validação Rigorosa do Arquivo:**
   * Verificação do **MIME Type real** do arquivo (`image/jpeg`, `image/png`) e leitura dos primeiros bytes do cabeçalho (*magic bytes*), descartando executáveis renomeados.
   * Limite estrito de tamanho de arquivo: **máximo 5MB por foto**.
   * Processamento e compressão automática da imagem via biblioteca `Pillow` em Python antes do salvamento.
2. **Sanitização de Nome e Caminho (Anti-Path Traversal):**
   * O nome original do arquivo enviado pelo celular é descartado. O servidor renomeia a foto usando um hash único **UUIDv4** (ex.: `f47ac10b-58cc-4372-a567-0e02b2c3d479.jpg`).
3. **Isolamento no Ubuntu Server:**
   * O diretório de armazenamento das mídias (`/var/www/perdas_media/`) possui permissão de gravação sem permissão de execução de scripts (`noexec`).

---

### 5. Trilha de Auditoria Imutável e Soft Delete

#### 5.1. Log Imutável de Auditoria
* Cada requisição no backend que altere estado (INSERT, UPDATE) passa por um **Middleware de Auditoria em Python**.
* O middleware captura automaticamente:
  * `usuario_id` e `perfil` da sessão JWT ativa.
  * `ip_origem` e cabeçalho `User-Agent` (identificando o modelo do celular/PC).
  * `data_hora` com precisão de milissegundos do servidor.
  * Snapshot no formato `JSONB` dos dados anteriores e novos.
* Gravado na tabela `tb_logs_auditoria` sem permissão de exclusão/alteração no banco.

#### 5.2. Inativação Lógica (*Soft Delete*)
* Para garantir que desativar um motivo, setor ou usuário antigo não quebre o histórico dos relatórios financeiros do passado, o sistema utiliza a flag `status: True/False` (Ativo/Inativo) em todas as tabelas de cadastro.

---

### 6. Proteção da API e Hardening
1. **CORS Restrito:** A API aceita requisições apenas do domínio oficial da aplicação do supermercado.
2. **Prevenção de SQL Injection:** Uso obrigatório de ORM em Python (**SQLAlchemy** / **SQLModel**) com consultas parametrizadas.
3. **Rate Limiting:** Proteção contra ataques de força bruta nas rotas de login (máximo 5 tentativas por minuto por IP).
