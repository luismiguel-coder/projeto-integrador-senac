# Consolidação dos Requisitos Técnicos de Segurança e Criptografia do Backend

**Responsável pela Entrega:** Luis Miguel  
**Projeto:** Sistema de Gestão de Perdas – Supermercado  
**Data:** 08/009/2026  

---

## 1. Introdução e Diretrizes de Segurança

Este documento estabelece as especificações técnicas de **Segurança da Informação, Criptografia, Tratamento de Logs e Conformidade com a LGPD** para o Sistema de Gestão de Perdas. O objetivo é garantir a proteção integral dos dados corporativos e pessoais, mantendo uma trilha de auditoria imutável contra fraudes e erros de lançamento, alinhada às melhores práticas globais de segurança cibernética e privacidade de dados.

---

## 2. Criptografia Avançada de Credenciais (Argon2)

O sistema adota o estado da arte em proteção de credenciais recomendado por órgãos internacionais de segurança:

* **Algoritmo Padrão:** Utilização da função de derivação de chave **Argon2id** (vencedora do *Password Hashing Competition* e recomendada pelo OWASP). O Argon2id combina defesas contra ataques de canal lateral e ataques de força bruta baseados em hardware especializado (GPUs e ASICs).
* **Salts Criptográficos e CSPRNG:** Cada senha gerada ou redefinida recebe obrigatoriamente um *salt* criptográfico exclusivo de no mínimo 128 bits, gerado por um gerador de números pseudoaleatórios criptograficamente seguro (CSPRNG).
* **Parâmetros de Ajuste (Memory-Hard):** O algoritmo é configurado com alto custo de memória para dificultar ataques em massa:
  * **Consumo de memória dedicado:** m = 65536 (64 MB)
  * **Fator de paralelismo:** p = 4
  * **Número de iterações (tempo):** t = 3

---

## 3. Controle de Acesso (RBAC) e Segregação de Tela (Front-End e Back-End)

Para diminuir o risco de vazamento de dados financeiros e cumprir o Princípio do Mínimo Privilégio:

* **Bloqueio no Front-end:** O sistema lê o perfil do usuário no momento do login. Menus sensíveis (como Relatórios Financeiros e Custos de Perdas) são completamente ocultados, e qualquer tentativa de acesso direto via URL é interceptada e respondida com "Acesso Negado".
* **Travas no Back-end:** O acesso a dados sensíveis é regulado na camada de serviços (API) e no banco de dados por meio de políticas rígidas de autorização (RBAC), DTOs filtrados e middlewares de validação de escopo. O perfil Estoquista possui restrição absoluta de 100% na visualização de custos e margens corporativas, acessando apenas os endpoints e tabelas estritamente necessários para o registro de avarias entre outras funções interligada a seu perfil.

---

## 4. Gestão de Logs, Rotação, Retenção e Exigências da LGPD

Os logs do sistema foram arquitetados para equilibrar a rastreabilidade antifraude com o respeito à privacidade de dados pessoais previstos na legislação brasileira.

### Segregação Funcional dos Logs

Os arquivos e tabelas de log são divididos por funções para facilitar a auditoria e a gestão de acesso:

* **log_usuario_acesso:** Trilha de autenticação, falhas de login e endereços IP.
* **log_bipagem:** Histórico de entradas e movimentações físicas de estoque.
* **log_acoes_criticas:** Exclusões, ajustes e aprovações de descartes.
* **log_acesso_seguranca:** Focado na infraestrutura de autenticação e perímetro. Registra tentativas de login (sucessos e falhas), bloqueios temporários de conta por força bruta, IPs de origem, horários de acesso, expirações de sessão por timeout e alterações de credenciais.
* **log_movimentacao_estoque:** Focado na operação diária de perdas e avarias. Registra as operações de entrada, leituras de código de barras (bipagem de produtos estragados/avarias - UC02), atualizações físicas de estoque e registros de validade, contendo o carimbo de tempo em milissegundos e o ID do operador.
* **log_transacoes_financeiras:** Focado na custódia de valores. Registra visualizações de relatórios gerenciais, consultas a custos de perdas por parte de perfis autorizados (Analista de Prevenção de Perdas) e interações sensíveis com dados de margem corporativa.
* **log_governanca_administrativa:** Focado no controle de privilégios e mudanças de estado estruturais do sistema (UC05 e UC10). Registra aprovações ou rejeições de descartes físicos de perdas, alterações globais de parâmetros, modificações em tabelas de base de dados e concessões ou remoções de permissões de usuários executadas pelo Administrador.

### Identificação de Ações Autônomas (IA)

Quando o Agente de IA disparar um alerta ou sugestão automática de desconto/perda, o log registrará o evento gravando o autor como `ID_USUARIO = "SISTEMA_IA"`, garantindo que ações automatizadas possuam rastreabilidade completa.

### Rotação de Logs (Com Limites Rígidos de Tamanho)

Os logs passam por rotação periódica automática para balancear o uso de armazenamento do servidor local e manter a legibilidade dos arquivos:

* **Gatilho por Tamanho de Arquivo:** A rotação é disparada automaticamente assim que qualquer arquivo de log atinge o limite máximo de **10 MB** por arquivo.
* **Limite de Arquivos Rotacionados:** O sistema mantém até **10 arquivos históricos rotacionados** por categoria de log (totalizando um buffer ativo máximo de **100 MB** por módulo antes do arquivamento).
* **Compactação Automática:** Logs que sofrerem rotação são compactados no formato `.gz` / `.zip` de forma automática para otimizar o espaço em disco do servidor local mantendo a integridade imutável (*append-only*).

### Retenção e Exclusão para Funcionários Desligados (LGPD)

* **Prazo de Retenção:** Os logs de auditoria geral são mantidos pelo período mínimo de **12 meses** para fins fiscais e de conformidade.
* **Anonimização de Dados Sensíveis:** Caso um funcionário seja desligado, os dados de identificação pessoal (PII) atrelados aos metadados dos logs operacionais antigos são anonimizados (substituídos por hashes irreversíveis ou identificadores genéricos como `USER_EXC_[HASH]`). Isso atende aos direitos do titular previstos nos artigos 15 e 16 da LGPD, preservando a integridade estatística do histórico de estoque.

---

## 5. Referências Técnicas e Sites Consolidados de Segurança

As diretrizes de segurança, criptografia e tratamento de logs deste documento foram baseadas nos padrões e documentações dos seguintes sites e organizações de referência global:

* **Governo Federal / ANPD (Autoridade Nacional de Proteção de Dados):** Diretrizes sobre o ciclo de vida dos dados, eliminação e boas práticas de adequação à **LGPD (Lei nº 13.709/2018)**.
  * *Consulta oficial:* **Portal GOV.BR - LGPD** (`https://www.gov.br/anpd`)
* **Cisco Systems (Cybersecurity & Threat Intelligence):** Padrões de arquitetura de rede segura, segmentação de perfis de acesso (RBAC) e melhores práticas para mitigação de riscos de vazamento de dados corporativos.
  * *Consulta oficial:* **Cisco Security Center** (`https://www.cisco.com/c/en/us/products/security`)
* **NIST (National Institute of Standards and Technology):** Orientações de gerenciamento de identidades, diretrizes de senhas e proteção de trilhas de auditoria (**NIST SP 800-63B**).
  * *Consulta oficial:* **NIST Computer Security Resource Center** (`https://csrc.nist.gov/`)
* **OWASP (Open Worldwide Application Security Project):** Especificações técnicas consolidadas para armazenamento seguro de senhas utilizando **Argon2id** e prevenção contra falhas de controle de acesso.
  * *Consulta oficial:* **OWASP Password Storage Cheat Sheet** (`https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html`)
