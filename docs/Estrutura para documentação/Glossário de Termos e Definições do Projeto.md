**REGISTRO DE ENTREGA**

**Projeto:** Projeto entregador

**Responsável:**

**Data:**

**Equipe:**

**1. O QUE FOI SOLICITADO?**

Faça um pequeno resumo sobre o que você entendeu que deveria ser
realizado.

(Montar uma tabela listando e explicando de forma simples e clara cada
termo técnico e de varejo que usamos no projeto**.**)

**2. SUA ENTREGA**

Coloque aqui o que você produziu ou realizou para atender à solicitação.

# (Cop **GLOSSÁRIO DE TERMOS TÉCNICOS E DE VAREJO**

<table style="width:100%;">
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p><strong>FEFO</strong></p>
<p><strong>É um método de gestão de estoque que prioriza a saída
dos produtos cuja data de validade está mais próxima, independentemente
de terem entrado primeiro no estoque.</strong></p></th>
<th>É o método de gestão de estoque que prioriza a saída dos produtos
com <strong>data de validade mais próxima</strong>. Na prática, o
sistema utiliza as datas de validade registradas no estoque para indicar
ou priorizar qual lote deve ser separado primeiro, ajudando a reduzir
perdas por vencimento.</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><p><strong>XML de Nota
Fiscal</strong></p>
<p><strong>arquivo eletrônico da NF-e</strong></p></td>
<td>É o arquivo digital, normalmente em formato XML, que contém as
informações estruturadas de uma Nota Fiscal Eletrônica (NF-e), como
produtos, quantidades, valores, impostos e dados do fornecedor. No
sistema, o XML pode ser utilizado para importar e conferir
automaticamente os dados da nota durante o recebimento das mercadorias,
reduzindo erros de digitação.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>Logs Imutáveis</strong></p>
<p><strong>registros de eventos que não podem ser
alterados</strong></p></td>
<td>São registros de atividades do sistema que, depois de gravados, não
podem ser alterados ou apagados de maneira comum. Na prática, são
utilizados para manter um histórico confiável das operações, como
movimentações de estoque, alterações de informações e ações realizadas
pelos usuários, permitindo auditoria e rastreabilidade.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>RTO</strong></p>
<p><strong>É o tempo máximo aceitável para que um sistema ou serviço
seja restaurado após uma falha ou indisponibilidade.</strong></p></td>
<td><strong>RTO (Recovery Time Objective)</strong> representa o tempo
máximo aceitável para que um sistema seja restaurado após uma falha. Por
exemplo, se o RTO definido para o sistema for de 2 horas, o objetivo é
que o serviço volte a funcionar dentro desse período após uma
indisponibilidade.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>RPO</strong></p>
<p><strong>É o período máximo de dados que a empresa aceita perder
em caso de uma falha ou indisponibilidade do sistema. Ele indica até
quanto tempo antes do incidente os dados precisam estar disponíveis para
recuperação.</strong></p></td>
<td><strong>RPO (Recovery Point Objective)</strong> representa a
quantidade máxima de dados que pode ser perdida em caso de falha,
considerando o momento do último backup ou replicação. Por exemplo, um
RPO de 15 minutos significa que, em uma situação de desastre, o sistema
deve buscar limitar a perda de dados aos últimos 15 minutos.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>SLA</strong></p>
<p><strong>É um acordo que estabelece os níveis de serviço que devem
ser cumpridos, como disponibilidade do sistema, tempo de resposta,
prazo para atendimento e resolução de problemas.</strong></p></td>
<td><strong><br />
SLA (Service Level Agreement)</strong> é o acordo que estabelece os
níveis de serviço esperados, como disponibilidade, tempo de atendimento
e prazo para resolução de problemas. No sistema, pode ser utilizado para
definir, por exemplo, o prazo máximo para atendimento de uma ocorrência
ou o percentual mínimo de disponibilidade da aplicação.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>Timeout</strong></p>
<p><strong>limite de tempo para uma operação aguardar
resposta</strong></p></td>
<td><strong><br />
Timeout</strong> é o tempo máximo que o sistema aguarda uma resposta de
outro serviço, operação ou conexão antes de considerar que houve uma
falha. Na prática, evita que uma integração fique esperando
indefinidamente e permite que o sistema apresente uma mensagem de erro
ou execute uma nova tentativa.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>RBAC</strong></p>
<p><strong>É um modelo de segurança utilizado para controlar o que cada
usuário pode acessar ou executar dentro de um sistema, de acordo com seu
perfil ou função.</strong></p></td>
<td><strong>RBAC (Role-Based Access Control)</strong> é um modelo de
controle de acesso baseado em papéis ou funções. Na prática, o sistema
pode possuir perfis como administrador, operador de estoque e gestor,
permitindo que cada usuário acesse somente as funcionalidades
necessárias para sua função.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>Bipagem</strong></p>
<p><strong> leitura de código de barras</strong></p></td>
<td><strong>Bipagem</strong> é a leitura de um código de barras ou outro
identificador utilizando um leitor ou dispositivo móvel. No sistema, a
bipagem pode ser usada para confirmar produtos, volumes, endereços ou
documentos durante processos como recebimento, separação, conferência e
expedição.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>Avarias</strong></p>
<p><strong>produtos danificados ou inadequados para
venda</strong></p></td>
<td><strong>Avarias</strong> são danos ou condições inadequadas
identificadas em produtos ou embalagens, como itens quebrados, amassados
ou violados. No sistema, uma avaria pode ser registrada durante o
recebimento ou movimentação do estoque, permitindo identificar o produto
afetado, sua quantidade, motivo e responsável pelo registro.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p><strong>Divergência de
Estoque</strong></p>
<p><strong>diferença entre estoque físico e estoque registrado no
sistema</strong></p></th>
<th>Divergência de estoque ocorre quando a quantidade registrada no
sistema é diferente da quantidade encontrada fisicamente no estoque. Na
prática, o sistema pode registrar a diferença durante uma contagem ou
conferência, gerar uma ocorrência e permitir a análise e eventual ajuste
do saldo.</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><p><strong>RMS</strong></p>
<p><strong>É um sistema utilizado para administrar e controlar
processos relacionados à operação do varejo, como produtos, preços,
lojas, estoque, vendas e movimentações.</strong></p></td>
<td>RMS (Retail Management System) é um sistema utilizado para apoiar a
gestão das operações de varejo, podendo controlar informações
relacionadas a produtos, estoque, lojas, vendas e movimentações. Na
prática, o RMS pode atuar integrado ao sistema do projeto, fornecendo ou
recebendo informações necessárias para manter os dados operacionais
sincronizados.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>TOTVS</strong></p>
<p><strong>plataforma/empresa de soluções de gestão
empresarial</strong></p></td>
<td>TOTVS é uma empresa brasileira de tecnologia que oferece sistemas de
gestão empresarial, incluindo soluções utilizadas por empresas de
varejo, logística e outros setores. No contexto do projeto, o TOTVS pode
representar um sistema externo com o qual a solução precisa realizar
integrações, trocando informações como produtos, notas fiscais, estoque
ou movimentações.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>API</strong></p>
<p><strong>é uma interface que permite que diferentes sistemas,
aplicações ou serviços se comuniquem e troquem informações de
forma padronizada.</strong></p></td>
<td>API (Application Programming Interface) é um mecanismo que permite
que diferentes sistemas se comuniquem e troquem informações de forma
padronizada. Na prática, uma API pode ser utilizada para integrar o
sistema do projeto com o RMS, TOTVS ou outros serviços, permitindo
enviar e consultar dados automaticamente.</td>
</tr>
<tr>
<td style="text-align: center;"><p><strong>INTEGRAÇÃO</strong></p>
<p><strong>é o processo de conectar diferentes sistemas ou
aplicações para que possam trocar informações e executar processos de
forma automática e padronizada.</strong></p></td>
<td>Integração é a comunicação entre diferentes sistemas para troca
automática de informações. No projeto, uma integração pode permitir que
dados recebidos de um sistema externo sejam utilizados pela aplicação,
evitando lançamentos manuais e reduzindo erros de informação.</td>
</tr>
</tbody>
</table>

ie e cole abaixo)

**3. REFERÊNCIAS**

Coloque aqui as fontes que você utilizou como base para sua entrega,
como documentos, sites, vídeos, artigos, materiais da aula, entre
outros.

(Copie e c **REFERÊNCIAS**

BRASIL. **Portal da Nota Fiscal Eletrônica (NF-e)**. Governo Federal.
Disponível no Portal da NF-e. Acesso em: 09 set. 2026.

IBM. **O que é um SLA (Service Level Agreement)?** IBM. 2024. Acesso em:
09 set. 2026.

MDN WEB DOCS. **API — Application Programming Interface**. Mozilla
Developer Network. Acesso em: 09 set. 2026.

NIST — NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **Role-Based
Access Control (RBAC)**. Computer Security Resource Center. Acesso em:
09 set. 2026.

NIST — NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **Computer
Security Resource Center**. Publicações e referências sobre segurança,
continuidade e recuperação de sistemas. Acesso em: 09 set. 2026.

TOTVS. **Soluções para Varejo**. TOTVS. Acesso em: 09 set. 2026.

ole abaixo)

**4. FEEDBACK**

**Esta parte será preenchida pelo líder responsável pela equipe.**

(Não coloque nada aqui)

**Responsável pelo feedback:**

**Data: 09/09/2026**
