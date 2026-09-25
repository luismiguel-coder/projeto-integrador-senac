
# "Controle de Acesso":

R = Controle de Acesso e um grade conjunto de regras políticas que se aplicam tanto em lugares físicos quando em lugares digitais definido quem poderá usar os recursos no sistema ou lugares restritos mostrando quando, como e sobre quais condições vão decidir se o acesso serra autorizado ou negado.

*fonte de pesquisa = https://pt.wikipedia.org/wiki/Controle_de_acesso*

# "Política de Autenticação"
 
R= e um conjunto de regras de políticas e procedimentos que garante a verificação do usuário com o dispositivo para acessar os recursos com base em senhas e biometria garantindo segurança e responsabilidade no sistemas e dispositivos. 

*fonte de pesquisa = https://www.sciencedirect.com/topics/computer-science/authentication-policy*
  

OWASP Top 10 

## 1. Controle de acesso quebrado 

**O que é:** O sistema não consegue impedir que um funcionário acesse coisas às quais não tem acesso, mesmo estando logado. 

**Exemplo no mercado:**
- Um funcionário do caixa consegue abrir o relatório de salários dos outros colaboradores. 

**Por que é perigoso:** Qualquer funcionário utilizando o sistema pode “pular” as travas e acessar dados sensíveis, como CPFs e endereços. 

**LGPD e dados de funcionários:** 
O art. 46 da LGPD exige que a empresa adote medidas técnicas e administrativas para proteger dados pessoais de seus funcionários, evitando que eles possam mexer no acesso restrito. Isso significa que o sistema precisa e deve garantir que apenas os funcionários autorizados tenham acesso ao sistema de acordo com sua área ou função de trabalho.


## 2. Falhas criptográficas 

**O que é:** Dados sensíveis trafegando entre servidores ou guardados sem criptografia adequada podem se tornar alvos fáceis para invasores. 

**Exemplo no mercado:**
- Senhas de login de funcionários salvas em texto puro no banco de dados.
- CPFs trafegando sem o protocolo seguro de transferência de hipertexto entre o sistema do caixa e qualquer outro servidor. 

**Por que é perigoso:** Se algum invasor interceptar a comunicação entre servidores e conseguir ler os dados, todas as mensagens e dados sensíveis estarão expostos. 

**LGPD e dados de funcionários:** 
No art. 46 e em guias de conformidade, é recomendado o uso de criptografia em trânsito, como a Segurança da Camada de Transporte (TLS) nas versões 1.2 e 1.3, e em armazenamento para dados pessoais, especialmente os mais sensíveis, como CPF e credenciais de acesso. As senhas devem ser armazenadas com hash forte. 


## 3. Injeção 

**O que é:** O sistema executa ou identificam um comandos como  (SQL, OS, etc.) construídos por uma pessoa mal intencionada em formato de dado que o sistema não tendo uma boa validação do que é código de uma simples pesquisa isso pode dar acesso de dados sensíveis ao intruso. 

**Exemplo no mercado:**
- Um funcionário digita algo no campo de busca de produto que, por trás, roda um comando SQL e vaza a tabela de funcionários com CPFs.
- Um script malicioso é injetado em um formulário interno e altera registros de ponto. 

**Por que é perigoso:** pois permite que o invasor possa ler, alterar ou apagar dados do banco inteiro, incluindo dados pessoais de funcionários. 

**LGPD e dados de funcionários:**  
No art. 46. Vazar ou alterar indevidamente CPFs e logins de funcionários é um incidente de segurança que a LGPD trata como tratamento inadequado/ilegal de dados pessoais.  A empresa precisa prevenir isso com consultas de parâmetros específicos, validação de entrada e testes de invasão.


## 4. Design inseguro 

**O que é:** A arquitetura do sistema foi feita sem pensar nos principais riscos com quem pode entrar? quem pode acessar? e quem pode modificar?, sem  modelagem de ameaças e sem princípios de segurança desde o início. 

**Exemplo no mercado:**
- Sistema mal projetado permitiria que qualquer funcionário logado possa explorar a base completa de funcionários, sem necessidade de perfil de administrador.

**Por que é perigoso:** Mesmo sem “bugs” clássicos, a construção do desenho errado do sistema cria brechas estruturais para vazamentos. 

**LGPD e dados de funcionários:**  
A LGPD No art. 46 fala em “segurança desde a concepção”: as medidas de proteção devem ser consideradas já na fase de projeto do produto/serviço.  Isso inclui definir claramente quem pode acessar dados de login e CPF de funcionários e limitar o mínimo necessário (princípio do menor privilégio). 

## 5. Configuração insegura de segurança 

**O que é:** quanto Servidores, bancos e aplicações do sistema ficam com configurações padrão, desnecessárias ou fracas. 

**Exemplo no mercado:**
- Painel administrativo do sistema do mercado exposto na internet com senha padrão. 

**Por que é perigoso:** Facilita muito O Invasor a entrar e invadir o sistema; muitas vezes nem precisa de técnica avançada. 

**LGPD e dados de funcionários:**  
No art. 46 da LGPD.  A empresa deve ser bem rígida no processo de segurança servidores, remover serviços desnecessários e restringir acessos administrativos. 

## 6. Componentes vulneráveis e desatualizados 

**O que é:** Uso de bibliotecas, frameworks ou softwares com falhas conhecidas e sem atualização. 

**Exemplo no mercado:**
- Sistema de gestão de estoque usando uma versão antiga de um framework web com falha crítica conhecida.
- Plugin de relatório financeiro com vulnerabilidade publicada há meses, mas nunca corrigida. 

**Por que é perigoso:** Ataques automatizados exploram essas falhas públicas para invadir sistemas e roubar dados. 

**LGPD e dados de funcionários:**  
No art. 46 e orientações da ANPD.  deve ter processo de atualização e monitoramento de vulnerabilidades em bibliotecas e firmwares do sistema. 

## 7. Falhas de identificação e autenticação 

**O que é:** O sistema não protege adequadamente o processo de login do usuário. 

**Exemplo no mercado:**
- Senhas fracas permitidas para funcionários (ex.: “123456”, “mercado2025”).
- Sessões que não expira, permitindo que qualquer pessoa que use o mesmo computador acesse a conta do funcionário.


**Por que é perigioso:** Facilita que invasores ou pessoas mal intencionadas acessem contas e, a partir delas dados sensíveis estarão extremamente expostos. 

**LGPD e dados de funcionários:**  
No art. 46. exige que a empresa proteja dados pessoais contra acessos não autorizados; falhas de autenticação aumentam diretamente esse risco.  Boas práticas recomendadas incluem políticas de senha fortes, Autenticação Multifator MFA para painéis administrativos e controle de sessão. 

## 8. Falhas de integridade de software e dados 

**O que é:** O sistema aceita atualizações, scripts ou dados de fontes não confiáveis sem verificar adequada a origem. 

**Exemplo no mercado:**
- Sistema de um servidor baixa atualizações de outro servidor sem assinatura digital, permitindo que um invasor injete código malicioso.
- Planilha de controle de funcionários carregada a partir de link externo sem validação, alterando CPFs e dados de login. 

**Por que é perigoso:** Permite que códigos ou dados alterados rodem dentro do ambiente da empresa, comprometendo a integridade dos dados pessoais. 

**LGPD e dados de funcionários:**  
No art. 46 da LGPD manda a empresa se proteger.  A organização deve garantir integridade de atualizações e dados críticos (assinatura digital, validação, controle de mudanças). 

## 9. Falhas de registro e monitoramento 

**O que é:** O sistema não registra (loga) adequadamente acessos e ações, ou ninguém monitora esses logs. 

**Exemplo no mercado:**
- Ninguém sabe quem acessou o relatório de funcionários com CPFs na última semana.
- Tentativas de login falhas em massa não geram alerta, permitindo ataques de força bruta. 

**Por que é perigoso:** Sem logs e monitoramento, a empresa demora para perceber invasões e não consegue investigar quem acessou ou vazou dados. 

**LGPD e dados de funcionários:**  
O art. 48 da LGPD exige notificação à Agência Nacional de Proteção de Dados (ANPD)  em caso de incidente de segurança; sem logs, fica difícil detectar, investigar e comprovar o que aconteceu.  A lei e guias de conformidade recomendam trilha de auditoria, retenção de logs de acesso (ex.: 6 meses) e monitoramento contínuo como medidas técnicas para proteger dados pessoais, incluindo login e CPF de funcionários. 

## 10. Falsificação de solicitação no lado do servidor 

**O que é:** O servidor faz requisições para 
Localizador Uniforme de Recursos (URLs) informadas pelo usuário sem validar, permitindo que um atacante ou um invasor possa acessar sistemas internos. 

**Exemplo no mercado:**
- Funcionalidade que “importa dados de fornecedor” a partir de uma URL digitada pelo funcionário, e o atacante usa isso para acessar serviços internos que guardam dados de Recursos Humanos RH deixando dados sensíveis expostos 

**Por que é perigoso:** Pode dar acesso para atacante ou um invasor de formar indireto no sistemas e bancos de dados que não deveriam estar expostos, incluindo bases com CPFs e logins. 

**LGPD e dados de funcionários:**  
Se uma Falsificação de Requisição no Lado do Servidor SSRF permitir acesso não autorizado a dados pessoais de funcionários, a empresa estará descumprindo o dever de proteção do art. 46 da LGPD.  A mitigação inclui validar e restringir Localizador Uniforme de Recursos URLs permitidas e segmentar a rede para limitar o que o servidor pode acessar. 

## Como a LGPD exige proteção específica para login e CPF de funcionários 

De forma direta: 

- **Art. 46 da LGPD:** determina que empresas ou agentes de tratamento adotem **medidas de segurança técnicas e administrativas** para proteger dados pessoais contra:
  - acessos não autorizados;
  - destruição, perda, alteração, comunicação ou difusão indevida;
  - qualquer forma de tratamento inadequado ou ilícito. 

- **Dados de login e CPF** são dados pessoais que identificam diretamente o funcionário. Por isso:
  - Devem ter **controle de acesso restrito** somente quem precisa, como  Recursos Humanos RH e o próprio funcionário, quando aplicável.
  - Devem ser protegidos com **criptografia em trânsito e em repouso**, senhas com impressão digital hash forte e políticas de autenticação adequadas.
  - O acesso a esses dados deve gerar **logs de auditoria** quem acessou?, quando?, de onde?, retidos por período definido, para permitir investigação em caso de incidente.

- Em caso de **vazamento ou acesso indevido** a esses dados, a empresa deve:
  - Ter um **plano de resposta a incidentes**;
  - Notificar a Autoridade Nacional de Proteção de Dados ANPD e, quando cabível, os titulares (funcionários), conforme art. 48 da LGPD.
