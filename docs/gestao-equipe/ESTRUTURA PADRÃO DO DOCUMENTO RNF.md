---
title: "**ESTRUTURA PADRÃO DO DOCUMENTO DE ENTREGA**"
---

**\[CABEÇALHO\]**

- **Projeto:** Sistema de Gestão de Perdas – Supermercado

- **Documento:** Especificação de Requisitos Não Funcionais (RNF)

- **Equipe Responsável:** Grupo \[1, 2 ou 3\]

- **Líder de Área:** \[Nome do Líder\]

- **Data de Emissão:** \[DD/MM/AAAA\]

------------------------------------------------------------------------

**1. INTRODUÇÃO E OBJETIVO**

*(O membro deve escrever em 2 ou 3 linhas o que este documento define e
por que ele é importante para o sistema, baseando-se no objetivo de
reduzir perdas)*

**2. DETALHAMENTO DOS REQUISITOS (ESPECIFICAÇÃO TÉCNICA)**

*Esta é a parte principal. Cada requisito deve ser detalhado seguindo
esta tabela de métricas:*

| **Requisito (RNF)** | **Descrição do Funcionamento** | **Métrica/Indicador de Sucesso** |
|----|----|----|
| **Exemplo: Backup** | Como os dados serão salvos. | Cópia diária às 03:00h; Retenção de 5 anos (RN-09). |
| **\[Item do Grupo\]** | \[Explicação simples e sem "lixo de IA"\] | \[Número real: segundos, GB, %, etc.\] |
| **\[Item do Grupo\]** | \[Explicação simples e sem "lixo de IA"\] | \[Número real: segundos, GB, %, etc.\] |

**3. MAPEAMENTO DE REGRAS DE NEGÓCIO (RN)**

*(Aqui o membro deve ligar o requisito às regras oficiais do projeto)*

- **RN-XX:** \[Nome da Regra\] – Como este requisito ajuda a cumprir
  essa regra? (Ex: O Log de Auditoria garante o cumprimento da **RN-09**
  sobre histórico imutável).

**4. INTEGRAÇÃO E SEGURANÇA (Se aplicável)**

*(Se o grupo for o do Ed ou tratar de dados sensíveis)*

- **Sistemas Externos:** Como o requisito se comporta com **RMS e
  Totvs**?

- **Privacidade:** Como o requisito respeita a **LGPD** e os perfis de
  acesso (Gerente vs. Estoquista)?

**5. VALIDAÇÃO DO LÍDER DE ÁREA**

*(Espaço para o líder confirmar que filtrou o trabalho dos membros)*

- **Revisão técnica realizada por:** \[Nome do Líder\]

- **Parecer:** ( ) Aprovado \| ( ) Necessita Ajustes

- **Notas do Líder:** \[Comentários sobre a qualidade da entrega\]

------------------------------------------------------------------------

**COMO CADA GRUPO DEVE PREENCHER O CAMPO 2 (EXEMPLOS):**

- **Grupo 1 (Emilli):** No item **Monitoramento e Logs**, a métrica deve
  ser: *"O sistema deve registrar ID, IP, Data e Hora de toda exclusão
  de produto, conforme a RN-09"*.

- **Grupo 2 (Pedro):** No item **Interface Intuitiva**, a métrica deve
  ser: *"O operador deve conseguir registrar uma perda com no máximo 3
  cliques a partir da tela inicial"*.

- **Grupo 3 (Ed):** No item **Capacidade de Armazenamento**, a métrica
  deve ser: *"O banco de dados deve suportar 500GB de imagens de
  evidências fotográficas por ano"*.
